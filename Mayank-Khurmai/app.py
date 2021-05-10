from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'some_secret_key'


@app.route("/", methods=["GET", "POST"])
def homepage():
    if request.method == "POST":
        flash("Welcome {}! Have a nice day!".format(request.form["username"]))
        lst = [["Username", request.form["username"]], ["Date of birth", request.form["dob"]],["Email", request.form["email"]], ["Gender", request.form["gender"]]]
        return render_template("profile.html", lst=lst)
    else:
        return render_template("homepage.html")

#run app
if __name__ == "__main__":
    app.debug = True
    app.run()
