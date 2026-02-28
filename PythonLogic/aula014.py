#formatação de strings com o método format
a='A'
b='B'
c=1.1

formato='a={} b={} c={:.2f}'.format(a,b,c)
formato_indicie='a={0} b={1} c={2:.2f}'.format(a,b,c)

print(formato)
print(formato_indicie)
