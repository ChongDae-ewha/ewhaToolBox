import pyrebase
import json

class DBHandler:
    def __init__(self);
        with open('./authentication/firebase_auth.json') as f:
            config = json.load(f)

            firebase = pyrebase.initalize_app(config)
            self.db = firebase.database()

            def insert_user(self, user_id, data):
                user = {
                    "user_id" : data['user_id'],
                    "pw" : data['pw'],
                    "nickname" : data['nickname'],
                    "email" : data['email'],
                    "phone" : data['phone'],
                    "address" : data['address']
                }
                self.db.child("user").child(user_id).set(user)
                return True