from register import *
from functions import *

def main():
    flag = True
    op = int(input('Por favor ingrese una eleccion: '))
    registro = []
    s = None
    while flag:
        if op == 1:
            n = int(input('Ingrese una cantidad de registros a procesar: '))
            registro = carga(n, registro)
            op = int(input('Por favor ingrese una eleccion: '))
        elif op == 2:
            k = int(input('Por favor ingrese un numero entre 0 y 19: '))
            zona(k, registro)
            op = int(input('Por favor ingrese una eleccion: '))
        elif op == 3:
            matriz(registro)
            op = int(input('Por favor ingrese una eleccion: '))
        elif op == 4:
            s = generate(registro)
            op = int(input('Por favor ingrese una eleccion: '))
        elif op == 5:
            show(s)
        elif op == 6:
            print('Adios!!')
            flag = False


if __name__ == '__main__':
    main()
