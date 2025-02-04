from flask import (
    Blueprint,
    request,
    redirect,
    url_for,
    make_response,
    jsonify,
    render_template,
)
from flask_login import login_user, current_user, login_required, LoginManager
from werkzeug.security import check_password_hash
from models.user import User
from app import db, csrf

bp = Blueprint("dashboard", __name__)

@bp.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")
