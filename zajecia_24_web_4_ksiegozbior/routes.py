from flask import Blueprint, render_template, request
from biblioteka import app_handler

my_blueprint = Blueprint("my_blueprint", __name__)

@my_blueprint.route("/", methods=["GET", "POST"])
def main_view():
    if request.method == "GET":
        return render_template("ksiegarnia.html", ksiegozbior=app_handler.ksiegozbior, saldo=app_handler.saldo)
    elif request.method == "POST":
        form_type = request.form.get("form_type")
        print(form_type)
        if form_type == "change_saldo":
            value = request.form.get("kwota")
            valid_data = app_handler.change_saldo(float(value))
        elif form_type == "sale":
            valid_data = app_handler.sale_book(request.form)
        else:
            valid_data = app_handler.buy_books(request.form)
        app_handler.save_app_context()
        if valid_data:
            return render_template("ksiegarnia.html", ksiegozbior=app_handler.ksiegozbior, saldo=app_handler.saldo)
        else:
            return "Nie mamy takiej kwoty"



@my_blueprint.route("/history/", defaults={"from_date": None, "to_date": None})
@my_blueprint.route("/history/<from_date>/<to_date>")
def show_history(from_date, to_date):
    data = app_handler.show_history(from_date, to_date)
    return render_template("historia.html", historia=data)
