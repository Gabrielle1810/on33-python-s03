while True: 
    nota = float(input('Insira uma nota de 1 a 10'))
    if 0 <= nota <= 10:
        if nota >=7:
            print('Aprovado')
        else:
            print('Reprovado')
        break
    else:
        print('Nota inválida, digite uma nota entre 1 e 10.') 

