from flask import Blueprint, request, redirect, url_for, flash, render_template
from flask_login import login_user, logout_user, login_required
from services.auth_service import AuthService

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = AuthService.login(username, password)
        if user:
            login_user(user)
            return redirect(url_for("admin.dashboard"))
        else:
            flash("Username atau password salah.", "danger")

    return render_template("login.html")  # Asumsi Anda memiliki file template ini


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))


@auth_bp.route("/forgot", methods=["GET", "POST"])
def forgot_password():
    # Stub untuk fitur lupa password
    return "Halaman Lupa Password"
