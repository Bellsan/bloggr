import os
from flask import current_app as app

def login():
    return app.config['SECRET_KEY']