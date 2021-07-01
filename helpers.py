import jwt
from flask import jsonify
from datetime import datetime


def generateToken(message, key="secret"):
    JWT_EXPIRY = 900 # 15 minutes == 900 seconds expiry time
    message["exp"] = datetime.utcnow().timestamp() + JWT_EXPIRY
    token = jwt.encode(message, key=key, algorithm="HS256")
    return jsonify({"token": token})


def expired(json):
    return json["exp"] < datetime.utcnow().timestamp()


def decode(token, key="secret"):
    decoded = jwt.decode(token, key=key, algorithms="HS256", options={"verify_exp": False})
    return decoded


