from blog.database import Base
from sqlalchemy import String,Column,Integer,ForeignKey
from sqlalchemy.orm import relationship


class Blog(Base):
    __tablename__='blogs'
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String(50))
    body=Column(String(50))
    user_id=Column(Integer,ForeignKey('user.id')) 
    
    creator= relationship('User', back_populates="blogs")

class User(Base):
    __tablename__='user'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String(50))
    email=Column(String(100))
    password=Column(String(250))

    blogs=relationship('Blog', back_populates='creator')











