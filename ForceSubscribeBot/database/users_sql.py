from sqlalchemy import Column, BIGINT, String
from . import BASE, SESSION


class Users(BASE):
    __tablename__ = "users"
    __table_args__ = {'extend_existing': True}
    user_id = Column(BIGINT, primary_key=True)
    channels = Column(String, nullable=True)

    def __init__(self, user_id):
        self.user_id = user_id


Users.__table__.create(checkfirst=True)


async def num_users():
    try:
        return SESSION.query(Users).count()
    finally:
        SESSION.close()
