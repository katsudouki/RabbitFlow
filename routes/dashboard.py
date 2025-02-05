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

@bp.route("/dash")
@login_required
def dash():
    return render_template("dash.html")

@bp.route("/transactions")
@login_required
def transactions():
    return render_template("transactions.html")

@bp.route("/income")
@login_required
def income():
    return render_template("income.html")

@bp.route("/expense")
@login_required
def expense():
    return render_template("expense.html")

@bp.route("/profile")
@login_required
def profile():
    return render_template("profile.html")

@bp.route("/settings")
@login_required
def settings():
    return render_template("settings.html")
