# Leia o nome do usuário

# Leia o peso do usuário

# Leia a altura do usuário

# Calcule o IMC

# Mostre o IMC do usuário na tela 

user = input("Digite seu nome")
peso = float(input("Digite seu peso"))
altura = float(input("Digite a sua altura"))

imc = peso/(altura*altura)

print("O IMC de",user,"é",imc)
