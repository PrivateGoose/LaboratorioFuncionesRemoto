a=int(input("Digite su número base: "))
b=int(input("Digite su número exponente: "))

def potencia(a,b):
    try:
        if(b==1):
            return(a)
        if(b!=1):
            return(a*potencia(a,b-1))
    except:
        print("Perdón, el programa no funciona con esas condiciones.")

while True:
    a=int(input("Digite cualquier número si desea continuar, en caso contrario, digite 0 para acabar el programa: "))
    if a==0:
        print("Programa finalizado")
        break
    else:
        a=int(input("Digite su número base: "))
        b=int(input("Digite su número exponente: "))
        print("Resultado:",potencia(a,b))
