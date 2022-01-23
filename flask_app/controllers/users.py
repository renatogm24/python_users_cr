from flask import render_template, request, redirect

from flask_app.models.user import User

from flask_app import app

@app.route("/")
def index2():
    # llamar al método de clase get all para obtener todos los amigos
    users = User.get_all()
    print(users)
    return render_template("index.html",users=users)

@app.route("/users")
def users():
    # llamar al método de clase get all para obtener todos los amigos
    users = User.get_all()
    print(users)
    return render_template("index.html",users=users)

@app.route("/user/new")
def user_form():
    title = "Create user"
    data = {
        "id": 0,
        "first_name": "",
        "last_name": "",
        "email": "",
        "created_at" : "",
        "updated_at" : ""
    }
    user = User(data)
    return render_template("user_form.html", user=user, title=title)

@app.route("/user/edit/<int:id>")
def user_show(id):
    title = "Edit user"
    data = {
        "id": id
    }
    user = User.get_user_by_id(data)
    return render_template("user_form.html", user=user, title = title)

@app.route("/user/delete/<int:id>")
def delete(id):
    data = {
        "id": id
    }
    User.delete(data)
    return redirect("/users")

@app.route("/user/show/<int:id>")
def user_edit(id):
    data = {
        "id": id
    }
    user = User.get_user_by_id(data)
    return render_template("user_info.html", user=user)

@app.route('/create_user', methods=["POST"])
def create_user():
    if(request.form["id"] != 0):
      data = {
        "id": request.form["id"],
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
      }
      User.update(data)
    else:
      data = {
          "first_name": request.form["first_name"],
          "last_name" : request.form["last_name"],
          "email" : request.form["email"]
      }
      User.save(data)

    return redirect('/users')