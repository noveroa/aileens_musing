import os
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
basedir = os.path.abspath(os.path.dirname(__file__))

Base = declarative_base()
engine = create_engine('sqlite:///' + os.path.join(basedir, 'musings_db.db'))
Base.metadata.create_all(engine)
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()