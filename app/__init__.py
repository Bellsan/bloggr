#!/usr/bin/env python3
"""
Documentation

Blog application to learn flask
"""
import os
from flask import Flask, jsonify
from flask_cors import CORS
import app.auth.auth as auth

def create_app(config='instance.config.DevelopmentConfig'):
    app = Flask(__name__)
    
    app.config.from_object(config)
    print(f"Environment: {app.config['ENV']}")
    print(f"Debug: {app.config['DEBUG']}")
    print(f"Secret key: {app.config['SECRET_KEY']}")

    CORS(app)

    # Definition of the routes. Put them into their own file. See also
    # Flask Blueprints: http://flask.pocoo.org/docs/latest/blueprints
    from app.main.routes import main
    from app.auth.routes import auth
    app.register_blueprint(main)
    app.register_blueprint(auth)


    return app
