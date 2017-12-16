from flask import Flask, request, redirect, render_template

app = Flask(__name__)

# when directly root called, run the index function 
@app.route("/")
def index():
    # open the index.html page
    return render_template('index.html')

# when the result url hit with a post request, show result function
@app.route('/showGreeting', methods = ['POST'])
def result():
	# get the element with name 'name'
    userName = request.form['username']
    # pass the name to the result.html template
    return render_template('showGreeting.html', name = userName)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')