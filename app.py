from flask import Flask,render_template,redirect,request,url_for,session
from sites import siteslist
from databaseinitialise import connect

sitenames=siteslist()

app=Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html',sitenames=sitenames)

@app.route('/logout')
def logout():
	session.clear()
	return redirect(url_for('home'))

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/login',methods=['POST','GET'])
def login():
	if request.method=="POST":
		entered_email=request.form['mailid']
		entered_password=request.form['password']
		#if entered_email=="admin" and entered_password=="admin":
		#	return redirect(url_for('userhomepage'))
		#elif entered_password=='' or entered_email=='':
		#	return redirect(url_for('login'))
		db,dbc=connect()
		#In place of 'USERS' write your own Table Name
		#In place of 'EMAIL' write your own email field Name
		getemail=dbc.execute("select * from USERS where EMAIL='%s'"%(entered_email))
		getpasswd=dbc.fetchone()[5]
		if getpasswd==entered_password:
			session['logged_in']=True
			session['username']=getemail
			return redirect(url_for('userhomepage'))
		else:
			return redirect(url_for('login'))
		db.commit()
		dbc.close()
		db.close()
	return render_template('login.html')

@app.route('/signup',methods=['GET','POST'])
def signup():
	if request.method=="POST":
		db,dbc=connect()
		fname=request.form['fname']
		lname=request.form['lname']
		mail=request.form['mail']
		pwd=request.form['pwd']
		#Write your own fields name in place of 'FIRSTNAME, LASTNAME, EMAIL, PASSWORD'
		dbc.execute("insert into USERS(FIRSTNAME, LASTNAME, EMAIL, PASSWORD) values(%s, %s, %s, %s)",(fname, lname, mail, pwd))
		db.commit()
		db.close()
		dbc.close()
	return redirect(url_for('login'))
	return render_template('signup.html')

@app.route('/userhomepage')
def userhomepage():
	return render_template('userhomepage.html')


if __name__=='__main__':
	app.secret_key = 'super secret key '
	app.run(debug=True)  
