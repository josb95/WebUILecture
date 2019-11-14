from flask import Flask, render_template
import RPi.GPIO as g
import time

g.setmode(g.BCM)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', motor_status="차량 정지", lift_status="지게 정지")

@app.route('/motor/f')
def motor_forward():
    g.setup(8, g.OUT)
    g.setup(7, g.OUT)
    g.setup(20, g.OUT)
    g.setup(21, g.OUT)
    g.output(8, True) #left
    g.output(7, False)
    g.output(20, True) #right
    g.output(21, False)
    return render_template('index.html', motor_status="전진")

@app.route('/motor/b')
def motor_backward():
    g.setup(8, g.OUT)
    g.setup(7, g.OUT)
    g.setup(20, g.OUT)
    g.setup(21, g.OUT)
    g.output(8, False) #left
    g.output(7, True)
    g.output(20, False) #right
    g.output(21, True)
    return render_template('index.html', motor_status="후진")

@app.route('/motor/fl')
def motor_foreleft():
    g.setup(8, g.OUT)
    g.setup(7, g.OUT)
    g.setup(20, g.OUT)
    g.setup(21, g.OUT)
    g.output(8, False) #left
    g.output(7, False)
    g.output(20, True) #right
    g.output(21, False)
    return render_template('index.html', motor_status="좌회전")

@app.route('/motor/fr')
def motor_foreright():
    g.setup(8, g.OUT)
    g.setup(7, g.OUT)
    g.setup(20, g.OUT)
    g.setup(21, g.OUT)
    g.output(8, True) #left
    g.output(7, False)
    g.output(20, False) #right
    g.output(21, False)
    return render_template('index.html', motor_status="우회전")

@app.route('/motor/rl')
def motor_rearleft():
    g.setup(8, g.OUT)
    g.setup(7, g.OUT)
    g.setup(20, g.OUT)
    g.setup(21, g.OUT)
    g.output(8, False) #left
    g.output(7, False)
    g.output(20, False) #right
    g.output(21, True)
    return render_template('index.html', motor_status="역좌회전")

@app.route('/motor/rr')
def motor_rearright():
    g.setup(8, g.OUT)
    g.setup(7, g.OUT)
    g.setup(20, g.OUT)
    g.setup(21, g.OUT)
    g.output(8, False) #left
    g.output(7, True)
    g.output(20, False) #right
    g.output(21, False)
    return render_template('index.html', motor_status="역우회전")

@app.route('/motor/ms')
def motor_stop():
    g.setup(8, g.OUT)
    g.setup(7, g.OUT)
    g.setup(20, g.OUT)
    g.setup(21, g.OUT)
    g.output(8, False) #left
    g.output(7, False)
    g.output(20, False) #right
    g.output(21, False)
    return render_template('index.html', motor_status="차량 정지")

@app.route('/motor/lu')
def lift_up():
    g.setup(23, g.OUT)
    g.setup(24, g.OUT)
    g.output(23, True)
    g.output(24, False)
    return render_template('index.html', lift_status="지게 상승")

@app.route('/motor/ld')
def lift_down():
    g.setup(23, g.OUT)
    g.setup(24, g.OUT)
    g.output(23, False)
    g.output(24, True)
    return render_template('index.html', lift_status="지게 하강")

@app.route('/motor/ls')
def lift_stop():
    g.setup(23, g.OUT)
    g.setup(24, g.OUT)
    g.output(23, False)
    g.output(24, False)
    return render_template('index.html', lift_status="지게 정지")

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80, debug = True)
