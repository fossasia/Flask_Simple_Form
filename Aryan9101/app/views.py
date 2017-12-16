from flask import render_template, flash, request, redirect, url_for
from wtforms import Form, StringField, validators
from flask import Flask
from app import app

WTF_CSRF_ENABLED = True #Important Config that prevents CSRF attacks

class GreetingForm(Form):
    """
    Create a Greeting form class.
    Contains the main attributes i.e, String fields to be filled in a form
    """
    username = StringField('Username', [validators.Length(min = 1)]) #validator to make sure data is entered

@app.route('/')
@app.route('/greeting', methods=['POST', 'GET'])
def greeting():
    form = GreetingForm(request.form)
    if request.method == 'POST': 
        if form.validate(): #Check is username is entered
            username = request.form['username']
            flash("Hi %s, Have a nice day" % form.username.data)
        else:
            flash("Please enter a name")
            return redirect(url_for('greeting'))
    return render_template("greetings.htm",
                           title='Greetings',
                           form=form)


    
