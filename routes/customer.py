from flask import (
    Blueprint,
    request,
    redirect,
    url_for,
    session,
    jsonify,
    render_template,
)
from services.menu_service import MenuService
from services.cart_service import CartService
from services.order_service import OrderService
from services.recommendation_service import RecommendationService
import uuid

customer_bp = Blueprint("customer", __name__)


# Helper untuk memastikan setiap pengunjung punya session ID
def get_session_id():
    if "cart_session_id" not in session:
        session["cart_session_id"] = str(uuid.uuid4())
    return session["cart_session_id"]


@customer_bp.route("/")
def home():
    best_sellers = MenuService.get_best_sellers()
    return render_template("home.html", best_sellers=best_sellers)


@customer_bp.route("/menu")
def menu_list():
    menus = MenuService.get_all(active_only=True)
    return render_template("menu.html", menus=menus)


@customer_bp.route("/cart/add", methods=["POST"])
def add_to_cart():
    menu_id = request.form.get("menu_id")
    quantity = int(request.form.get("quantity", 1))

    CartService.add_item(get_session_id(), menu_id, quantity)
    return redirect(url_for("customer.menu_list"))


@customer_bp.route("/preorder", methods=["GET", "POST"])
def preorder():
    session_id = get_session_id()
    if request.method == "POST":
        customer_data = {
            "name": request.form.get("customer_name"),
            "pickup_schedule": request.form.get("pickup_schedule"),
            "note": request.form.get("note"),
            "order_type": request.form.get("order_type", "pickup"),
        }
        order = OrderService.create_order(session_id, customer_data)
        if order:
            return redirect(url_for("customer.track_status", code=order.order_code))

    summary = CartService.get_summary(session_id)
    recos = RecommendationService.get_recommendations(session_id)
    return render_template("checkout.html", summary=summary, recommendations=recos)


@customer_bp.route("/track/<code>")
def track_status(code):
    order_data = OrderService.track_status(code)
    if not order_data:
        return "Pesanan tidak ditemukan", 404
    return render_template("track.html", order=order_data)
