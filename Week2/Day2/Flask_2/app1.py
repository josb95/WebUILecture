from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def template_test():
    return render_template('index.html',                # 렌더링 html 파일명
     title = 'Flask Template Test',                     # title 텍스트 바인딩1
      my_str = 'Hello Flask!',                          # my_str 텍스트 바인딩2
       my_list = [x + 1 for x in range(30)])            # 30개 리스트 선언(1~30)


# host_addr = "0.0.0.0"
# port_num = "8080"

if __name__ == "__main__":
    app.run( host = '0.0.0.0', port = 8080, debug = True)
