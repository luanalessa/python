#Faça um programa que preencha dois vetores com N elementos e retorne dois novos vetores: um contendo a interseção entre os vetores lidos e outro contendo a união entre os mesmos vetores. Ambos os vetores retornados não devem ter elementos repetidos.

N = int(input("Qual o número de elementos das listas? "))
uniao = [ ]

lista_1 = [ ]
for i in range (N):
  lista_1.append(int(input(f'Digite o elemento {i} do vetor 1: ')))

uniao += lista_1

lista_2 = [ ]
for i in range (N):
  lista_2.append(int(input(f'Digite o elemento {i} do vetor 2: ')))

uniao += lista_2
  
comum_numero = [numero for numero in lista_1 if numero in lista_2]

uniao.sort()
comum_numero.sort()

print("Primeiro vetor:")
print(lista_1)  
print("Segundo vetor:")
print(lista_2)
print("Vetor interseção:")
print(comum_numero)
print("Vetor união:")
print(list(set(uniao)))



