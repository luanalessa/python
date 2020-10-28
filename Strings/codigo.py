#O código identificador de um funcionário de um empresa é formado por 8 caracteres numéricos, o caractere hífen ('-') e a soma verificadora de caracteres numéricos. A soma verificadora é gerada somando-se o valor numérico de cada caractere ASCII do código identificador. O resultado numérico desta soma é convertido em uma string correspondente. Faça um programa que leia uma string de 8 caracteres numéricos e gere o código identificador correspondente

id = input("Digite o número identificador:")
print(f'Número identificador: "{id}"')
soma = ord(id[0]) + ord(id[1]) + ord(id[2]) + ord(id[3]) + ord(id[4]) + ord(id[5]) + ord(id[6]) + ord(id[7])
print(f'Soma dos caracteres ASCII: {ord(id[0])}+{ord(id[1])}+{ord(id[2])}+{ord(id[3])}+{ord(id[4])}+{ord(id[5])}+{ord(id[6])}+{ord(id[7])} = ',soma)
print(f'Conversão : {soma} -> "{soma}"')
print(f'Resultado final : "{id}-{soma}"') 
