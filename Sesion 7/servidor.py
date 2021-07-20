from flask import Flask, request

# Crea una aplicacion Flask
app = Flask(__name__)

#Creando la ruta /
@app.route("/")
def hello():
    return "Hello World a todos!!!"

#Creando la ruta /
@app.route("/test")
def test():
    return "Esto es una prueba"

@app.route("/suma")
def suma():
    #Acceder a un parametro en Querystring
    #request.args.get('parametro',valor por defecto, tipo)
    parametro1 = request.args.get('a',0,int)
    parametro2 = request.args.get('b',0,int)
    return "Suma de {} + {} = {}".format(parametro1,parametro2,parametro1+parametro2)

@app.route("/saludos/<nombre>")
@app.route("/saludos/<nombre>/<int:edad>")
def saluda(nombre,edad=10):
    return "Hola {} que tiene edad {}".format(nombre,edad)


@app.route("/calculadora/<operacion>")
def calculadora(operacion):
    #Acceder a un parametro en Querystring
    #request.args.get('parametro',valor por defecto, tipo)
    parametro1 = request.args.get('a',0,int)
    parametro2 = request.args.get('b',0,int)
    if operacion == "suma":
        return "Suma de {} + {} = {}".format(parametro1,parametro2,parametro1+parametro2)
    elif operacion == "resta":
        return "Resta de {} - {} = {}".format(parametro1,parametro2,parametro1-parametro2)
    elif operacion == "multiplicacion":
        return "Multiplicacion de {} x {} = {}".format(parametro1,parametro2,parametro1*parametro2)
    elif operacion == "division":
        try:
            return "Division de {} / {} = {}".format(parametro1,parametro2,parametro1/parametro2)
        except:
            return "Division entre 0 no permitida!!!"
        #return "Division de {} / {} = {}".format(parametro1,parametro2,parametro1/parametro2)