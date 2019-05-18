# #001_WebFlask

## http 프로토콜이란
 - 브라우저와 서버 간 데이터를 주고 받는 방식
 - Stateless Protocall
 	- 각각의 데이터 요청이 서로 독립적이다.
 	- 서버가 정보를 추가적으로 관리하지 않아도 되고, 다수의 요청 처리 및 서버의 부하를 줄일 수 있는 성능의 이점이 있다.
 	- but, http 쿠키를 이용해 데이터간의 상호작용을 하는 세션을 만들 수 있다. 
 - TCP/IP 통신에서 동작하고, 기본 포트 : 80
 - 프록시
 	- 애플리케이션 계층에서 클라이언트와 서버를 중계하고 중간에 캐싱, 필터링, 로드 밸런싱 등 다양한 기능 수행이 가능하다.
 - 

## Request와 Response
 ### 1. Request
 - Client(Browser) to Server
 - HTTP Verbs(요청 메소드)를 이용하여 서버에 특정 데이터를 요청한다.
 > get : 존재하는 자원 요청
 > post : 새로운 자원 생성
 > put : 존재하는 자원 변경
 > delete : 존재하는 자원 삭제
 > head : 서버 헤더 정보를 획득, get과 달리 response body를 반환하지 않는다.
 > options : 서버 옵션들을 확인하기 위한 요청, CORS에서 사용한다.
 >> CORS : 다른 도메인으로부터 리소스를 받아올 수 있도록 제시된 request 방법


 ### 2. Response
 - Server to Client
 - 서버에서 설정하여 상태코드를 응답하는 것
 - 주요 상태코드
 > 2xx - 성공
 > 3xx - 리다이렉션
 >- 이전 주소의 데이터를 요청하여 서버에서 새로운 url로 유도하는 경우
 
 > 4xx - 클라이언트 에러
 > 5xx - 서버 에러


## template langauge (jinja2)
## orm (SQLAlchemy)
- SQL문인 아닌 객체지향 언어를 사용해서 관리할 수 있게 해준다.


