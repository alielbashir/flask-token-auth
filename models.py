from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
base = declarative_base()


class User(base):

    MAX_USERNAME = 32

    __tablename__ = "users"
    userId = Column(Integer, primary_key=True)
    username = Column(String(MAX_USERNAME), unique=True)

    @property
    def serialize(self):
        return {
            "userId": self.userId,
            "username": self.username
        }


engine = create_engine('sqlite:///users.db')
base.metadata.create_all(engine)
