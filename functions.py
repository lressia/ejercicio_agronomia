import random, os.path, pickle
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
    importe = random.random()*(random.randint(1, 500)/7)
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


def matriz(vec):
    v1 = int(input('Por favor ingrese un valor: '))
    v2 = int(input('Por favor ingrese un valor: '))
    fila, columna = 16, 20
    matriz = [[0] * columna for i in range(fila)]
    for i in vec:
        tipo = i.tipo
        zona = i.zona
        matriz[tipo][zona] += 1
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            if v1 < matriz[f][c] < v2:
                print(f'Tipo: {vec[f].tipo}| Zona: {vec[c].zona}| Cantidad: {matriz[f][c]}')

def prom(vec):
    promedio = 0
    cant = len(vec)

    for item in vec:
        promedio += item.importe
    promedio = promedio / cant

    return promedio

def generate(vec):
    promedio = prom(vec)
    name = input('Ingrese un nombre para el archivo(si no se encuentra será generado): ')
    m = open(name, 'wt', encoding='utf8')
    for item in vec:
        if item.importe > promedio:
            m.write(f'Id: {item.id}| Descripcion: {item.desc}| Importe: {item.importe}| Tipo: {item.tipo}| Zona: {item.zona}')
            m.write('\n')
    m.close()

    return name


def show(n):
    if not os.path.exists(n):
        print('Archivo no encontrado')
    else:
        m = open(n, 'rt', encoding='utf8')
        t = os.path.getsize(n)
        c = 0
        # print(t)
        while m.tell() < t:
            linea = m.readline()
            # linea = linea.split('\n')
            print(linea)
            c += 1
            print(m.tell)
        print(f'La cantidad de registros mostrados es de {c}')
        m.close()
