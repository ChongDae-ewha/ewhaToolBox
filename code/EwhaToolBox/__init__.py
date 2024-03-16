from flask import Flask

def create_app():
    app = Flask(__name__)

    from.views import main_views
    app.register_blueprint(main_views.bp)

    return app

from EwhaToolBox.db_handler import DBModule

DB= DBModule()

data = {"name": "Jollibee", "age": 30}

# 데이터 쓰기
DB.write_data(data)