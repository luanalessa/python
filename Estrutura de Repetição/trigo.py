#Considere um tabuleiro de xadrez comum, com 64 casas. Qual o total em toneladas (1t = 1000kg) que será obtido se você colocar na primeira casa 1 grão de trigo, na segunda casa, 2 grãos de trigo, na terceira casa, 4 grãos de trigo, e assim sucessivamente, sempre dobrando a quantidade anterior. Sabe-se que 1 grão de trigo pesa 0,00526g. Escreva um programa para realizar esse cálculo.
trigo = 1

for i in range (0,65):
  trigo *= 2
  quantidade = (trigo * (0.0052))+1
gramas_kilos = quantidade/1000
kilos_toneladas = gramas_kilos/1000
print(f'{kilos_toneladas} toneladas')


