from flask import Flask, request, redirect, render_template
from os import urandom

app = Flask(__name__)
app.config["SECRET_KEY"] = str(urandom(24));

@app.route('/')
def index():
	return render_template("index.html")

@app.route('/greeting', methods = ["POST"])
def greeting():
	POST_name = request.form["name"]
	return render_template("greeting.html", name = POST_name)

if __name__ == '__main__':
	app.run(debug = True)
