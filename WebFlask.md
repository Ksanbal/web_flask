# WebFlask
## 순서링크 
1. [1. #001](#￼￼#001)
2. [2. #002](￼#002)

## #001
### http 프로토콜이란
* 클라이언트(브라우저)와 서버 간 데이터를 주고 받는 방식
* Stateless Protocol
	* 각각의 데이터 요청이 서로 독립적이다.
	* 서버가 정보를 추가적으로 관리하지 않아도 되고, 다수의 요청 처리 및 서버의 부하를 줄일 수 있는 성능의 이점이 있다.
	* but, http 쿠키를 이용해 데이터간의 상호작용을 하는 세션을 만들 수 있다.
* TCP/IP 통신에서 동작하고, 기본 포트 : 80
* 프록시
	* 애플리케이션 계층에서 클라이언트와 서버를 중계하고 중간에 캐싱, 필터링, 로드 밸런싱 등 다양한 기능 수행이 가능하다.
#### HTTP로 제어할 수 있는 것
* 캐시 : 캐시되는 방식 제어가능, 서버는 캐시 대상과 기간 지시 가능, 클라이언트는 저장된 문서의 무시를 지시가능
* orgin 제약사항 완화 : 프라이버시 침해를 막기 위해, 동일한 origin으로 온 페이지만 전체 정보에 접근할 수 있다. but, http 헤더를 이용해 완화할 수 있다.
* 인증 : WWW-Authenticate 또는 유사한 헤더, http 쿠키를 이용해 특정세션에서 특정 사용자만 접근할 수 있게 한다.
* 프록시와 터널링
* 세션 : 쿠키를 사용하여 http가 기본적으로 Stateless 프로토콜이지만 세션을 만들어 준다.

### Request와 Response
#### 1. Request
* Client(Browser) to Server
* 단순히 해당 URL의 HTML만 요청하는 것이 아니라 추가로 요청한 브라우저의 종류, 위치 등 다양한 정보를 같이 전송한다.
* HTTP Verbs(요청 메소드)를 이용하여 서버에 특정 데이터를 요청한다.
get : 존재하는 자원 요청

post : 새로운 자원 생성

put : 존재하는 자원 변경

delete : 존재하는 자원 삭제

head : 서버 헤더 정보를 획득, get과 달리 response body를 반환하지 않는다.

options : 서버 옵션들을 확인하기 위한 요청, CORS에서 사용한다.> > CORS : 다른 도메인으로부터 리소스를 받아올 수 있도록 제시된 request 방법* 구성 : Method, Path, protocol's version, Hearders
#### 2. Response
* Server to Client
* 서버에서 설정하여 상태코드를 응답하는 것
* 주요 상태코드
> 2xx - 성공  
>   
> 3xx - 리다이렉션 : 이전 주소의 데이터를 요청하여 서버에서 새로운 url로 유도하는 경우  
>   
> 4xx - 클라이언트 에러  
>   
> 5xx - 서버 에러 구성 : protocol's version, Status code, Status message, Headers  
### template language (jinja2)
### orm (SQLAlchemy)
- SQL문인 아닌 객체지향 언어를 사용해서 관리할 수 있게 해준다.

```python
from flask import Flask, render_template, request


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
```

- - - -

## #002
### SQLAlchemy
#### 데이터 자료형 타입의 종류
##### 1. Generic Types
###### - Python 타입의 데이터 타입
###### - 만약 대상 DB에서 없는 자료형을 사용할 경우 비슷한 타입으로 생성가능하다.
1. BigInteger : 데이터의 크기가 큰 int integers (8바이트)
2. Boolean : True와 False로 나타내는 datatype
3. Date : 년,월,일의 날짜를 나타내는 타입
4. DateTime : 날짜와 시간의 조합
5. Enum : 열거형,  서로 관련이 있는 상수들의 집합
6. Float : 실수
7. Integer : 정수
8. Interval : 두 date간의 차이를 나타내는 기간
9. LargeBinary : 데이터의 크기가 큰 binary (2진수)
10. MatchType : ?
11. Numeric : 고정 소수점 
12. PickleType : bytes로 쓰여진 객체를 읽고 쓸 수 있는 타입
13. SchemaType :  ?
14. SmallInteger : 데이터의 크기가 작은 int integers (2바이트)
15. String : 연속된 문자열을 쓸 수 있는 타입
16. Text : 가변적인 사이즈의 string 타입
17. Time : 시,분,초의 시간을 나타내는 타입
18. Unicode : 가변적인 길이의 유니코드 string 타입
19. UnicodeText : 무한한 길이의 유니코드 string 타입

##### 2.  Standard & Multiple Vendor Type
###### - 대상 DB에 상관없이 사용하는 타입,
###### - 원하는 타입을 정확하게 지정할 수 있으나, 대상 DB에 없을 경우 작동하지 않을 수 있다.
1. ARRAY : 배열
2. BIGINT : 8바이트의 SQL int 타입
3. BINARY 
4. BLOB : DB 외부에 바이너리 타입으로 이루어진 파일을 저장하는 타입
5. BOOLEAN 
6. CHAR 
7. CLOB : DB 외부에 문자열 타입으로 대용량 파일을 저장하는 타입
8. DATE 
9. DATETIME 
10. DECIMAL 
11. FLOAT
12. INT : 4바이트의 SQL int 타입
13. JSON : JSON 파일을 저장 할 수 있고, 관계형 구조로 JSON 문서를 분석하고 가져올 수 있다.
14. INTEGER
15. NCHAR : n자로 고정된 유니코드 문자
16. NVARCHAR : n개의 가변 유니코드 문자
17. NUMERIC
18. REAL : 4바이트의 부동소수점 
19. SMALLINT : 2바이트의 SQL int 타입
20. TEXT
21. TIME
22. TIMESTAMP : 타임스탬핑을 통해 특정 시각을 가진 문자열 
23. VARBINARY : 가변형 binary
24. VARCHAR : 가변형 char

##### 3. Vendor-Specific Types
###### - 각 DB에 맞춰서 DB 패키지 안에 명시되어 있는 타입을 사용한다.


### WTF
#### 필드의 종류
###### - Field : 데이터베이스 테이블에서 데이터가 있는 Column, Attribute 와 같이 열을 나타내는 것
##### 1. Base Field
1. BooleanField : True, False로 저장되는 필드
2. DateField : datetime.date, 날짜
3. DatetimeField : datetime.datetime, 날짜와 시간의 조합
4. DecimalField : decimal.Decimal을 받는 텍스트 필드
5. FileField : 파일을 저장한다.
6. MultipleFileField : 여러 파일을 저장할 수 있는 필드
7. FloatField : float를 저장하는 필드
8. IntegerField : 정수로 저장하는 필드
9. RadioField : SelectField와 비슷하지만, 라디오 버튼을의 목록을 보여준다.
10. SelectField : 값과 레이블로 이루어진 선택들을 쌍으로 가진다. 값은 어떤것이 와도 된다.
11. SelectMultipleField : SelectField와 같지만 여러 선택을 가질 수 있다.
12. SubmitField : Submit 버튼이 눌리는 것을 체크하는 필드
13. StringField : 텍스트를 받는 필드

##### 2. Convenience Field
1. HiddenField : String필드이지만 입력창이 보이지 않는 필드이다.
2. PasswordField : 입력되는 값을 브라우저에서 보여주지 않는 필드이다.
3. TextAreaField : 여러줄을 입력 받을 수 있는 텍스트 필드.

##### 3. Field Enclosures
1. FormField : 데이터 폼을 저장하는 필드
2. FieldList : 필드의 인스턴스를 list로 저장하는 필드

##### 4. Custom Field
- 내가 수정할 수 있는 필드.


```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///example.sqlite"
# app.config : 설정값
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

#db.create_all()
@app.before_first_request
def fi():
    print("first")
    db.create_all()


@app.route('/')
def all1():
    # x = User.query.all()
    x = User.query.filter(User.username == 'moon').all()

    x.username = 'sun'
    db.session.commit()

    db.session.remove(x)
    db.session.commit()
    print(x)
    for _ in x:
        print(_.username)
    return 'x'
```