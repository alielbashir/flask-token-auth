from flask import Flask, request
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError
from sqlalchemy import create_engine
from models import User

from helpers import *

# Setup DB
base = declarative_base()
engine = create_engine('sqlite:///users.db')
base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)


@app.route('/api/register', methods=["POST"])
def register():
    def createUser(username):
        user = User(username=username)
        session.add(user)
        try:
            session.commit()
        except IntegrityError:
            return jsonify({"error": "User already exists"})
        return jsonify(user.serialize)

    req = request.json
    username = req["username"]

    user = createUser(username)

    return user


@app.route("/api/users", methods=["POST"])
def users():
    def getUserName(userId):
        try:
            username = session.query(User.username).filter_by(userId=userId).one()[0]
        except NoResultFound:
            return jsonify({"error": "User not found"})
        return jsonify({"username": username})

    headers = request.headers
    # If token exists
    if "Authorization" in headers:
        token = headers["Authorization"][7:]
        decodedRequest = decode(token)
        userId = decodedRequest["userId"]

        if expired(decodedRequest):
            return generateToken({"userId": userId})
        else:
            return getUserName(userId)
    # If token doesnt exist
    else:
        return generateToken({"userId": request.json["userId"]})


if __name__ == '__main__':
    app.debug = False
    app.run(host='0.0.0.0', port=5000)
