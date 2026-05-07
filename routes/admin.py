from flask import Blueprint, request, redirect, url_for, render_template, flash
from flask_login import login_required
from services.menu_service import MenuService
from services.order_service import OrderService
from services.analytics_service import AnalyticsService

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


@admin_bp.route("/dashboard")
@login_required
def dashboard():
    summary = AnalyticsService.get_dashboard_summary()
    active_orders = OrderService.get_active()
    return render_template(
        "admin/dashboard.html", summary=summary, orders=active_orders
    )


@admin_bp.route("/menu")
@login_required
def menu_management():
    menus = MenuService.get_all(active_only=False)
    return render_template("admin/menu_list.html", menus=menus)


@admin_bp.route("/menu/<int:id>/toggle", methods=["POST"])
@login_required
def toggle_menu(id):
    MenuService.toggle_active(id)
    flash("Status menu berhasil diubah.", "success")
    return redirect(url_for("admin.menu_management"))


@admin_bp.route("/orders")
@login_required
def order_list():
    recent_orders = OrderService.get_recent(limit=20)
    return render_template("admin/orders.html", orders=recent_orders)


@admin_bp.route("/orders/<int:id>/process", methods=["POST"])
@login_required
def process_order(id):
    OrderService.update_status(id, "memasak")
    return redirect(url_for("admin.dashboard"))


@admin_bp.route("/orders/<int:id>/complete", methods=["POST"])
@login_required
def complete_order(id):
    OrderService.update_status(id, "selesai")
    return redirect(url_for("admin.dashboard"))
