from flask import Flask, render_template, request, redirect, url_for,flash, g
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from models import db, Alumnos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

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
	csrf.init_app(app)
	db.init_app(app)
	with app.app_context():	
		db.create_all()
	app.run(debug=True)