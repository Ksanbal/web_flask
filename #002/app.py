from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = SQLAlchemy(app)

db.create_all()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
def hello_world():
    user = User(username='moon', email='123')
    db.session.add(user)
    db.session.commit()
    return user.username

#
# @app.before_first_request
# def fi():
#     print("first")
#     db.create_all()

#
# @app.route('/')
# def all():
#     x = User.query.filter(User.username == 'moon').all()
#
#     x.username = 'sun'
#     db.session.commit()
#
#     db.session.remove(x)
#     db.session.commit()
#     print(x)
#
#     for _ in x:
#         print(_.username)
#
#     return 'x'


if __name__ == '__main__':
    app.run()
