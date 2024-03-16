import io
import sys
import json

from flask import Flask, jsonify, request, Blueprint,redirect, url_for

bp=Blueprint('main',__name__,url_prefix='/')


@bp.route("/")
def index():
    return "index"

@bp.route("/user")
def user():
    return ""

@bp.route("/user/signup", methods=['POST'])
def reg_user():
    user_id = request.args.get('user_id')
    pw = request.args.get('pw')
    name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone')
    address = request.args.get('address')



