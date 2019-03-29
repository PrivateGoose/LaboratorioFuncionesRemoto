a=int(input("Digite su número base: "))
b=int(input("Digite su número exponente: "))

def potencia(a,b):
  elev=a
  for i in range(1,b):
    elev=elev*a
    
  print(elev)

potencia(a,b)