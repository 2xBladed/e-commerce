from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        senha = request.form.get('senha')

        user = User.query.filter_by(username=username).first()
        print(user.senha)
        if user:
            if user.senha == senha:
                flash('entrou com sucesso!', category='Sucesso')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('senha incorreta.', category='Erro')
        else:
            flash('nome de usuário não existe.', category='Erro')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        username = request.form.get('username')
        senha1 = request.form.get('senha1')
        senha2 = request.form.get('senha2')
        
        user = User.query.filter_by(username=username).first()
        if user:
            flash('esse nome de usuário já existe.', category='Erro')
        else:
            if senha1 != senha2:
                flash('as senhas não coincidem.', category='Erro')
            else:
                # TODO criptografar antes
                new_user = User(username=username, senha=senha1)
                db.session.add(new_user)
                db.session.commit()
                login_user(user, remember=True)

                flash('conta criada com sucesso.', category='Sucesso')

                return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)

@auth.route('/carrinho')
@login_required
def carrinho():
    return render_template("carrinho.html", user=current_user)