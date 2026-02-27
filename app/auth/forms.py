from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired



class LoginForm(FlaskForm):
    username = StringField("usuario", validators=[DataRequired()])
    password = PasswordField("contraseña", validators=[DataRequired()])
    submit = SubmitField("ingresar")


class RegisterForm(FlaskForm):
    username = StringField("usuario", validators=[DataRequired()])
    password = PasswordField("contraseña", validators=[DataRequired()])
    submit = SubmitField("ingresar")
    activo = BooleanField("activo")
    rol = StringField("rol")
    nombre = StringField("nombre", validators=[DataRequired()])