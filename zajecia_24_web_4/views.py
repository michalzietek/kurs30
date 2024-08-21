# class LoginView:
#
#     def process(self):
#         print("logika odpowiedzialna za zalogowanie uzytkownika")

from flask.views import MethodView
from flask import render_template

class MainView(MethodView):

    def get(self):
        return render_template("index.html")

    def post(self):
        return "Zrobiłeś zapytanie typu post"
