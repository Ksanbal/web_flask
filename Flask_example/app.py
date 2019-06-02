from flask import Flask
from flask_admin import AdminIndexView #Admin 페이지 Home
from flask_admin.contrib.sqlamodel import ModelView
from extesnsions import admin, db
from models import User
import config

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = config.DATABASE_FILE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '123456790'
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'  # 부트스트립에서 지원하는 테마


db.init_app(app)
admin.init_app(app)  # init를 통해 Flask와 연동하겠다


class UserModelView(ModelView):  # Admin 페이지에서 보이는 기능 수정
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
    can_export = True
    create_modal = True


admin.add_view(UserModelView(User, db.session))


# adminIndexview = AdminIndexView(name='admin2') #Admin의 Home 페이지 수정
# admin.add_view(adminIndexview)


@app.before_first_request
def db_creat():
    db.create_all()


@app.route('/')  # 첫화면
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
