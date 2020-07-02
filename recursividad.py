#Es hacer que una funcion se llame a si misma

def factorial(n):
    if n>1
        return n * factorial(n-1)
    return 1 #como si no se cumple la condicion del if, simplemente saltea la linea, no es necesario el else
print factorial(5)
