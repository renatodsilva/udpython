#formatação de strings com f-strings
#s - string
#d - int
#f - floa
#x ou X - Hexadecimal
#(caractere)(><^)(quantidade)
#> - esquerda
#< - direita
#^ - centro
#sinal - + ou -
#conversion flags - !r !s !a

variavel='ABC'
print(f'{variavel}')
print(f'{variavel:>10}')
print(f'{variavel:<10}')
print(f'{variavel:^10}')
print(f'{-1000.1831983912:+,.2f}')