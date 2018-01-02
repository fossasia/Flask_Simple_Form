from flask import Flask, render_template, request
app=Flask(__name__)
@app.route('/form', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
       return render_template('Form.html')
    elif request.method == 'POST':
        return render_template('Result.html', name = request.form['username'])