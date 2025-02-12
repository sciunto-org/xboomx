# coding=utf-8
import os
from xboomx.config import config_dir
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String

__author__ = 'Victor Häggqvist'


try:
    os.makedirs(config_dir, exist_ok=True)
except OSError as e:
    print(f"Error creating the directory {config_dir}: {e}")
    raise

dbname = 'xboomx_sqlite.db'
dbpath = os.path.join(config_dir, dbname)
dsn = 'sqlite:///%s' % dbpath

engine = create_engine(dsn, echo=False)
Base = declarative_base()


class PathItem(Base):
    __tablename__ = 'pathitems'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    count = Column(Integer)

    def __repr__(self):
        return f"<PathItem(name='{self.name}', count='{self.count}')>"


def get_session():
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()
