#Faça um programa que escolha um número aleatório entre 1 e 10 e peça para o usuário adivinhá-lo. Antes de iniciar o jogo, escreva no terminal a tela abaixo:

#Adivinhe o número! Escolha o nível:
#1 - Fácil 2 - Difícil 3 - Insano
#Digite a sua opção: O nível Fácil permite quantas tentativas forem necessárias para o usuário acertar o número e mostra dicas quando ele errar: Tente um número maior! (se o usuário digitou um número menor do que o escolhido) ou Tente um número menor! (se o usuário digitou um número maior do que o escolhido). O nível Difícil limita o número de tentativas em 3, ainda mostrando as dicas. O nível Insano também limita o número de tentativas em 3, mas sem dicas. Ao nal diga em quantas tentativas o usuário acertou o número


import random # biblioteca para números aleatórios
# escolhe um número inteiro aleatório entre 1 a 10
n = random.randint(1, 10)

op = int(input("Digite 1 para o nível fácil, 2 para difícil e 3 para insano"))


if (op == 1):
  while True:
    m = int(input("Qual numero?"))
    if(m>n):
      print("Tente um número menor")
    elif(m<n):
      print("Tente um numero maior") 
    else:
      print("Você acertou")
      break
elif (op == 2):
  cont = 0
  while (cont < 3):
    m = int(input("Qual numero?"))
    if(m>n):
      print("Tente um número menor")
    elif(m<n):
      print("Tente um numero maior") 
    else:
      print("Você acertou")
      break
    cont += 1
  print("Voce perdeu")
elif (op == 3):
  cont = 0
  while (cont > 3):
    if(m>n):
      print("Tente um número menor")
    elif(m<n):
      print("Tente um numero maior") 
    else:
      print("Você acertou")
      break
    cont += 1
else:
  print("Opção errada") 
    



