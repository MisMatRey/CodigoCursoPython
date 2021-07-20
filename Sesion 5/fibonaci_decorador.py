def memorize(f):
    memoria = {}

    def wraper(X):
        if X not in memoria:
            memoria[X] = f(X)
        return memoria[X]
    return wraper

@memorize
def fibo(x):
    if x == 2 :
        return 1
    elif x == 1 :
        return 1
    else : 
        return fibo(x - 1) + fibo(x - 2)

print(fibo(40))