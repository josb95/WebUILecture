from flask import Flask, jsonify

app = Flask( __name__ )

@app.route('/json_test')
def hello_json():
    data = {'name':'Hong', 'family' : 'Gildong'}
    return jsonify(data)

@app.route('/server_info')
def server_json():
    data = {'server_name': '0.0.0.0', 'server_port': '8080' }
    return jsonify(data)

host_addr = "0.0.0.0" # 모든 아이피 접속 허용
port_num = "8080"

if __name__ == "__main__":
    app.run( host = host_addr, port = port_num)
