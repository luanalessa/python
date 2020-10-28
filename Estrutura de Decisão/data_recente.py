d1 = int(input("Informe o dia: "))
while True:
  m1 = int(input("Informe o mês: "))
  if m1 <= 12:
    break
  else:
    print("Erro! Informe o mes correto.")
a1 = int(input("Informe o ano: "))

d2 = int(input("Informe o dia: "))
while True:
  m2 = int(input("Informe o mês: "))
  if m2 <= 12:
    break
  else:
    print("Erro! Informe o mes correto.")
a2 = int(input("Informe o ano: "))

if(a1>a2):
    print("A data:",d1,"/",m1,"/",a1," é a mais recente")
elif(a1<a2):
    print("A data:",d2,"/",m2,"/",a2," é a mais recente")
else: #anos iguais
  if(m1>m2):
    print("A data:",d1,"/",m1,"/",a1," é a mais recente")
  if(m1<m2):
    print("A data:",d2,"/",m2,"/",a2," é a mais recente")
  else:#meses iguais
    if(d1>d2):
          print("A data:",d1,"/",m1,"/",a1," é a mais recente")
    elif(d1<d2):
        print("A data:",d2,"/",m2,"/",a2," é a mais recente")
    else:
        print("As datas:",d1,"/",m1,"/",a1," são iguais")



 

