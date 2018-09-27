#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from calcoo import Calculadora


class CalculadoraHija(Calculadora):
    def multiplicacion(self, op1, op2):

        return op1 * op2

    def division(self, op1, op2):

        return op1 / op2


Calc_Hija = CalculadoraHija()

if __name__ == "__main__":
    try:
        operando1 = int(sys.argv[1])
        operando2 = int(sys.argv[3])
    except ValueError:
        sys.exit("Error: Non numerical parameters")

    if sys.argv[2] == "suma":
        result = Calc_Hija.plus(operando1, operando2)
    elif sys.argv[2] == "resta":
        result = Calc_Hija.minus(operando1, operando2)
    elif sys.argv[2] == "multiplicacion":
        result = Calc_Hija.multiplicacion(operando1, operando2)
    elif sys.argv[2] == "division":
        if sys.argv[3] == "0":
            sys.exit('Division by zero is not allowed')
        else:
            result = Calc_Hija.division(operando1, operando2)
    else:
        sys.exit('Operación no soportada')

    print(result)
