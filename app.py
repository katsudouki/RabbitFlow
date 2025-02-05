import os
from flask import Flask, redirect, url_for, session, request
from flask_babel import Babel
from extensions import db, csrf, login_manager

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


import models
import routes
for bp in routes.blueprints:
    app.register_blueprint(bp)

@login_manager.user_loader
def load_user(user_id):
    from models.user import User
    return User.query.get(int(user_id))

@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for("index.home"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, ssl_context=('certs/127.0.0.1.pem', 'certs/127.0.0.1-key.pem'))
