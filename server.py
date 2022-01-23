from flask import Flask, render_template, request, redirect
# importar la clase de friend.py
from User import User
app = Flask(__name__)
@app.route("/users")
def index():
    # llamar al método de clase get all para obtener todos los amigos
    users = User.get_all()
    print(users)
    return render_template("index.html",users=users)

@app.route("/user/new")
def user_form():
    return render_template("user_form.html")

@app.route('/create_user', methods=["POST"])
def create_user():
    # Primero hacemos un diccionario de datos a partir de nuestro request.form proveniente de nuestra plantilla
    # Las claves en los datos tienen que alinearse exactamente con las variables en nuestra cadena de consulta
    data = {
        "first_name": request.form["first_name"],
        "last_name" : request.form["last_name"],
        "email" : request.form["email"]
    }
    # Pasamos el diccionario de datos al método save de la clase Friend
    User.save(data)
    # No olvides redirigir después de guardar en la base de datos
    return redirect('/users')
            
if __name__ == "__main__":
    app.run(debug=True)