#introdução a f-strings
nome='Renato'
altura=1.80
peso=60
imc=peso/(altura*altura)

linha_1=f'{nome} tem {altura:.2f} de altura'
linha_2=f'pesa {peso} quilos e seu IMC é: {imc:.2f}'

print(linha_1)
print(linha_2)
