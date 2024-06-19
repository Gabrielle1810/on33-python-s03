def contarCaracteres(texto):
    return len(texto)


entrada = 55
# Se eu pedir para o usuário uma palavra ou frase, através da função input(), qualquer coisa digitada pelo usuário será tratada como uma string, visto que essa função sempre retorna uma string. 

try:
    caracteres = contarCaracteres(entrada)
    print(f'A string {entrada}, tem {caracteres} caracteres')
   
except:
    print('Erro, digite uma palavra ou frase')