from flask import Flask,render_template,request,redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/',methods=['POST'])
def name():
	user_name = request.form['name']
	if user_name != "":
		return render_template('name.html',name=user_name)
	else:
		return redirect(url_for('error'))


@app.route('/error',methods=['POST','GET'])
def error():        
    if request.method == "POST":
        return redirect('/')
    else:
    	return render_template('error.html')

if __name__ == '__main__':
	app.run(debug=True)
