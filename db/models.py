from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey

from sqlalchemy import Column, Integer, String, Boolean, DateTime

from db.database import Base


class DBSystemUser(Base):
    __tablename__ = 'systemUser'
    userId = Column(Integer, primary_key=True, index=True)
    username = Column(String(100))
    email = Column(String(100))
    password = Column(String(256))
    images = relationship('DBImage', back_populates='user')


class DBImage(Base):
    __tablename__ = 'images'
    imageId = Column(Integer, primary_key=True, index=True)
    image_file_url = Column(String(256))
    image_type = Column(String(50))
    uploaded_by_user = Column(Integer, ForeignKey('systemUser.userId'))
    user = relationship('DBSystemUser', back_populates='images')
    color_style = Column(Integer)
    additional_parameters = Column(Integer)
    status = Column(Boolean)
    result_image_url = Column(String(256))
    timestamp = Column(DateTime)
