#Faça um programa que leia um número inteiro positivo N e calcule o N-ésimo elemento de acordo com a seguinte série: 2, 7, 3, 4, 21, 12, 8, 63, 48, 16,189, 192, 32, 567, 768... Retorne também a soma dos N primeiros elementos dessa mesma série.

n = int(input("Informe a posição do numero"))
num = 0

soma_a = 0
soma_b = 0
soma_c = 0
soma_total = 0


if (n % 3 == 1):
  num += 2 * (2) ** (n//3)
elif (n % 3 == 2):
  num += 7 * (3) ** (n//3)
elif (n % 3 == 0):
  num += 3 * (4) ** (n//3 - 1)

for i in range (1,n+1):
  if (i % 3 == 1):
    soma_a += 2 * (2) ** (i//3)
  elif (i % 3 == 2):
    soma_b +=  7 * (3) ** (i//3)
  elif (i % 3 == 0):
    soma_c += 3 * (4) ** (i//3 - 1)
  
soma_total+= soma_a + soma_b + soma_c
  
  
print(f'A posição {n} da série é igual a {num}.')
print(f'A soma dos {n} primeiros elementos da série é igual a {soma_total}.')

