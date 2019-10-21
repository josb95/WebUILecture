from flask import Flask, render_template

app = Flask(__name__)

@app.route('/hello_loop')
def hello_name():
    value_list = ['list1', 'list2', 'list3']
    return render_template('loop.html', values = value_list)

host_addr = "0.0.0.0"
port_num = "8080"

if __name__ == "__main__":
    app.run( host = host_addr, port = port_num)
