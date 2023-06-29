from flask import Flask, render_template, session, redirect
app = Flask(__name__)
app.secret_key = 'Chrees Key'

@app.route('/')
def counter():
    if "num" not in session:
        session ['num'] = 0
    else: 
        session ['num'] +=1
    return render_template('index.html')

@app.route('/plus2')
def increment_2():
    session ['num'] +=1
    return redirect('/')

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)