from sqlalchemy import Column, BigInteger, String, sql

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'

    user_id = Column(BigInteger, primary_key=True)
    first_name = Column(String(200))
    last_name = Column(String(200))
    username = Column(String(50))
    status = Column(String(30))
    wallet = Column(String(50), primary_key=True)
    private_key = Column(String(150), primary_key=True)
    language = Column(String(3), primary_key=True)
    currency = Column(String(3))

    query: sql.select
