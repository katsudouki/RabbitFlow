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
from models.transactions import Transaction
from models.categories import Category
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
    income =Transaction.query.filter_by(type="income").all()
    categories = {c.id: c for c in Category.query.all()}
    return render_template("income.html", incomes=income, categories=categories)


@bp.route("/expense")
@login_required
def expense():
    expense = Transaction.query.filter_by(type="expense").all()
    categories = {c.id: c for c in Category.query.all()}
    return render_template("expense.html", expenses=expense, categories=categories)


@bp.route("/profile")
@login_required
def profile():
    return render_template("profile.html")


@bp.route("/settings")
@login_required
def settings():
    return render_template("settings.html")
