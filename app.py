from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect

import forms

app = Flask(__name__)

app.secret_key = 'clave_secreta'

csrf = CSRFProtect()

@app.route("/")
def index():
    titulo = "Flask IDGS-801"
    lista = ["Emmanuel","Haziel","Emiliano","Flor"]
    return render_template("index.html", titulo=titulo, lista=lista)

@app.route("/operasBas", methods=['GET','POST'])
def operasBas():
    n1=0
    n2=0
    res=0
    if request.method=='POST':
        n1 = request.form.get('n1')
        n2 = request.form.get('n2')
        res = float(n1) + float(n2)
    return render_template("operasBas.html", n1=n1,n2=n2,res=res)

@app.route("/resultado", methods=['GET','POST'])
def resultado():
    n1 = request.form.get('n1')
    n2 = request.form.get('n2')
    tem = float(n1) + float(n2)
    return f'La suma de {n1} + {n2} es: {tem}'

@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")

@app.route("/usuarios", methods = ['GET', 'POST'])
def usuarios():
    mat=0
    nom=''
    apa=''
    ama=''
    email=''
    usuario_class = forms.UserForm()
    if request.method == 'POST' and usuario_class.validate():
        mat = usuario_class.matricula.data
        nom = usuario_class.nombre.data
        apa = usuario_class.apaterno.data
        ama = usuario_class.amaterno.data
        email = usuario_class.correo.data
        mensaje = 'Bienvenido {}'.format(nom)
        flash(mensaje)
    return render_template("usuarios.html", form = usuario_class, mat=mat, nom=nom, apa=apa, ama=ama, email=email)

@app.route("/hola")
def hola():
    return "Hola mundo"

@app.route("/user/<string:user>")
def user(user):
    return f"Hola, {user}!"

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return f"<h1> Hola, {username}! Tu id es: {id}<h1>"

@app.route("/default/")
@app.route("/default/<string:param>")
def func(param="Danlei"):
    return f"<h1>¡Hola, {param}!<h1>"

@app.route("/operas")
def operas():
    return '''
    <form>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" requiered>
        </br>
        <label for="name">apaterno:</label>
        <input type="text" id="name" name="name" requiered>
    </form>
    '''

if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True)