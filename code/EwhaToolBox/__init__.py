from flask import Flask

def create_app():
    app = Flask(__name__)

    from.views import main_views
    app.register_blueprint(main_views.bp)

    return app

from EwhaToolBox.db_handler import DBModule

DB= DBModule()

# data = {"name": "Jollibee", "age": 30}

data= {"user_id": "test", "pw": "1234", "nickname": "test", "email": "123@com", "phone": "010-1234-5678", "address": "서울시 강남구"}

# # 데이터 쓰기
DB.insert_user( "test", data )


DB.signin("test", "1234")



