#Uma companhia de teatro deseja montar uma série de espetáculos. A direção calcula que, a R$5,00 o ingresso, serão vendidos 120 ingressos,e que as despesas serão de R$ 200,00. Diminuindo-se em R$0,50 o preço dos ingressos, espera-se que as vendas aumentem em 26 ingressos. Faça um programa que escreva uma tabela de valores de lucros esperados em função do preço do ingresso, fazendo-se variar esse preço de R$5,00 a R$1,00, de R$0,50 em R$0,50. Ao nal, escreva o preço em que o lucro máximo é obtido
v_ingresso = 5.0
t_ingresso = 120
despesas = 200
lucro_liquido = v_ingresso*t_ingresso
lucro = lucro_liquido - despesas
lucro_maximo = 0

while (v_ingresso >= 1):
  print(f'Valor do Ingresso: {v_ingresso} | Total de ingressos: {t_ingresso} |Lucro liquido: {lucro_liquido} | Lucro: {lucro}')
  v_ingresso -= 0.5
  t_ingresso += 26
  lucro_liquido = v_ingresso*t_ingresso
  lucro = lucro_liquido - despesas
  if (lucro_maximo < lucro):
    lucro_maximo = lucro
print(f'O lucro máximo é {lucro_maximo}')










