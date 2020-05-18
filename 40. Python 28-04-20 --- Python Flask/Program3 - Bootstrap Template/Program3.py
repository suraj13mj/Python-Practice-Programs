from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html",content="Namaste")

@app.route("/1")
def bootstrapHome():
	return render_template("index1.html",content="Hola")	




if __name__ == "__main__":
	app.run(debug=True)