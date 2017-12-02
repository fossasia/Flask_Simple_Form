from flask import Flask, request, redirect, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/greeting', methods = ['POST'])
def result():
    name = request.form['name']
    return render_template('greeting.html', name = name)


if __name__ == '__main__':
    app.run(debug=True)
