from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html",content="Namaskar")

@app.route("/<name>")
def user(name):
	return render_template("index.html",content=name)

@app.route("/test")
def test():
	return render_template("test.html")

@app.route("/test1")
def test1():
	lst=["Suraj","Prasad","Nikhil","Rohan","Vijay","Nitin"]
	return render_template("test1.html",list=lst)






if __name__ == "__main__":
	app.run()