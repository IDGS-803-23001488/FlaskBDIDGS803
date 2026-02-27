from flask import Flask, render_template, request, redirect, url_for
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate
from models import db, Alumnos
from config import DevelopmentConfig
import forms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()
db.init_app(app)
migrate = Migrate(app, db)

@app.errorhandler(404)
def page_noy_found(e):
    return render_template("404.html")

@app.route("/", methods=['POST','GET'])
@app.route("/index")
def index():
	create_form = forms.UserForm(request.form)
	alumnos = Alumnos.query.all()
	return render_template("index.html",form=create_form, alumnos=alumnos)

@app.route("/Alumnos",methods=['POST','GET'])
def alumnos():
	create_form = forms.UserForm(request.form)
	if request.method == 'POST':
		alumno = Alumnos(
			nombre=create_form.nombre.data,
			apellidos=create_form.apellidos.data,
			telefono=create_form.telefono.data,
			email=create_form.email.data,
		)
		db.session.add(alumno)
		db.session.commit()
		return redirect(url_for('index'))
	return render_template("alumnos.html", form=create_form)

@app.route("/detalles",methods=['POST','GET'])
def detalles():
	create_form = forms.UserForm(request.form)
	if request.method == 'GET':
		id = request.args.get('id')
		alumn = db.session.query(Alumnos).filter(Alumnos.id == id).first()
		nombre = alumn.nombre
		apellidos = alumn.apellidos
		telefono = alumn.telefono
		correo = alumn.email
	return render_template(
     "detalles.html",
     	alumn= alumn,
		nombre= nombre,
		apellidos= apellidos,
		telefono= telefono,
		correo= correo,
	)

@app.route("/modificar",methods=['POST','GET'])
def modificar():
	create_form = forms.UserForm(request.form)
	id = request.args.get('id')
	if request.method == 'GET':
		alumn = db.session.query(Alumnos).filter(Alumnos.id == id).first()
		create_form.id.data = alumn.id
		create_form.nombre.data = alumn.nombre
		create_form.apellidos.data = alumn.apellidos
		create_form.telefono.data = alumn.telefono
		create_form.email.data = alumn.email
	
	if request.method == 'POST':
		alumn = db.session.query(Alumnos).filter(Alumnos.id == id).first()
		alumn.nombre = create_form.nombre.data
		alumn.apellidos = create_form.apellidos.data
		alumn.telefono = create_form.telefono.data
		alumn.email = create_form.email.data
		db.session.add(alumn)
		db.session.commit()
		return redirect(url_for('index'))
	
	return render_template(
		"modificar.html",form = create_form
	)

@app.route("/eliminar",methods=['POST','GET'])
def eliminar():
	create_form = forms.UserForm(request.form)
	id = request.args.get('id')
	if request.method == 'GET':
		alumn = db.session.query(Alumnos).filter(Alumnos.id == id).first()
		create_form.id.data = alumn.id
		create_form.nombre.data = alumn.nombre
		create_form.apellidos.data = alumn.apellidos
		create_form.telefono.data = alumn.telefono
		create_form.email.data = alumn.email
	
	if request.method == 'POST':
		alumn = db.session.query(Alumnos).filter(Alumnos.id == id).first()
		db.session.delete(alumn)
		db.session.commit()
		return redirect(url_for('index'))
	
	return render_template(
		"eliminar.html",form = create_form
	)

if __name__ == '__main__':
	csrf.init_app(app)
	with app.app_context():	
		db.create_all()
	app.run(debug=True)