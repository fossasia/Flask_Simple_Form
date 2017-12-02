from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/result', methods = ['POST'])
def result():
    name = request.form['name']
    return render_template('result.html', name = name)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')