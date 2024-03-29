from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
    return render_template('variable.html', name = user)

host_addr = "0.0.0.0"
port_num = "8080"

if __name__ == "__main__":
    app.run( host = host_addr, port = port_num)
