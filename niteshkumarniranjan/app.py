from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

DEBUG = True
HOST = '0.0.0.0'
PORT = 8080

app = Flask(__name__)
app.secret_key = "sdsafsfdsfbdsj!jsdkfl"

class simple_form(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])


@app.route("/", methods=('GET', 'POST'))
def index():
    form = simple_form()
    return render_template("index.html", form=form)


@app.route("/hello/", methods=('GET', 'POST'))
def hello():
    name = request.form['name']
    return render_template("hello.html", name=name)
    
if __name__ == '__main__':
    app.run(debug=DEBUG, host=HOST, port=PORT)