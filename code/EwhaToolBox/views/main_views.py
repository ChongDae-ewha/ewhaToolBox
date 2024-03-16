import io
import sys
import json

<<<<<<< HEAD:code/EwhaToolBox/app.py
from flask import Flask, jsonify, render_template, request
from database import DBHandler

app = Flask(__name__)
DB = DBHandler()

@app.route("/")
def view_index():
    return render_template("index.html")
=======
from flask import Flask, jsonify, request, Blueprint,redirect, url_for

bp=Blueprint('main',__name__,url_prefix='/')

>>>>>>> 9395b5b9a4c434244d9b4b0694dcfb5713895515:code/EwhaToolBox/views/main_views.py

@bp.route("/")
def index():
    return "index"

@bp.route("/user")
def user():
    return ""

<<<<<<< HEAD:code/EwhaToolBox/app.py
@app.route("/user/signup")
def view_signup():
    return render_template("signup.html")

@app.route("/user/signup/submit")
def reg_user_submit():
    user_id = request.args.get("user_id")
    pw = request.args.get("pw")
    nickname = request.args.get("nickname")
    email = request.args.get("email")
    phone = request.args.get("phone")
    address = request.args.get("address")

@app.route("/user/signup/post", methods=["POST"])
def reg_user_post():
    data = request.form
    return render_template("signup_result.html", data=data)


@app.route("/user/signin")
def view_signin():
    return render_template("signin.html")

def login():
    return ""
=======
@bp.route("/user/signup", methods=['POST'])
def reg_user():
    user_id = request.args.get('user_id')
    pw = request.args.get('pw')
    name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone')
    address = request.args.get('address')

>>>>>>> 9395b5b9a4c434244d9b4b0694dcfb5713895515:code/EwhaToolBox/views/main_views.py


