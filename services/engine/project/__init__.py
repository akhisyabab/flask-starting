import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_debugtoolbar import DebugToolbarExtension
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_sqlalchemy_session import flask_scoped_session

import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

# instantiate the extensions
db = SQLAlchemy()
toolbar = DebugToolbarExtension()
bcrypt = Bcrypt()
migrate = Migrate()


def create_app(script_info=None):
    from project.models import models
    from project.applications.views import app_blueprint

    if os.environ.get('FLASK_ENV') == 'production':
        sentry_sdk.init(
            dsn="",
            integrations=[FlaskIntegration()]
        )

    # instantiate the app
    app = Flask(__name__, static_url_path='')

    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # set up extensions
    db.init_app(app)
    toolbar.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    # Setting up flask login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = "appblueprint.login"

    @login_manager.user_loader
    def load_user(user_id):
        return models.User.query.filter(models.User.id == int(user_id)).first()

    # register the blueprints
    app.register_blueprint(app_blueprint)

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
