import io
import sys
import json

from flask import Flask,  render_template, jsonify, request, Blueprint, redirect, url_for
from ..db_handler import DBModule

bp = Blueprint('main',__name__,url_prefix='/')
DB = DBModule()


@bp.route("/")
def index():
    return "index"

@bp.route("/user")
def user():
    return ""

@bp.route("/user/signup")
def view_signup():
    return render_template("signup.html")

@bp.route("/user/signup/submit")
def reg_user_submit():
    user_id = request.args.get("user_id")
    pw = request.args.get("pw")
    nickname = request.args.get("nickname")
    email = request.args.get("email")
    phone = request.args.get("phone")
    address = request.args.get("address")

@bp.route("/user/signup/post", methods=["POST"])
def reg_user_post():
    data = request.form
    if DB.signup(data['user_id'], data):
        return render_template("signup_result.html", data=data)
    else:
        return render_template("signup_error.html")


@bp.route("/user/signin")
def view_signin():
    return render_template("signin.html")
