from sqlalchemy import Column, Integer, String

from db.database import Base


class DBSystemUser(Base):
    __tablename__ = 'systemUser'
    userId = Column(Integer, primary_key=True, index=True)
    username = Column(String(100))
    email = Column(String(100))
    password = Column(String(256))

