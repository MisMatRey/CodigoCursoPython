# En Python las funciones son de orden superior 
# Son funciones que funciones que reciben funciones

# Un decorador es una funcion se ejecuta PRIMERO que otra funcion
# El Decorador TIENE  que regresar una funcion que sustituye a la ORIGINAL
def mi_primer_decorador(hello_word):
    print("Ejecucion de Decorador")

    def funcion_dummy():
        print("Esta es una funcion Dummy")
        
        return hello_word
    # Este return SUSTITUYE LA IMPLEMENTACION de la funcion original
    return funcion_dummy

@mi_primer_decorador
def hello_word():
    print("Hello Word!!")

hello_word()