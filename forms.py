from wtforms import Form
from wtforms import StringField, IntegerField, PasswordField
from wtforms import EmailField
from wtforms import validators

class UserForm(Form):
    id = IntegerField('id')
    nombre = StringField('Nombre',
        [
            validators.DataRequired("Este campo es requerido"),
            validators.length(min=4,max=10,message="Ingresa un valor valido")
        ]
    )
    apellidos = StringField('Apellidos',
        [
            validators.DataRequired("Este campo es requerido")
        ]
    )
    telefono = StringField('Telefono',
        [
            validators.DataRequired("Este campo es requerido")
        ]
    )
    email = EmailField('Correo',
        [
            validators.Email("Ingrese un correo valido")
        ]
    )


class MaestroForm(Form):
    matricula = IntegerField('Matrícula', [
        validators.DataRequired("La matrícula es requerida")
    ])

    nombre = StringField('Nombre', [
        validators.DataRequired("Este campo es requerido"),
    ])

    apellidos = StringField('Apellidos', [
        validators.DataRequired("Este campo es requerido"),
    ])

    especialidad = StringField('Especialidad', [
        validators.DataRequired("Este campo es requerido"),
    ])

    email = EmailField('Correo', [
        validators.Email("Ingrese un correo valido")
    ])