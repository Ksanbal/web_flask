from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/') # 아무것도 입력하지 않았을 때 상태.
def hello_world():
    return 'Hello World!'


@app.route('/<a>') # /뒤로 입력받는 문자를 표시하는 페이지
def first_page(a):
    if a == 't':
        return 'Nope'
    else:
        print(dir(request.user_agent))
        return render_template('Index.html', a=a)


if __name__ == '__main__':
    app.run()
