# Import Flask to allow us to create our app
from flask import Flask, render_template
# Create a new instance of the Flask class called "app"
app = Flask(__name__)


# The "@" decorator associates this route with the function immediately following
@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/success')
def success():
    return "success"


# for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
@app.route('/hello/<name>')
def hello(name):
    print(name)
    return "Hello, " + name


# for a route '/users/____/____', two parameters in the url get passed as username and id
@app.route('/users/<username>/<id>')
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id


if __name__ == "__main__":   # Ensure this file is being run directly and not from a different module
    # Run the app in debug mode.
    app.run(debug=True, host="localhost", port=8000)
