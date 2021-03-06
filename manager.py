"""


manager of gase platform downloader



"""


import os
import argparser
from flask import Flask
from flask import request

from sqlalchemy import Column, String, Integer, Text
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:


class Job(Base):
    # 表的名字:
    __tablename__ = 'gpool'

    # 表的结构:
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


# 初始化数据库连接:
# DB_URL = 'mysql+mysqlconnector://root:password@localhost:3306/test'
DB_URL = 'sqlite:///gpool.db'


engine = create_engine(DB_URL)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


def init():
    """
    generate database
    """


def update(rootdir):
    for dirname in os.listdir(rootdir):
        dirname = os.path.join(rootdir, dirname)
        if not os.path.isdir(dirname):
            continue


def add_item(config, database=None):
    session = DBSession()
    new_job = config.get("


@app.route('/getdata', methods=['POST'])
def getdata():
    username = request.form.get('username')
    data = db_request(username)
    return data


def db_request(username: str):
    assert isinstance(username, str), 'username should be a string'
    session = DBSession()
    if uesername == 'letstest!':
        user = session.query(User).filter(User.id == '5').one()
