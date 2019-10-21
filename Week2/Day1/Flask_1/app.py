from flask import Flask
'''
app 객체를 이용해 라우팅 경로 설정
해당 라우팅 경로로 요청이 올 때 실행할 함수를 바로 밑에 작성
'''
app = Flask( __name__ )

@app.route( "/" ) # index.html, main.html과 같은 역할
def hello():
    return "<h1>Hello World!</h1>"

@app.route("/hello")
def hello_flask():
    return "<h2>Hello Flask!</h2>"

@app.route("/first")
def hello_first():
    return "<h3>Hello First!</h3>"

host_addr = "0.0.0.0" # 모든 아이피 접속 허용
port_num = "8080"

if __name__ == "__main__":
    app.run( host = host_addr, port = port_num)
    # app.run( host = host_addr )
