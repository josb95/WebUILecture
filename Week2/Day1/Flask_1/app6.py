from flask import Flask, render_template

app = Flask(__name__)

@app.route('/html_test')
def hello_html():
    return render_template('simple.html')

host_addr = "0.0.0.0"
port_num = "8080"

if __name__ == "__main__":
    app.run( host = host_addr, port = port_num)
