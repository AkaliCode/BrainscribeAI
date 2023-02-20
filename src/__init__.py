import os
from flask import Flask, redirect
from src.auth import auth
from src.database.user import db,Bookmark
from flask_sqlalchemy import SQLAlchemy
from src.database.connector import connect_with_connector
from flask_jwt_extended import JWTManager,jwt_required,get_jwt_identity

def create_app(test_config = None):
    
    app = Flask(__name__,instance_relative_config=True)
    
    if test_config is None:
        app.config.from_mapping(
            SECRET_KEY = os.environ.get('SECRET_KEY'),
            SQLALCHEMY_DATABASE_URI= os.environ.get('SQLALCHEMY_DATABASE_URI'),
            SQLALCHEMY_TRACK_MODIFICATIONS=False,
            JWT_SECRET_KEY=os.environ.get('JWT_SECRET_KEY'))
        
    else:
        app.config.from_mapping(test_config)
    
    db.app = app
    db.init_app(app)
    
    JWTManager(app)
    
    app.register_blueprint(auth)
    
    @app.get('/<short_url>')
    def redirect_to(short_url):
        bookmark = Bookmark.query.filter_by(short_url=short_url).first_or_404()
        
        bookmark.visits +=1
        
        db.session.commit()
        
        return redirect(bookmark.url)
               

    @app.errorhandler(404)
    def error404(e):
        return {'error':'404 not found'},40
    @app.errorhandler(500)
    def error500(e):
        return {'error':'Something went wrong'},500

    return app

