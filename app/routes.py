from flask import render_template, request, jsonify, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from app import app, db, bcrypt, login_manager
from app.models import User, IPv6Address
from app.forms import AddIPv6Form
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length



@app.route('/')
def index():
    return render_template('index.html', ipv6_addresses=IPv6Address.query.all())

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/dashboard')
# ... (resto del código)

@app.route('/search', methods=['GET'])
# ... (resto del código)

@app.route('/add', methods=['GET', 'POST'])
def add_ipv6():
    form = AddIPv6Form()
    if form.validate_on_submit():
        new_ipv6 = IPv6Address(address=form.address.data, description=form.description.data)
        db.session.add(new_ipv6)
        db.session.commit()
        flash('IPv6 Address added successfully', 'success')
        return redirect(url_for('index'))
    return render_template('add_ipv6.html', form=form)

