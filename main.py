# FastAPIをインポート
from fastapi import FastAPI
from pydantic import BaseModel

import db_model as m
import db_setting as s

class UserBase(BaseModel):
  name : str
  mail: str
  sex :str

app = FastAPI()

# GETメソッドでルートURLにアクセスされたときの処理
@app.get("/")
async def root():
  return {"message": "Hello World"}

@app.get("/users", tags=["users"])
async def read_users():
  #DBからユーザ情報を取得
  result = s.session.query(m.Users).all()
  return result

# POSTメソッドで /usersにアクセスしたときの処理
# ユーザーの新規登録
@app.post("/users", tags=["users"])
async def create_user(data: UserBase):
  # Usersモデルを変数に格納
  user = m.Users()
  # セッションを新規作成
  session = s.session()
  s.session.add(user)
  try:
    #リクエストBodyで受け取ったデータを流し込む
    user.name = data.name
    user.mail = data.mail
    user.sex = data.sex
    #永続的にDBに反映
    session.commit()
  except:
    # DBへの反映は行わない
    session.rollback()
    raise
  finally:
    # 正常・異常どちらでもセッションは終わっておく
    session.close()

# DELETEメソッドで /usersにアクセスしたときの処理
# ユーザーの削除
@app.delete("/users/{id}", tags=["users"])
async def delete_user(id: int):
  # セッションを新規作成
   session = s.session()
   try:
    # 指定されたuser_idのユーザーを削除
       query = s.session.query(m.Users)
       query = query.filter(m.Users.user_id == id)
       query.delete()
        # 永続的にDBに反映
       session.commit()
   except:
       session.rollback()
       raise
   finally:
       session.close()
