n = int(input("Informe um numero inteiro positivo:"))
somafatorial = 0

if (n>0) and (n<50):
  for i in range (1,n+1):
    somafatorial += i
  print(f'A soma do fatorial do numero {n} é {somafatorial}')
else:
  print("Numero fora do intervalo")

