from flask import render_template, request, Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html')


@auth.route('/register')
def register():
    return render_template('auth/register.html')