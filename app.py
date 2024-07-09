from flask import Flask, render_template, request, jsonify, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length
from app.rutas import init_app


app = Flask(__name__)
app.config.from_pyfile('config.py')
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

init_app(app)


app.config['TEMPLATES_AUTO_RELOAD'] = True  # Recargar automáticamente las plantillas en modo de desarrollo
app.template_folder = 'templates'


app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_RECORD_QUERIES"] = True



class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)


class IPv6Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(39), unique=True, nullable=False)
    description = db.Column(db.String(100))

class AddIPv6Form(FlaskForm):
    address = StringField('IPv6 Address', validators=[DataRequired(), Length(min=3, max=39)])
    description = TextAreaField('Description', validators=[Length(max=100)])
    submit = SubmitField('Add IPv6 Address')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
