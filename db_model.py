from email.policy import default
from enum import Enum
import string
from xml.dom.domreg import well_known_implementations
from sqlalchemy import Column, Integer, String,DateTime
# CURRENT_TIMESTAMP関数を利用するためにインポート
from sqlalchemy.sql.functions import current_timestamp
# Baseクラス作成用にインポート
from sqlalchemy.ext.declarative import declarative_base
import enum
from  sqlalchemy import (Column,Integer,String,Enum,DateTime)

# Baseクラスを作成
Base = declarative_base()

class GenderType(str, enum.Enum):
    men = "男"
    women = "女"
    they = "その他"

class JobType(str, enum.Enum):
    engineer = "エンジニア"
    designer = "デザイナー"
    projectmanager = "プロジェクトマネージャー"
    producer = "プロデューサー"
    qa = "QA"
    sales = "セールス"
    maketer = "マーケター"

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(20), nullable=False)
    birth = Column(DateTime,nullable=False)
    gender = Column(Enum(GenderType, values_callable = lambda x: [e.value for e in x]), nullable = False)
    mail = Column(String(255),nullable=False)
    job = Column(Enum(JobType,values_callable = lambda x: [e.value for e in x]),default=None)
    work_at = Column(DateTime, default=None)
    created_at = Column(DateTime, nullable = False, server_default=current_timestamp())
    updated_at = Column(DateTime)

class Division(Base):
    __tablename__ = 'divisions'
    id = Column(Integer,primary_key = True, autoincrement=True)
    name = Column(String(255),nullable = False, default = 1)
    leader_user_id = Column(Integer,nullable = False)
    start_at = Column(DateTime,nullable = False)

class Belong(Base):
    __tablename__ = 'belongs'
    id = Column(Integer,nullable = False, primary_key = True,autoincrement = True)
    user_id = Column(Integer,nullable = False, default = 1)
    division_id = Column(Integer,nullable = False)
    start_at = Column(DateTime)
    end_id = Column(DateTime)



