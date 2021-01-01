from flask import Flask, render_template, url_for, redirect
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/home")
def home():
    return redirect(url_for('login'))

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/hello")
def hello():
    return 'hello mate.'

@app.route('/add')
def test():
    return 'Endpoint is changed now.'

@app.route('/multiply/<int:first>/<int:second>')
def multiply(first, second):
    return f'The multiply of request parameters are {first*second}.'
