import io
import sys
import json

from flask import Flask, jsonify, render_template, request
from database import DBHandler

app = Flask(__name__)
DB = DBHandler()

@app.route("/")
def view_index():
    return render_template("index.html")

@app.route("/user")
def user():
    return ""

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


if __name__ == "main":
    app.run(host = "0.0.0.0")