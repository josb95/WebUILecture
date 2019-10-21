from flask import Flask

app = Flask( __name__ )

@app.route( "/" ) # index.html, main.html과 같은 역할
def hello():
    return "<h1>Hello World!</h1>"

@app.route("/profile/<username>")
def get_profile(username):
    return "profile : " + username

@app.route("/first/<username>")
def get_first(username):
    return "<h3>Hello " + username + "!</h3>"

host_addr = "0.0.0.0" # 모든 아이피 접속 허용
port_num = "8080"

if __name__ == "__main__":
    app.run( host = host_addr, port = port_num)
