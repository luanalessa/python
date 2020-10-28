n = int()
for n in range (1, 8200):
  soma = 0 
  for i in range (1, n):
    if n % i == 0:
      soma += i
  if soma == n:
    print(n,"é um numero perfeito!")
  
 
    
