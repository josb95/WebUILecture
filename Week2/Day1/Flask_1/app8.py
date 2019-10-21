from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello_if/<value>')
def hello_html(value):
    value = int(value)
    return render_template('condition.html', data = value)

host_addr = "0.0.0.0"
port_num = "8080"

if __name__ == "__main__":
    app.run( host = host_addr, port = port_num)
