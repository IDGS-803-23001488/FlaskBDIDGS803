from flask import Flask, render_template

app = Flask(__name__)

@app.errorhandler(404)
def page_noy_found(e):
    return render_template("404.html")

@app.route("/")
@app.route("/index")
def index():
	return render_template("index.html")

@app.route("/alumnos")
def alumnos():
	return render_template("alumnos.html")


if __name__ == '__main__':
	app.run(debug=True)
