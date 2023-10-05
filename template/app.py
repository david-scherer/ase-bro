from flask import Flask

# https://s3.us-east-2.amazonaws.com/prettyprinted/flask_cheatsheet.pdf

app = Flask(__name__)

@app.route('/hello')
def hello():
    return 'Hello, World!'

@app.route('/hello2/<string:name>') 
def hello(name):
    return 'Hello ' + name + '!' # returns hello Anthony!

# @app.route('/test') #default. only allows GET requests
# @app.route('/test', methods=['GET', 'POST']) #allows only GET and POST.
# @app.route('/test', methods=['PUT']) #allows only PUT

if __name__ == '__main__':
    app.run(debug=True)

