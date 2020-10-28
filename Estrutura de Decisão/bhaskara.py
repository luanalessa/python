import math

# Pode usar math.sqrt(x) ou x ** 0.5 para tirar a raiz quadrada de x

a = float(input("Digite o coeficiente a"))
b = float(input("Digite o coeficiente b"))
c = float(input("Digite o coeficiente c"))

delta = b**2 - 4*a*c
x1 = (-b + (delta)**(1/2))/(2*a)
x2 = (-b - (delta)**(1/2))/(2*a)

if x1 != x2 and delta > 0:
  print("A equação possui 2 raízes reais:")
  print("x =",x1)
  print("x =",x2)
elif delta < 0:
  print("A equação não possui raízes reais.")
else:
  print("A equação possui 1 raiz real:")
  print("x =",x1)

  
