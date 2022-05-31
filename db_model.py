import enum

from sqlalchemy import Column, Integer, String, DateTime,Enum

# CURRENT_TIMESTAMP関数を利用するためにインポート
from sqlalchemy.sql.functions import current_timestamp
# Baseクラス作成用にインポート
from sqlalchemy.ext.declarative import declarative_base

#from sqlalchemy import (Column,Integer,String,Enum,)
#
#from db_model import Base

# Baseクラスを作成
Base = declarative_base()

class GenderType(str,enum.Enum):
  man = "男"
  woman ="女"
  others ="その他"

class UserType(str,enum.Enum):
  engineer = "エンジニア"
  designer = "デザイナー"
  project_manager = "プロジェクトマネージャー"
  producer = "プロデューサー"
  QA = "QA"
  sales = "セールス"
  marketer = "マーケター"

class Users(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True, autoincrement=True)
  name = Column(String(20), nullable=False)
  birth = Column(DateTime,nullable=False)
  gender = Column(Enum(GenderType, values_callable=lambda x: [e.value for e in x]), nullable=False)
  mail = Column(String,nullable=False)
  job = Column(Enum(UserType, values_callable=lambda x: [e.value for e in x]), nullable=False)
  work_at = Column(DateTime, default=None)
  created_at = Column(DateTime, nullable = False, server_default=current_timestamp())
  Updated_at = Column(DateTime)

class Divisions(Base):
  __tablename__ = 'divisions'
  id = Column(Integer,primary_key = True, autoincrement=True)
  name = Column(String,nullable = False, default = 1)
  leader_user_id = Column(Integer,nullable = False)
  start_at = Column(DateTime,nullable = False)

class Belongs(Base):
  __tablename__ = 'belongs'
  id = Column(Integer,nullable = False, default = 0, primary_key = True,autoincrement = True)
  user_id = Column(Integer,nullable = False, default = 1,)
  division_id = Column(Integer,nullable = False)
  start_at = Column(DateTime,nullable = False)
  end_at = Column(DateTime)
