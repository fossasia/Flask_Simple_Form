from flask import *
app = Flask(__name__)

@app.route('/')
def index():
    word=request.args.get('name', '')
    word = word.strip()
    if len(word) > 0:
        return render_template('hello.html', name=word)
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
