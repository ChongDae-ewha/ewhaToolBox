import pyrebase
import json

class DBModule:
    def __init__(self):
        with open("./EwhaToolBox/auth/firebaseAuth.json") as f:

            config = json.load(f)

        self.firebse = pyrebase.initialize_app(config)
        self.db=self.firebse.database()


    def login(self,id,pwd):
        pass

    def signup(self, user_id, data):
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

    def write_post(self,user,contents):
        pass

    def post_list(self):
        pass

    def post_detail(self,post_id):
        pass

    def get_user(self, user_id):
        pass

    #데이터 쓰기 체크 

    def write_data(self, data):
        # Firebase 데이터베이스에 데이터 쓰기
        self.db.child("example").set(data)
        print("데이터 쓰기가 완료되었습니다.")





