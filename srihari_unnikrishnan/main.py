from flask import Flask, render_template,request


app = Flask(__name__)
app.secret_key = 'development key'

@app.route('/')
def contact():
    return render_template('index.html')

@app.route("/result", methods = ['POST'])
def result():
    name = request.form["name"]
    return render_template('res.html', name = name)

    if __name__ == '__main__':
            app.run(debug = True)