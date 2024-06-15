nota = float(input('Insira sua nota: '))
presenca = int(input('Insira sua porcentagem de presença (sem %): '))

if nota >= 7 and presenca >= 75:
    print('Você foi aprovada!')
else:
    print('Você foi reprovada!')

