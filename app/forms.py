from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length

class AddIPv6Form(FlaskForm):
    address = StringField('IPv6 Address', validators=[DataRequired(), Length(min=3, max=39)])
    description = TextAreaField('Description', validators=[Length(max=100)])
    submit = SubmitField('Add IPv6 Address')