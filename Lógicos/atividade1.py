
nota = float(input('Insira sua nota: '))

if nota >= 7 and nota <= 10:
    print('Você foi aprovada!')
elif nota >= 1 and nota < 7:
    print('Você está reprovada!')
elif nota < 0 or nota > 10:
        print('Nota inválida!')


