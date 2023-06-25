from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/dojo')
def dojo():
    return 'Dojo'
@app.route('/say/flask')
def hello_flask():
    return 'Hi Flask!'
@app.route('/say/michael')
def hello_michael():
    return "Hi Michael!"
@app.route('/say/john')
def hello_john():
    return "Hi John!"
@app.route('/repeat/<int:num>/hello')
def repeat_hello(num):
    repeated = ''
    for i in range (0,num):
        repeated += '<p>hello<p>'
    return repeated
@app.route('/repeat/<int:num>/bye')
def repeat_bye(num):
    repeated = ''
    for i in range (0,num):
        repeated += '<p>bye<p>'
    return repeated
@app.route('/repeat/<int:num>/dogs')
def repeat_dogs(num):
    repeated = ''
    for i in range (0,num):
        repeated += '<p>dog<p>'
    return repeated
if __name__=="__main__":
    app.run(debug=True, host="localhost", port=8000)