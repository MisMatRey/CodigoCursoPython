from flask import Flask, render_template

# Crea una aplicacion Flask
app = Flask(__name__)

@app.route("/index")
@app.route("/")
def monstrar_html():
    return render_template("index.html")


@app.route("/saluda/<nombre>")
def saluda(nombre):
    return render_template("saluda.html",persona=nombre)