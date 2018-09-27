#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

fich = open(sys.argv[1], 'r')
lineas = fich.readlines()
fich.close()

from calcoohija import CalculadoraHija

Calc_Hija = CalculadoraHija()
for linea in lineas:
    elemento = linea.split(',')
    elemento[-1] = elemento[-1][:-1]
    operandos = elemento[1:]
    if elemento[0] == 'suma':
        operando_aux = 0
        for operado in operandos:
            suma = Calc_Hija.plus(operando_aux, int(operado))
            operando_aux = suma

    elif elemento[0] == 'resta':
        operando_aux = int(operandos[0])
        for operando in operandos[1:]:
            operando_aux = Calc_Hija.minus(operando_aux, int(operando))
            resta = operando_aux
    elif elemento[0] == 'multiplica':
        operando_aux = 1
        for operado in operandos:
            producto = Calc_Hija.multiplicacion(operando_aux, int(operado))
            operando_aux = producto
    elif elemento[0] == 'divide':
        operando_aux = int(operandos[0])
        for operando in operandos[1:]:
            operando_aux = Calc_Hija.division(operando_aux, int(operando))
            if int(operando) == 0:
                print('No se puede dividir por zero')
            else:
                razon = operando_aux
    else:

        print('No se puede realizar la operacion')

print("Suma = " + str(suma))
print("Resta = " + str(resta))
print("Multiplicacion = " + str(producto))
print("Division = " + str(int(razon)))
