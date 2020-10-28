#Faça um programa que leia uma quantidade inteira de dinheiro (em R$) e retorne as quantidades m´ınimas de notas nos valores de R$100, R$50, R$20, R$10, R$5, R$2 e R$1 (moeda) em que o valor pode ser convertido.
#• Exemplo: Dinheiro = R$173 → 1 nota de R$100, 1 nota de R$50, 1 nota de R$20, 1 nota de R$2 e 1 moeda de R$1.

valor = int(input("Informe o valor desejado: "))

n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0
n1 = 0

while (valor >=100):
  n100 += 1
  valor = valor - 100

while (valor >=50):
  n50 += 1
  valor = valor - 50

while (valor >=20):
  n20 += 1
  valor = valor - 20

while (valor >=10):
  n10 += 1
  valor = valor - 10

while (valor >= 5):
  n5 += 1
  valor = valor - 5

while (valor >=2):
  n2 += 1
  valor = valor - 2

while (valor >=1):
  n1 += 1  
  valor = valor - 1

valor = n100*100 + n50*50 + n20*20 + n10*10 + n5*5 + n2*2 + n1*1 

print("Dinheiro = R$",valor,":",n100,"nota de 100,",n50,"nota de 50,", n20,"nota de 20,",n10,"nota de 10,",n5,"nota de 5,",n2,"nota de 2 e ",n1,"nota de 1" )


