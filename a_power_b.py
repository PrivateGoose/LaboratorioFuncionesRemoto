a=int(input("Digite su número base: "))
b=int(input("Digite su número exponente: "))

def potencia(a,b):
  elev=a
  for i in range(1,b):
    elev=elev*a
    
  print(elev)

potencia(a,b)

while True:
    a=int(input("Digite cualquier número si desea continuar, en caso contrario, digite 0 para acabar el programa: "))
    if a==0:
        print("Programa finalizado")
        break
    else:
        a=int(input("Digite su número base: "))
        b=int(input("Digite su número exponente: "))
        print("Resultado:",potencia(a,b))
