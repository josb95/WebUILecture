from flask import Flask, render_template
import RPi.GPIO as g

g.setmode(g.BCM)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', status="None")

@app.route('/led/on')
def led_on():
    g.setup(15, g.OUT)
    g.output(15, True)
    return render_template('index.html', status="On")

@app.route('/led/off')
def led_off():
    g.setup(15, g.OUT)
    g.output(15, False)
    return render_template('index.html', status="Off")



if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80, debug = True)
