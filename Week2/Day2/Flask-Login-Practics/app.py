from flask import Flask, url_for, render_template, request, redirect

app = Flask( __name__ )

@app.route( "/" )
def index():
    return render_template( "index.html" )

@app.route( "/register", methods = [ 'GET', 'POST' ] )
def register():
    if request.method == 'GET':
        return render_template( "register.html" )
    else:
        return redirect( url_for( "login" ) )
        

@app.route( "/login", methods = [ 'GET', 'POST' ] )
def login():
    if request.method == 'GET':
    	return render_template( 'login.html' )
    else:
        return redirect( url_for( "main" ) )

@app.route( "/main" )
def main():
    return render_template( "HTMLPageLayout.html" )

if __name__ == "__main__":
    app.run( host = "0.0.0.0", port = 80, debug = True )
