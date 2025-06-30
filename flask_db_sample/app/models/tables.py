from sqlalchemy import Column, ForeignKey, Integer, String
from app.database.sqlAlchemy import db, Base
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.orm import  Mapped, mapped_column
from typing import List
import json
from dataclasses import dataclass

class AlchemyEncoder(json.JSONEncoder):

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                data = obj.__getattribute__(field)
                try:
                    json.dumps(data) # this will fail on non-encodable values, like other classes
                    fields[field] = data
                except TypeError:
                    fields[field] = None
            return fields

        return json.JSONEncoder.default(self, obj)
# 

@dataclass
class Student(db.Model):
    __tablename__ = 'students'
    __allow_unmapped__ = True  
    #data properties to return
    id : int
    fname: str
    lname: str
    subject: str
    comments: List['Comment']

    #datatable
    id = Column(Integer, primary_key=True)
    fname = Column(String(250), nullable=False)
    lname = Column(String(250), nullable=False)
    subject = Column(String(250))
    comments = db.relationship(
        "Comment",
        backref= "id",
        cascade="all, delete-orphan"
    )

@dataclass
class Comment(db.Model):
    __tablename__ = 'comments'
    __allow_unmapped__ = True   
    #data properties to return
    comment_id: int
    commenter_id: str
    comment: str
    p_name: str
    #datatable
    comment_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    commenter_id = db.Column(db.Integer, db.ForeignKey('students.id'), nullable=True)
    commenter_username = db.Column(db.String(80), nullable=True)
    comment = db.Column(db.String(80), nullable=False)
    p_name = db.Column(db.String(80), db.ForeignKey('projects.project_name'), nullable=False)
    
@dataclass    
class Project(db.Model):
    __tablename__ = 'projects'
    # https://github.com/sqlalchemy/sqlalchemy/discussions/10117
    # ORM annotations should normally make use of the ``Mapped[]`` generic type, or other ORM-compatible generic type, as a container for the actual type, which indicates the intent that the attribute is mapped. Class variables that are not intended to be mapped by the ORM should use ClassVar[].  To allow Annotated Declarative to disregard legacy annotations which don't use Mapped[] to pass, set "__allow_unmapped__ = True" on the class or a superclass this class.

    __allow_unmapped__ = True
    #data properties to return
    project_id: str
    project_name: str
    owner_id: str
    owner_username: str
    comments: List['Comment']

    #datatable
    project_id = db.Column(db.String(80), unique=True, primary_key=True)
    project_name  = db.Column(db.String(80), unique=True, nullable=True)
    owner_id = db.Column(db.String(80), unique=False, nullable=True)
    owner_username = db.Column(db.String(80), unique=False, nullable=True)
    comments = db.relationship(
        "Comment",
        backref= "project_name",
        cascade="all, delete-orphan"
    )

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    def __repr__(self):
        return '<User %r>' % self.username
    
