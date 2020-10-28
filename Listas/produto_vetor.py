#Faça um programa que preencha dois vetores de números inteiros. Os vetores devem ser lidos com os elementos separados por vírgula (por exemplo, 1,2,3,4,5). Caso os vetores tenham tamanhos diferentes, mostre "Os vetores devem ter o mesmo número de elementos!" e termine o programa. Caso contrário, calcule e mostre os produtos interno e externo entre os vetores lidos. Por último, calcule e mostre a matriz transposta do produto externo calculado.

#Importante: Você deve usar somente listas básicas da linguagem Python para resolver o problema. Nenhuma função ou pacote adicional pode ser usado


a = input('Digite o vetor 1 (elementos separados por vírgula): ')
v_a = list(a.split(","))
vetor_a = [int(x) for x in v_a]

b = input('Digite o vetor 2 (elementos separados por vírgula): ')
v_b = list(b.split(","))
vetor_b = [int(x) for x in v_b]

if (len(vetor_a) != len(vetor_b)):
  print("Os vetores devem ter o mesmo número de elementos!")
else: 
  produto_interno = 0
  produto_externo = 0
  produto_externot = 0
  vetor_c = [ ]
  vetor_d = [ ]
  cont = 0
  contt= 0

  for i in range(len(vetor_a)):
    produto_interno += vetor_a[i] * vetor_b[i]
    
  print('Primeiro vetor: ',vetor_a)
  print('Segundo vetor: ', vetor_b)
  print('Produto interno:', produto_interno)
  print('Produto externo: ')
  while (cont < len(vetor_b)):
    for i in range(len(vetor_a)):
      produto_externo = vetor_b[i] * vetor_a[0+cont]
      vetor_c.append(produto_externo)
    print(vetor_c)
    cont += 1
    vetor_c[:] = []
    
  print('Produto externo transposto: ') 
  while (contt < len(vetor_b)):
    for i in range(len(vetor_a)):
      produto_externot = vetor_b[0+contt] * vetor_a[i]
      vetor_d.append(produto_externot)
    print(vetor_d)
    contt += 1
    vetor_d[:] = []
     
  
  

