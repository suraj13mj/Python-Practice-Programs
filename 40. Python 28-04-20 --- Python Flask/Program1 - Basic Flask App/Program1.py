from flask import Flask, redirect, url_for

app = Flask(__name__)          	#Instance of Flask Web Application

@app.route("/")
def home():						
	return "Hello World <h1>PYTHON</h1> <h2>Flask</h2>"


@app.route("/<name>/")
def user(name):
	return f"Hello {name}!"



@app.route("/admin/")
def admin():
	return redirect(url_for("user",name="Admin!"))



if __name__ == "__main__":
	app.run()