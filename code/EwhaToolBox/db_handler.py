import pyrebase
import json

class DBModule:
    def __init__(self):
        with open("./EwhaToolBox/auth/firebaseAuth.json") as f:

            config = json.load(f)

        self.firebse = pyrebase.initialize_app(config)
        self.db=self.firebse.database()

    
    ## 사용자
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
    
    def get_user(self, user_id):
        pass
    
    def signin(self, id, pwd):
        pass

    def signup(self, id, pwd):
        pass

    ## 게시글
    def insert_post(self, post_id, data):
        post = {
            "post_id" : data['post_id'],
            "writer_id" : data['writer_id'],
            "category" : data['category'],
            "title" : data['title'],
            "desc" : data['desc'],
            "period_start" : data['period_start'],
            "period_end" : data['period_end'],
            "price" : data['price'],
            "min_amount" : data['min_amount'],
            "max_amount" : data['max_amount'],
            "image_url" : data['image_url'],
            "option_cnt" : data['option_cnt'],
            "status" : data['status']
        }
        self.db.child("post").child(post_id).set(post)
        return True
    
    def user_duplicate_check(self, user_id):
        users = self.db.child("user").get()
        for user in users.each():
            if (user.key() == user_id):
                return False
        return True
    
    def write_post(self):
        pass

    def post_list(self):
        pass

    def post_detail(self,post_id):
        pass


    ## 작성자
    def insert_writer(self, writer_id, data):
        writer = {
            "writer_id" : data['writer_id'],
            "post_id" : data['post_id'],
            "form_url" : data['form_url']
        }
        self.db.child("writer").child(writer_id).set(writer)
        return True
    
    def writer_duplicate_check(self, writer_id):
        writers = self.db.child("writer").get()
        for writer in writers.each():
            if (writer.key() == writer_id):
                return False
        return True


    ## 공지
    def insert_notice(self, notice_id, data):
        notice = {
            "notice_id" : data['notice_id'],
            "post_id" : data['post_id'],
            "writer_id" : data['writer_id'],
            "notice_desc" : data['notice_desc']
        }
        self.db.child("notice").child(notice_id).set(notice)
        return True
    
    def notice_duplicate_check(self, notice_id):
        notices = self.db.child("notice").get()
        for notice in notices.each():
            if (notice.key() == notice_id):
                return False
        return True
   
    
    ## 리뷰
    def insert_review(self, review_id, data):
        review = {
            "review_id" : data['review_id'],
            "post_id" : data['post_id'],
            "writer_id" : data['writer_id'],
            "review_desc" : data['review_desc']
        }
        self.db.child("review").child(review_id).set(review)
        return True
    
    def review_duplicate_check(self, review_id):
        reviews = self.db.child("review").get()
        for review in reviews.each():
            if (review.key() == review_id):
                return False
        return True


    ## Q&A - Q
    def insert_question(self, question_id, data):
        question = {
            "question_id" : data['question_id'],
            "post_id" : data['post_id'],
            "writer_id" : data['writer_id'],
            "question_desc" : data['question_desc']
        }
        self.db.child("question").child(question_id).set(question)
        return True
    
    def question_duplicate_check(self, _id):
        questions = self.db.child("question").get()
        for question in questions.each():
            if (question.key() == question_id):
                return False
        return True
    

    ## Q&A - A
    def insert_answer(self, answer_id, data):
        answer = {
            "answer_id" : data['answer_id'],
            "question_id" : data['question_id'],
            "post_id" : data['post_id'],
            "writer_id" : data['writer_id'],
            "answer_desc" : data['answer_desc']
        }
        self.db.child("answer").child(answer_id).set(answer)
        return True
    
    def answer_duplicate_check(self, answer_id):
        answers = self.db.child("answer").get()
        for answer in answers.each():
            if (answer.key() == answer_id):
                return False
        return True


    ## 디자인
    def insert_design(self, design_id, data):
        design = {
            "design_id" : data['design_id'],
            "user_id" : data['user_id'],
            "design_name" : data['design_name'],
            "memo" : data['memo'],
            "design_image_url" : data['design_image_url']
        }
        self.db.child("design").child(design_id).set(design)
        return True
    
    def design_duplicate_check(self, design_id):
        designs = self.db.child("design").get()
        for design in designs.each():
            if (design.key() == design_id):
                return False
        return True

    ## 주문
    def insert_order(self, order_id, data):
        order = {
            "order_id" : data['order_id'],
            "post_id" : data['post_id'],
            "user_id" : data['user_id'],
            "size" : data['size'],
            "amount" : data['amount'],
            "deliver" : data['deliver'],
            "address" : data['address']
        }
        self.db.child("order").child(order_id).set(order)
        return True
    
    def order_duplicate_check(self, order_id):
        orders = self.db.child("order").get()
        for order in orders.each():
            if (order.key() == order_id):
                return False
        return True


    #데이터 쓰기 체크 
    def write_data(self, data):
        # Firebase 데이터베이스에 데이터 쓰기
        self.db.child("example").set(data)
        print("데이터 쓰기가 완료되었습니다.")





