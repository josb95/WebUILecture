from flask import Flask, render_template, jsonify
import time
import cx_Oracle as ora
import WareHouse.Storage as WS





app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/customer')
def customer():
    return render_template('customer.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')


@app.route('/run') # 이 URI는 무한루프기 때문에 창고관리를 실행할때만 접속
def run():
    # DB에서 정보 가져오기 시작
    
    # DB에서 정보 가져오기 끝
    s = WS.Storage(9, 5)
    while True:
        # 무한 루프 창고 관리
        
        pass
    # DB에 정보 저장 시작
    # DB에 정보 저장 끝

if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 80, debug = False)
    