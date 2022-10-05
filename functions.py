import random
from register import *


def validate(n, id):
    for item in id:
        while n == item:
            n = random.randint(0, 455)

    return n

def azar():
    v = []
    id = random.randint(0, 455)
    id = validate(id, v)
    desc = random.choice(['Riego por la mañana', 'Riego por la tarde', 'Riego por la noche', 'Paseo con el tractor'])
    importe = random.random()*1450.25
    tipo = random.randint(0, 15)
    zona = random.randint(0, 19)
    v.append(id)

    return id, desc, importe, tipo, zona


def add_in_order(vec, re):
    n = len(vec)
    pos = n
    izq, der = 0, n-1
    while izq <= der:
        c = (izq + der)//2
        if vec[c].id == re.id:
            pos = c
            break
        if vec[c].id < re.id:
            izq = c + 1
        else:
            der = c - 1
    if izq > der:
        pos = izq

    vec[pos:pos] = [re]


def carga(n, re):
    for i in range(n):
        t = azar()
        s = Operacion(t[0], t[1], t[2], t[3], t[4])
        add_in_order(re, s)

    return re

def zona(n, vec):
    for item in vec:
        if item.zona >= n:
            to_string(item)
