from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/',methods=['POST'])
def name():
	name = request.form['name']
	if name != "":
		return render_template('name.html',name=name)
	else:
		return render_template('index.html', error="No name")

