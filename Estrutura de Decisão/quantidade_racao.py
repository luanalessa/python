#Cesar comprou um saco de ração com peso em quilos (kg) para alimentar seus cachorros. A quantidade de ração para cada cachorro é medida em gramas (g) e é sempre a mesma quantidade por dia. Faça um programa que receba o peso do saco de ração, o número de cachorros e a quantidade de ração fornecida para cada cachorro. Calcule e mostre se a quantidade de ração é suficiente e quanto restará de ração no saco após 1 semana.

saco = float(input("Informe o peso do saco de ração"))
cachorros = float(input("Informe o numero de cachorros"))
ração = 0
cont = 0
while cont < cachorros:
  ração = float(input("Informe a quantidade de ração"))
  cont = cont + 1
  ração = ração + ração

if((ração*7)==saco):
    print("A ração só é suficiente para uma semana")
elif((ração*7)<saco):
    total = saco - (ração*7)
    print("A ração é suficiente para uma semana e restam",total)
else:
    falta = (ração*7) - saco
    print("A ração não é suficiente para uma semana",falta)







