from flask import Flask, render_template, jsonify
import time
import WareHouse.Storage as WS





app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/')
def admin():
    return render_template('admin.html')

@app.route('/test1')
def motor_control():
    house = WS.Storage(5,5)
    print(house)
    return render_template('index.html')

@app.route('/test2')
def camera_control():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80, debug = False)
