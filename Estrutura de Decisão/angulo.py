#Faca um programa que receba a medida de um angulo em graus. Calcule e mostre o quadrante em que se localiza esse angulo. Considere os quadrantes da trigonometria e, para angulos maiores que 360◦ ou menores que -360◦ reduzi-los, mostrando tambem o numero de voltas e o sentido da volta (horario ou anti-horario).

angulo = float(input("Informe o angulo em graus"))
voltas = 0

#Condicional para o angulo positivo menor que 360
if (0<angulo<=90):
  print("O angulo se localiza no primeiro quadrante")
elif(90<angulo<=180):
  print("O angulo se localiza no segundo quadrante") 
elif(180<angulo<=270):
  print("O angulo se localiza no terceiro quadrante")
elif(270<angulo<=360):
  print("O angulo se localiza do quarto quadrante") 
#Condicional para o angulo positivo maior que 360 
elif (angulo>360):
  while (angulo>360):
    angulo = angulo/4 
    rest_angulo = angulo%4
  
    voltas += 1
    if(0<rest_angulo<=90):
      print("O angulo dá",voltas," volta(s) sentido horário e se localiza no primeiro quadrante, marcando",rest_angulo,"º")
    elif(90<angulo<=180):
      print("O angulo dá ",voltas," volta(s) sentido horário e se localiza no segundo quadrante, marcando",angulo,"º")
    elif(180<angulo<=270):
      print("O angulo dá ",voltas," volta(s) sentido horário e se localiza no terceiro quadrante, marcando",angulo,"º")
    elif(270<angulo<=360):
      print("O angulo dá ",voltas," volta(s) no sentido horário e se localiza do quarto quadrante, marcando",angulo,"º") 

#Condicional para o angulo negativo menor que 0
else:
    if(0>angulo>=-90):
      print("O angulo se localiza no primeiro quadrante no sentido anti-horário")
    elif(-90>angulo>=-180):
      print("O angulo se localiza no segundo quadrante no sentido anti-horário")
    elif(-180>angulo>=-270):
      print("O angulo se localiza no terceiro quadrante no sentido anti-horário")
    elif(-270>angulo>=-360):
      print("O angulo se localiza do quarto quadranteno sentido anti-horário")
      #Condicional para o angulo negativo menor que 360
    elif (((angulo)*(-1))>360):
      while(((angulo)*(-1))>360):
        angulo = (angulo / 4)
        voltas += 1
        if(0<angulo<=90):
          print("O angulo se localiza no primeiro quadrante no sentido anti-horário")
        elif(90<angulo<=180):
          print("O angulo se localiza no segundo quadrante no sentido anti-horário")
        elif(180<angulo<=270):
          print("O angulo se localiza no terceiro quadrante no sentido anti-horário")
        elif(270<angulo<=360):
          print("O angulo se localiza do quarto quadranteno sentido anti-horário")


    
