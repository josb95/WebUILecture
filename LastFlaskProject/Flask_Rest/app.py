from flask import Flask, render_template, jsonify
import time


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/motor')
def motor_control():
    return

@app.route('/camera')
def camera_control():
    return

@app.route('/')
