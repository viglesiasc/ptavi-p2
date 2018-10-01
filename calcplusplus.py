#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import csv

from calcoohija import CalculadoraHija
Calc_Hija = CalculadoraHija()

with open(sys.argv[1]) as fichero:
    reader = csv.reader(fichero)
    for linea in reader:
        operandos = linea[1:]
        if linea[0] == 'suma':
            operando_aux = 0
            for operado in operandos:
                suma = Calc_Hija.plus(operando_aux, int(operado))
                operando_aux = suma
        elif linea[0] == 'resta':
            operando_aux = int(operandos[0])
            for operando in operandos[1:]:
                operando_aux = Calc_Hija.minus(operando_aux, int(operando))
                resta = operando_aux
        elif linea[0] == 'multiplica':
            operando_aux = 1
            for operado in operandos:
                producto = Calc_Hija.multiplicacion(operando_aux, int(operado))
                operando_aux = producto
        elif linea[0] == 'divide':
            try:
                operando_aux = int(operandos[0])
                for operando in operandos[1:]:
                    operando_aux = Calc_Hija.division(operando_aux,
                                                      int(operando))
                    razon = operando_aux
            except ZeroDivisionError:
                sys.exit('Division by zero is not allowed')

        else:
            print('No se puede realizar la operacion')

print("Suma = " + str(suma))
print("Resta = " + str(resta))
print("Multiplicacion = " + str(producto))
print("Division = " + str(razon))
