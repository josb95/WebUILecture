from flask import Flask

app = Flask( __name__ )

@app.route( "/" ) # index.html, main.html과 같은 역할
def hello():
    return "<h1>Hello World!</h1>"

@app.route("/message/<int:message_id>")
def get_message(message_id):
    return "message id: %d" % message_id

@app.route("/first/<int:messageid>")
def get_first(messageid):
    return "<h1>%d<h1>" % (messageid + 5)

host_addr = "0.0.0.0" # 모든 아이피 접속 허용
port_num = "8080"

if __name__ == "__main__":
    app.run( host = host_addr, port = port_num)
    # app.run( host = host_addr )
