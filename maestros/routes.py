from flask import render_template, request, redirect, url_for
from . import maestros
from models import db, Maestros
from forms import MaestroForm

@maestros.route("/maestros", methods=['GET', 'POST'])
def lista():
    create_form = MaestroForm(request.form)
    maestros_list = Maestros.query.all()

    return render_template(
        "maestros/lista.html",
        form=create_form,
        maestros=maestros_list
    )

@maestros.route("/maestros/crear", methods=['GET', 'POST'])
def crear():
    create_form = MaestroForm(request.form)

    if request.method == 'POST':
        maestro = Maestros(
            nombre=create_form.nombre.data,
            apellidos=create_form.apellidos.data,
            especialidad=create_form.especialidad.data,
            email=create_form.email.data,
        )

        db.session.add(maestro)
        db.session.commit()

        return redirect(url_for('maestros.lista'))

    return render_template(
        "maestros/crear.html",
        form=create_form
    )


@maestros.route("/maestros/detalles", methods=['GET'])
def detalles():
    id = request.args.get('id')

    maestro = db.session.query(Maestros).filter(Maestros.matricula == id).first()

    nombre = maestro.nombre
    apellidos = maestro.apellidos
    especialidad = maestro.especialidad
    correo = maestro.email

    return render_template(
        "maestros/detalles.html",
        maestro=maestro,
        nombre=nombre,
        apellidos=apellidos,
        especialidad=especialidad,
        correo=correo
    )


@maestros.route("/maestros/modificar", methods=['GET', 'POST'])
def modificar():
    create_form = MaestroForm(request.form)
    id = request.args.get('id')

    if request.method == 'GET':
        maestro = db.session.query(Maestros).filter(Maestros.matricula == id).first()

        create_form.matricula.data = maestro.matricula
        create_form.nombre.data = maestro.nombre
        create_form.apellidos.data = maestro.apellidos
        create_form.especialidad.data = maestro.especialidad
        create_form.email.data = maestro.email

    if request.method == 'POST':
        maestro = db.session.query(Maestros).filter(Maestros.matricula == id).first()

        maestro.nombre = create_form.nombre.data
        maestro.apellidos = create_form.apellidos.data
        maestro.especialidad = create_form.especialidad.data
        maestro.email = create_form.email.data

        db.session.add(maestro)
        db.session.commit()

        return redirect(url_for('maestros.lista'))

    return render_template(
        "maestros/modificar.html",
        form=create_form
    )


@maestros.route("/maestros/eliminar", methods=['GET', 'POST'])
def eliminar():
    create_form = MaestroForm(request.form)
    id = request.args.get('id')

    if request.method == 'GET':
        maestro = db.session.query(Maestros).filter(Maestros.matricula == id).first()

        create_form.matricula.data = maestro.matricula
        create_form.nombre.data = maestro.nombre
        create_form.apellidos.data = maestro.apellidos
        create_form.especialidad.data = maestro.especialidad
        create_form.email.data = maestro.email

    if request.method == 'POST':
        maestro = db.session.query(Maestros).filter(Maestros.matricula == id).first()

        db.session.delete(maestro)
        db.session.commit()

        return redirect(url_for('maestros.lista'))

    return render_template(
        "maestros/eliminar.html",
        form=create_form
    )

@maestros.route('/perfil/<nombre>')
def perfil(nombre):
    return f"Perfil de {nombre}"