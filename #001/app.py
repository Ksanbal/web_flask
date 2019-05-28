# from flask import Flask, render_template, request
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite" # app.config : 설정값
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'test'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

    def __str__(self):
        return '<User%>' %self.username


@app.route("/")
def hel():
    user = User(username='moon', email='123')
    db.session.add(user)
    db.session.commit()
    return user.username


db.create_all()

#
# @app.before_first_request
# def fi():
#     print("first")
#     db.create_all()

#
# @app.route('/')
# def all1():
#     # x = User.query.all()
#     x = User.query.filter(User.username == 'moon').all()
#
#     x.username = 'sun'
#     db.session.commit()
#
#     db.session.remove(x)
#     db.session.commit()
#     print(x)
#     for _ in x:
#         print(_.username)
#     return 'x'


#
# @app.route('/') # 아무것도 입력하지 않았을 때 상태.
# def hello_world():
#     return 'Hello World!'
#
#
# @app.route('/<a>') # /뒤로 입력받는 문자를 표시하는 페이지
# def first_page(a):
#     if a == 't':
#         return 'Nope'
#     else:
#         print(dir(request.user_agent))
#         return render_template('Index.html', a=a)
#

if __name__ == '__main__':
    app.run()
