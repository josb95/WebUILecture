from flask import Flask, render_template
import RPi.GPIO as g
import time

g.setmode(g.BCM)
g.setup(18, g.OUT)
pwm = g.PWM(18, 1000)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', status="None")

@app.route('/led/on_1')
def led_on_1():
    # g.setup(20, g.OUT)
    g.setup(21, g.OUT)
    # g.output(20, True)
    g.output(21, False)
    dutycycle = 0;
    pwm.start(dutycycle)
    while(True):
        dutycycle = dutycycle + 2;
        pwm.ChangeDutyCycle(dutycycle)
        time.sleep(0.02)
        print(dutycycle)
        if (dutycycle > 50):
            break;

    return render_template('index.html', status="On_1")

@app.route('/led/on_2')
def led_on_2():
    # g.setup(20, g.OUT)
    g.setup(21, g.OUT)
    # g.output(20, False)
    g.output(21, False)
    dutycycle = 0;
    pwm.start(dutycycle)
    while(True):
        dutycycle = dutycycle + 2;
        pwm.ChangeDutyCycle(dutycycle)
        time.sleep(0.02)
        print(dutycycle)
        if (dutycycle > 50):
            break;

    return render_template('index.html', status="On_2")

@app.route('/led/off')
def led_off():
    # g.setup(20, g.OUT)
    g.setup(21, g.OUT)
    # g.output(20, False)
    g.output(21, False)
    dutycycle = 50;
    pwm.start(dutycycle)
    while(True):
        dutycycle = dutycycle - 2;
        pwm.ChangeDutyCycle(dutycycle)
        time.sleep(0.02)
        print(dutycycle)
        if (dutycycle <= 0):
            break;

    return render_template('index.html', status="Off")



if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80, debug = True)
