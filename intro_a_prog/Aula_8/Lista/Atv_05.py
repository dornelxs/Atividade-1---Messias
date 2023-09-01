#Dado uma tupla de tuplas, onde cada tupla interna representa um intervalo de tempo (horário de início
#e horário de término), crie um algoritmo que retorne a quantidade de horas total dos intervalos.
#Exemplo de entrada: ((8, 12), (14, 18), (19, 22))
#Saída esperada: 11

intervalos = ((6, 8), (12, 14), (9, 11))

horas_totais = 0

for intervalo in intervalos:
    horas_inicio, horas_finais = intervalo
    horas_intervalo = horas_finais - horas_inicio
    horas_totais += horas_intervalo

print(horas_totais)


