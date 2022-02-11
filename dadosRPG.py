import random

def rolarComVantagem(dado):
    rol1 = random.randint(1,dado)
    rol2 = random.randint(1,dado)
    if rol1>rol2:
        return rol1
    else:
        return rol2
    
def rolarComDesvantagem(dado):
    rol1 = random.randint(1,dado)
    rol2 = random.randint(1,dado)
    if rol1<rol2:
        return rol1
    else:
        return rol2

#rolar um dado do valor passado
def rolarDado(dado):
    return random.randint(1,dado)