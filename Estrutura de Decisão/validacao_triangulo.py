A = float(input("Informe o tamanho do lado A: "))
B = float(input("Informe o tamanho do lado B: "))
C = float(input("Informe o tamanho do lado C: "))


if (A+B)>C and (A+C)>B and (B+C)>A and A>0 and B>0 and C>0:
  if(A>B) and (A>C) and (A**2==B**2+C**2) or (B>A) and (B>C) and (B**2==A**2+C**2) or (C>B) and (A<C) and (C**2==B**2+A**2):
      print("Os lados informados constituem um triangulo retangulo")
  elif (A>B) and (A>C) and (A**2>B**2+C**2) or (B>A) and (B>C) and (B**2>A**2+C**2) or (C>B) and (A<C) and (C**2>B**2+A**2):
      print("Os lados informados constituem um triangulo obtusangulo")
  elif (A>B) and (A>C) and (A**2<B**2+C**2) or (B>A) and (B>C) and (B**2<A**2+C**2) or (C>B) and (A<C) and (C**2<B**2+A**2):
      print("Os lados informados constituem um triangulo actangulo")  
else: 
  print("O triangulo não existe")
