#Faça um programa que leia uma lista de N elementos numéricos e retorne uma nova lista contendo somente os elementos únicos da lista lida, ou seja, removendo os elementos duplicados.

N = int(input("Qual o número de elementos da lista? "))
lista = [ ] 


for i in range (N):
  lista.append(int(input(f'Digite o elemento {i} da lista: ')))
  
print("Lista original:")
print(lista)
print("Nova lista:")
print(list(set(lista)))
