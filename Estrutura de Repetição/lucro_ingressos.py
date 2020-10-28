i = float(input("Informe o valor esperado de ingressos ao preço de R$5,00:"))
d = float(input("Informe o valor da despesas do espetáculo:"))
a = float(input("Informe o aumento esperado da venda, diminuindo R$0,50 do preço do ingresso:"))

preco = 5.5
lucro_max = 0
total_preco=0
total_i = 0

while (preco >=1):
  if(preco == 5.5):
    print(f"Preço\tPúblico\tLucro")
    preco -=0.5

  else:
    lucro = preco*i - d 
    print("R$%.2f"%preco,"\t%.0f"%i,"\tR$%.2f"%lucro)
    preco -= 0.5
    i += a
    lucro = preco*i - d 
    if (lucro_max <= lucro):
      lucro_max = lucro
      total_preco = preco
      total_i = i
    
print(f'Ao preço de R${total_preco:0.2f} serão vendidos {total_i:0.0f} ingressos e o lucro será de R${lucro_max:0.2f}.')
  


