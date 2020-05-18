from flask import Flask, render_template, request, session, redirect, url_for, flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "HELLO"
app.permanent_session_lifetime = timedelta(minutes=2)

@app.route("/")
def home():
	return render_template("index.html")

	

@app.route("/login/", methods=["GET","POST"])
def login():
	if request.method == "POST":
		flash("Logged in successfully!!","info")
		session.permanent = True
		usr = request.form["name"]
		session["user"] = usr
		return redirect(url_for("user"))
	else:
		if "user" in session:
			usr=session["user"]
			flash(f"You are already logged in...{usr}","info")
			return redirect(url_for("user"))
		return render_template("login.html")


@app.route("/user/")
def user():
	if "user" in session:
		usr = session["user"]
		return render_template("user.html",content=usr)
	else:
		return redirect(url_for("login"))


@app.route("/logout")
def logout():
	if "user" in session:
		flash("Logged out successfully!!","info")
		session.pop("user",None)
	return redirect(url_for("login"))





if __name__ == "__main__":
	app.run(debug=True)