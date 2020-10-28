# Leia o ano que será testado

# Verifique se o ano é bissexto

# Escreva o resultado na formatação pedida.

ano = int(input("Digite o ano"))

if ano%100!=0 and ano%400==0 or ano%4==0:
  print("O ano",ano,"é bissexto.")
else:
  print("O ano",ano,"não é bissexto.")
 
    
