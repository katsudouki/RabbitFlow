import os
import importlib
from flask import Flask, redirect, url_for, session, request
from extensions import db, csrf, login_manager
from models import user
from flask_babel import Babel, _
from models.user import create_admin

app = Flask(__name__)
app.config.from_pyfile("config.py")
db.init_app(app)
csrf.init_app(app)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'pt']
babel = Babel(app)


def get_locale():
    if 'lang' in session:
        return session['lang']
    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])


babel.init_app(app, locale_selector=get_locale)

login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return user.User.query.get(int(user_id))


@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for("home"))


models_dir = os.path.join(os.path.dirname(__file__), "models")
for filename in os.listdir(models_dir):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = f"models.{filename[:-3]}"
        importlib.import_module(module_name)

routes_dir = os.path.join(os.path.dirname(__file__), "routes")
for filename in os.listdir(routes_dir):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = f"routes.{filename[:-3]}"
        module = importlib.import_module(module_name)
        if hasattr(module, "bp"):
            app.register_blueprint(module.bp)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        create_admin()

app.run(debug=True, ssl_context=('certs/127.0.0.1.pem', 'certs/127.0.0.1-key.pem'))