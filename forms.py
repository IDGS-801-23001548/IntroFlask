from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField
from wtforms import validators

class UserForm(FlaskForm):
    matricula = IntegerField("Matricula", [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=100, max=1000, message="Ingrese valor valido")
    ])

    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido"),
        validators.Length(min=3, max=10, message="Ingrese un nombre valido")
    ])

    apaterno = StringField("Apaterno", [
        validators.DataRequired(message="El campo es requerido")
    ])

    amaterno = StringField("Amaterno", [
        validators.DataRequired(message="El campo es requerido")
    ])

    correo = EmailField("Correo", [
        validators.Email(message="Ingresa un correo valido")
    ])
