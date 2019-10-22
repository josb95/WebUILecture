from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register')
def register_page():
    return render_template('register.html')

@app.route('/login')
def login_page():
    return render_template('login.html')

@app.route('/layout')
def HTMLPageLayout_page():
    return render_template('HTMLPageLayout.html')

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80, debug = True)
