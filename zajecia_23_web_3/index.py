from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


users = [{
        "name": "Michal",
        "surname": "Zietkowski",
        "email": "michalzietkowski@gmail.com"
    },
    {
        "name": "Adam",
        "surname": "Malysz",
        "email": "adam.malysz@op.pl"
    },
    {
        "name": "Mariusz",
        "surname": "Pudzianowski",
        "email": "tobynicniedalo@wp.pl"
    }
]

@app.route("/")
def hello():
    print("Tutaj jestem")
    wynik = 2 + 2
    print(wynik)
    return "Witaj w naszym programie"

@app.route("/hello/", defaults={"name": None})
@app.route("/hello/<name>/")
def hello_user(name):
    return render_template("hello_user.html", user=name)
    #return render_template("hello_user.html")

@app.route("/users/")
def show_users():
    return render_template("users_list.html", users=users)

@app.route("/users/create", methods=["GET", "POST"])
def create_user():
    if request.method == "GET":
        return render_template("create_user.html")
    elif request.method == "POST":
        users.append({
            "name": request.form.get("name"),
            "surname": request.form.get("surname"),
            "email": request.form.get("email")
        })
        return redirect(url_for("show_users"))


@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("example_with_multiple_forms.html")
    elif request.method == "POST":
        print(request.form.get("form_type"))
        return render_template("example_with_multiple_forms.html")

if __name__ == "__main__":
    app.run(debug=True)