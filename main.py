from fastapi import FastAPI
import random

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Bem-vindo ao RPG Simulator API!'}
  

@app.get('/roll/{dado}')
def roll_dice(dado: str):
    import random

    acrescimo = 0 
    decrescimo = 0

    if 'd' in dado:
        dado = dado.split('d')
    else:
        return'Valor informado é inválido'
        
    if len(dado) != 2:
        return'Formato informado é inválido'
        
    try: quantidade_dados = int(dado[0])
    except: return'A quantidade de dados informada é inválida'

    lado_dados = dado[1]

    if '+' in lado_dados:
        try:
            dados = lado_dados.split('+')
            lado_dados = int(dados[0])
            acrescimo = int(dados[1])
        except: return'Valor inválido para acrescimo dos dados'
        
    elif '-' in lado_dados:
        try:
            dados = lado_dados.split('-')
            lado_dados = int(dados[0])
            decrescimo = int(dados[1])
        except: return'Valor inválido para decrescimo dos dados'
    else:
        try:
            lado_dados = int(lado_dados)
        except: return'Valor inválido para lado dos dados'



    if quantidade_dados < 1 or lado_dados < 2:
        return'Valor inválido para quantidade de dados ou lado dos dados.'
        
    total = 0
    for i in range(quantidade_dados):
        dado_atual = random.randint(1, lado_dados)
        total += dado_atual

    if acrescimo:
        total += acrescimo
        
    elif decrescimo:
        total -= decrescimo
        
    return total

