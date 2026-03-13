from flask import render_template, request, redirect, url_for
from . import alumnos
from models import db, Alumnos
from forms import UserForm

@alumnos.route("/alumnos", methods=['GET', 'POST'])
def index():
	create_form = UserForm(request.form)
	alumnos = Alumnos.query.all()
	return render_template("alumnos/lista.html",form=create_form, alumnos=alumnos)

@alumnos.route("/alumnos/crear",methods=['POST','GET'])
def craer():
	create_form = UserForm(request.form)
	if request.method == 'POST':
		alumno = Alumnos(
			nombre=create_form.nombre.data,
			apellidos=create_form.apellidos.data,
			telefono=create_form.telefono.data,
			email=create_form.email.data,
		)
		db.session.add(alumno)
		db.session.commit()
		return redirect(url_for('alumnos.index'))
	return render_template("alumnos/alumnos.html", form=create_form)

@alumnos.route("/alumnos/detalles",methods=['POST','GET'])
def detalles():
	id = request.args.get('id')
	alumn = db.session.query(Alumnos).filter(Alumnos.id == id).first()
	return render_template(
        "alumnos/detalles.html",
        alumn=alumn
    )

@alumnos.route("/alumnos/modificar",methods=['POST','GET'])
def modificar():
	create_form = UserForm(request.form)
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
		return redirect(url_for('alumnos.index'))
	
	return render_template(
		"alumnos/modificar.html",form = create_form
	)

@alumnos.route("/alumnos/eliminar",methods=['POST','GET'])
def eliminar():
	create_form = UserForm(request.form)
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
		return redirect(url_for('alumnos.index'))
	
	return render_template(
		"alumnos/eliminar.html",form = create_form
	)
