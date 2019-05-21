from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():

    headline = 'hello world'
    return render_template("index.html", headline=headline)
'''
@app.route("/wario")
def dallas():
    return "hello world!"
# below route,generalised for all sets of routes,takes a string which will be the name
@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"Hello, {name}!"

'''