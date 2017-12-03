from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

@app.route('/index', methods=["GET", "POST"])
def index():
    form = LoginForm()
    if form.validate_on_submit():

        flash('Hi %s! Have a nice day!' % (form.openid.data))
        return redirect('/index')
    
    return render_template('index.html', title='Fossasia', form=form)