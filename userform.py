from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, RadioField
from wtforms import validators
from wtforms.validators import ValidationError

class boletos(FlaskForm):
    nombre = StringField("Nombre", [
        validators.DataRequired(message="El campo es requerido."),
        validators.Length(min=3, max=10, message="Ingrese un nombre válido")
    ])

    compradores = IntegerField("Compradores", [
        validators.DataRequired(message="El campo es requerido."),
        validators.NumberRange(min=1, max=100, message="Ingrese un valor válido")
    ])

    tarjeta = RadioField(
        "Tarjeta",
        choices=[
            ('1', 'Sí'),
            ('0', 'No')
        ],
        validators=[validators.DataRequired(message="Seleccione una opción")]
    )

    boletos = IntegerField("Boletos", [
        validators.DataRequired(message="El campo es requerido"),
        validators.NumberRange(min=1, message="Ingrese un valor válido")
    ])

    def validate_boletos(self, field):
        if self.compradores.data is None:
            return

        max_boletos = self.compradores.data * 7

        if field.data > max_boletos:
            raise ValidationError(
                f"Máximo {max_boletos} boletos para {self.compradores.data} comprador(es)"
            )
