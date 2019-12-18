from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config



db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    # 启用 cors,负责前端会报错
    CORS(app)
    db.init_app(app)
    migrate.init_app(app,db)
    # 蓝图注册  blueprint
    from app.api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    app.config['DEBUG'] = True
    return app


from app import models
