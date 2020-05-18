from flask import Flask , render_template, redirect, url_for, request

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")



@app.route("/login/",methods = ["POST","GET"])
def login():
	if request.method == "POST":
		user = request.form["name"]
		return redirect(url_for("main",usr=user))
	else:
		return render_template("login.html")



@app.route("/<usr>")
def main(usr):
	return render_template("main.html",content=usr)




if __name__ == "__main__":
	app.run(debug=True)