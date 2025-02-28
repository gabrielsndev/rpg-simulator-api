import random

dado = '2d20-3'
acrescimo = 0 
decrescimo = 0

if 'd' in dado:
    dado = dado.split('d')
else:
    print('Valor informado é inválido.')
    
if len(dado) != 2:
    print('Valor informado é inválido.')
    
quantidade_dados = int(dado[0])
lado_dados = dado[1]

if '+' in lado_dados:
    dados = lado_dados.split('+')
    lado_dados = int(dados[0])
    acrescimo = int(dados[1])
    
elif '-' in lado_dados:
    dados = lado_dados.split('-')
    lado_dados = int(dados[0])
    decrescimo = int(dados[1])
else:
    lado_dados = int(lado_dados)



if quantidade_dados < 1 or lado_dados < 2:
    print('Valor inválido para quantidade de dados ou lado dos dados.')
    
total = 0
for i in range(quantidade_dados):
    dado_atual = random.randint(1, lado_dados)
    total += dado_atual

if acrescimo:
    total += acrescimo
    
elif decrescimo:
    total -= decrescimo
    
    
print(total)