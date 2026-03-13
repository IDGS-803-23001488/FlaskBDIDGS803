from flask import Flask, render_template, request, redirect, url_for, Blueprint
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from models import db
from config import DevelopmentConfig
from maestros.routes import maestros
from alumnos.routes import alumnos
from cursos.routes import cursos

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
app.register_blueprint(maestros)
app.register_blueprint(alumnos)
app.register_blueprint(cursos)
csrf = CSRFProtect()
db.init_app(app)
migrate = Migrate(app, db)

@app.errorhandler(404)
def page_noy_found(e):
    return render_template("404.html")

@app.route("/", methods=['POST','GET'])
@app.route("/index")
def index():
	return render_template("index.html")

if __name__ == '__main__':
	csrf.init_app(app)
	with app.app_context():	
		db.create_all()
	app.run(debug=True)