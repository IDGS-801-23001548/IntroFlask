from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect
import math

import forms, userform

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
    
@app.route("/boletos", methods=['GET', 'POST'])
def boletos():
    usuario_class = userform.boletos()
    total = 0
    boletos = usuario_class.boletos.data
    tarjeta = usuario_class.tarjeta.data
    nombre = usuario_class.nombre.data
    compradores = usuario_class.compradores.data

    if request.method == 'POST' and usuario_class.validate_on_submit():
        total = boletos * 12

        if boletos > 5:
            total *= 0.85
        elif boletos >= 3:
            total *= 0.90

        if tarjeta == '1':
            total *= 0.90

    return render_template("boletos.html", form=usuario_class, total=total, nombre=nombre, compradores=compradores, tarjeta=tarjeta, boletos=boletos)


@app.route("/distancia", methods=['GET', 'POST'])
def distancia():

    form = forms.DistanciaForm()
    distancia=0
    x1=0
    x2=0
    y1=0
    y2=0
    
    if request.method == 'POST':
        
        x1 = float(request.form['x1'])
        x2 = float(request.form['x2'])
        y1 = float(request.form['y1'])
        y2 = float(request.form['y2'])
        
        distancia = math.sqrt(pow((x2-x1),2) + pow((y2-y1),2))
    
    return render_template("distancia.html", form=form, x1=x1,x2=x2, y1=y1, y2=y2, distancia=distancia)

if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True)