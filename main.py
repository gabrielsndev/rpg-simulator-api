from fastapi import FastAPI
import random

app = FastAPI()

@app.get('/')
def read_root():
    return {'message': 'Bem-vindo ao RPG Simulator API!'}

# @app.get('/roll/expression/{expressao}')
# def roll_multiple_dice(expressao: str):
#     values = expressao.split('d')
    
#     if len(values) < 2:
#         return {'error': 'Input  inválido, utilize o modelo {quantidade}d{lado}.'}
    
#     quantidade = int(values[0])
#     lado = int(values[1])
    
#     if lado < 2:
#         return {'error': 'Número de lados deve ser maior que 2.'}
    
#     if quantidade < 1:
#         return {'error': 'Número de dados deve ser maior ou igual a 1.'}
    
#     resultado = 0
#     for i in range(quantidade):
#         resultado += random.randint(1, lado)

#     return {'dado': f'{quantidade}d{lado}', 'total': resultado}    

@app.get('/roll/{lado}')
def roll_dice(lado: str):
    if lado < 2:
        return {'error': 'Número de lados deve ser maior que 2.'}
    
    resultado =  random.randint(1, lado)
    return{'dado': f'd{lado}', 'resultado': resultado}


