from flask import Flask, render_template,request, session, redirect
app = Flask(__name__)
app.secret_key = 'Chrees Key'

@app.route('/')
def dojo_form():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit_form():
    print("Info received")
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['flanguage'] = request.form['flanguage']
    session['comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def show_result():
    return render_template('result.html')

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)