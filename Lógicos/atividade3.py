nota = float(input('Digite sua nota de 1 a 10: '))
presenca = float(input('Digite sua presença em porcentagem: '))

if nota >= 7 or presenca >= 75:
    print('Parabéns! Você foi aprovada!')
else:
    print('Lamento, você foi reprovada!')