#introdução ao try/except

numero=input('Digite um número para ser dobrado')

try:
    numero_float=float(numero)
    print(f'O dobro de {numero} é {numero_float*2}')
except:
    print(f'Isso não é um número')