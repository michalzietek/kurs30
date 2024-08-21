from flask import render_template, Blueprint, request
# from views import LoginView
from views import MainView

my_blueprint = Blueprint("my_blueprint", __name__)

# @my_blueprint.route("/")
# def main_view():
#     return render_template("index.html")
#
#
# @my_blueprint.route("/login", methods=["POST"])
# def login():
#     if request.method == "POST":
#         LoginView().process()

my_blueprint.add_url_rule("/", view_func=MainView.as_view("main_view"))
