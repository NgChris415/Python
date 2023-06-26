from flask import Flask, render_template
app = Flask(__name__)


@app.route('/box')
def display_box1():
    return render_template("Ng_Chris_Playground.html", num=3, color="blue")


@app.route('/box/<int:num>')
def display_box2(num):
    return render_template("Ng_Chris_Playground.html", num=num, color="blue")


@app.route('/box/<int:num>/<string:color>')
def display_box3(num, color):
    return render_template("Ng_Chris_Playground.html", num=num, color=color)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)
