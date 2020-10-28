#Faça um programa que leia a duração de um evento em segundos e converta para horas, minutos e segundos

segundos = int(input("Informe os segundos do evento: "))

horas = (segundos / (60*60))
total_h = int(horas)
rest_segundos = segundos % 3600
minutos = rest_segundos / 60
total_m = int(minutos)
total_s = segundos % 60


if(total_h>1):
  print("Duração =",segundos,"segundos:",total_h,"horas,",total_m,"minutos e",total_s,"segundos")
elif(total_h==1):
  print("Duração =",segundos,"segundos:",total_h,"hora,",total_m,"minutos e",total_s,"segundos")
else:
  print("Duração =",segundos,"segundos:",total_m,"minutos e",total_s,"segundos")




