from flask import flask

DEBUG = True

app = Flask(__name__)

@app.route("/")
def hello_world():
	return "HEllo"


if __name__ == "__main__":
	app.run(debug=DEBUG)