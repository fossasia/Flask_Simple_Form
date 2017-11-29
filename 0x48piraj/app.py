from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import sys
import json
import os
import shutil
from os import path


#import urllib #Deprecated in py3
import urllib.request #now, it's good
from bs4 import BeautifulSoup

from scraper import AdvancedSearchScraper
# App config.
#DEBUG = True
path = path.dirname(path.realpath(__file__))
app = Flask(__name__,template_folder=path+'/')
app.config['SECRET_KEY'] = '3d441f27u331c27333d331k2f3333a'
 
class ReusableForm(Form):
    name = TextField("FOSSASIA's Family Member's Name?")
    twitter = TextField("What's your Twitter handle?")
    github = TextField("What's your Github handle?")
 
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
    if len(form.errors) != 0:
       print(form.errors)
    if request.method == 'POST':
        name=request.form['name']
        github=request.form['git']
        twitter=request.form['twitter']
        print(name, " ", twitter, " ", github)
 
        if len(name) != 0:
            flash('Thanks for coming ' + name)
            if len(github) and len(twitter) != 0:
             url = 'http://github.com/' + github
             data = urllib.request.urlopen(url).read() # update with urllib.request.urlopen
             soup = BeautifulSoup(data)
             fullname = soup.find('span', {'class' : 'vcard-fullname'}).string
             username = soup.find('span', {'class' : 'vcard-username'}).string
             twitter_user = AdvancedSearchScraper(twitter, 1)
             tweets = twitter_user.scrape()
             flash("Latest Tweet : "+ json.dumps(tweets[0]["tweet_text"]) + " Retweets : "+json.dumps(tweets[0]["retweets"])+" Likes : "+json.dumps(tweets[0]["favorites"]))
             flash("Github Profile: " +fullname+" (@"+username+")")
        else:
            flash('Error: `Name` in the form field is required.')
 
    return render_template('index.html', form=form)
 
if __name__ == "__main__":
    app.run()