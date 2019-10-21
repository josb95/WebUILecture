from flask import Flask, url_for

app = Flask( __name__ )

@app.route( "/hello/" ) # index.html, main.html과 같은 역할
def hello():
    return "<h1>Hello World!</h1>"

@app.route("/profile/<username>")
def get_profile(username):
    return "profile : " + username

host_addr = "0.0.0.0" # 모든 아이피 접속 허용
port_num = "8080"

if __name__ == "__main__":
    with app.test_request_context():
        print(url_for('hello'))
        print(url_for('get_profile', username = 'flash'))
