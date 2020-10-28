custo_total = float(input("Informe o custo total da viagem:"))
valor_inicial = float(input("Informe o valor inicial da poupança:"))
valor_mensal = float(input("Informe o valor a ser depositado mensalmente:"))
rendimento_mensal = float(input("Informe o rendimento mensal da poupança:"))

tempo = 0

while (valor_inicial < custo_total): 
 valor_inicial += valor_mensal + (valor_inicial*rendimento_mensal)/100 
 tempo += 1  
  
print("Em",tempo,"meses você terá R$%.2f"%valor_inicial,"para sua viagem!")
  
