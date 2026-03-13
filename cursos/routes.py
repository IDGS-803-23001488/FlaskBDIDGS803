from flask import render_template, request, redirect, url_for
from . import cursos
from models import db, Curso, Maestros, Alumnos
from forms import CursoForm


@cursos.route("/cursos", methods=['GET'])
def lista():

    cursos_list = Curso.query.all()

    return render_template(
        "cursos/lista.html",
        cursos=cursos_list
    )

@cursos.route("/cursos/crear", methods=['GET', 'POST'])
def crear():

    create_form = CursoForm(request.form)

    maestros = Maestros.query.all()
    create_form.maestro_id.choices = [
        (m.matricula, f"{m.nombre} {m.apellidos}") for m in maestros
    ]

    if request.method == 'POST' and create_form.validate():

        curso = Curso(
            nombre=create_form.nombre.data,
            descripcion=create_form.descripcion.data,
            maestro_id=create_form.maestro_id.data
        )

        db.session.add(curso)
        db.session.commit()

        return redirect(url_for('cursos.lista'))

    return render_template(
        "cursos/crear.html",
        form=create_form
    )

@cursos.route("/cursos/detalles", methods=['GET','POST'])
def detalles():

    form = CursoForm(request.form)

    id = request.args.get("id")

    curso = Curso.query.get(id)

    alumnos_disponibles = Alumnos.query.all()

    return render_template(
        "cursos/detalles.html",
        form=form,
        curso=curso,
        alumnos_disponibles=alumnos_disponibles
    )

@cursos.route("/cursos/revisar", methods=['GET','POST'])
def revisar():

    form = CursoForm(request.form)

    id = request.args.get("id")

    curso = Curso.query.get(id)

    if request.method == "POST":

        accion = request.form.get("accion")
        alumno_id = request.form.get("alumno_id")

        alumno = Alumnos.query.get(alumno_id)

        if accion == "agregar":
            if alumno not in curso.alumnos:
                curso.alumnos.append(alumno)

        elif accion == "eliminar":
            if alumno in curso.alumnos:
                curso.alumnos.remove(alumno)

        db.session.commit()

        return redirect(url_for("cursos.revisar", id=id))

    alumnos_disponibles = Alumnos.query.all()

    return render_template(
        "cursos/revisar.html",
        form=form,
        curso=curso,
        alumnos_disponibles=alumnos_disponibles
    )

@cursos.route("/cursos/modificar", methods=['GET', 'POST'])
def modificar():

    create_form = CursoForm(request.form)

    id = request.args.get('id')
    curso = Curso.query.get(id)

    maestros = Maestros.query.all()
    create_form.maestro_id.choices = [
        (m.matricula, f"{m.nombre} {m.apellidos}") for m in maestros
    ]

    if request.method == 'GET':
        create_form.id.data = curso.id
        create_form.nombre.data = curso.nombre
        create_form.descripcion.data = curso.descripcion
        create_form.maestro_id.data = curso.maestro_id

    if request.method == 'POST' and create_form.validate():

        curso.nombre = create_form.nombre.data
        curso.descripcion = create_form.descripcion.data
        curso.maestro_id = create_form.maestro_id.data

        db.session.commit()

        return redirect(url_for('cursos.lista'))

    return render_template(
        "cursos/modificar.html",
        form=create_form
    )

@cursos.route("/cursos/eliminar", methods=['GET', 'POST'])
def eliminar():

    create_form = CursoForm(request.form)
    
    id = request.args.get('id')
    
    maestros = Maestros.query.all()
    create_form.maestro_id.choices = [
        (m.matricula, f"{m.nombre} {m.apellidos}") for m in maestros
    ]
    if request.method == 'GET':
        curso = db.session.query(Curso).filter(Curso.id == id).first()
        create_form.id.data = curso.id
        create_form.nombre.data = curso.nombre
        create_form.descripcion.data = curso.descripcion
        create_form.maestro_id.data = curso.maestro_id

    if request.method == 'POST':

        curso = db.session.query(Curso).filter(Curso.id == id).first()

        db.session.delete(curso)
        db.session.commit()

        return redirect(url_for('cursos.lista'))

    curso = db.session.query(Curso).filter(Curso.id == id).first()

    return render_template(
        "cursos/eliminar.html",
        form=create_form,
        curso=curso
    )

@cursos.route("/cursos/cards", methods=['GET'])
def cards():

    cursos_list = Curso.query.all()

    return render_template(
        "cursos/cards.html",
        cursos=cursos_list
    )