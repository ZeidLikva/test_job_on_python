# -*- coding: UTF-8 -*-
from sys import argv
import sys

def itoBase(nb, from_base=None, to_base=None):
    if to_base == None:
        base = str(from_base)
        baseDst = len(base)
        nb = int(nb)
        if nb >= baseDst:
            return itoBase(nb/baseDst, base) + base[nb % baseDst]
        else:
            return base[nb]
    else:
        baseSrc = len(from_base)
        grade = len(nb)
        nb_decimal = 0
        for i in range(grade):
            j = 0
            while nb[i] != from_base[j]:
                j+=1
            nb_decimal = nb_decimal + j*pow(baseSrc, (grade-i-1))
        return itoBase(nb_decimal, to_base)

def main(argv):
    if len(argv) == 2:
        nb = argv[0]
        base = argv[1]
        if nb.isdecimal() == False:
            print("Задано не десятичное число\nИспользуйте ввод типа\npython task1.py nb 01234567\nгде nb - десятичное число для конвертации\n01234567 - система счисления, в которую конвертируем")
        else:
            print(itoBase(nb, base))
    elif len(argv) == 3:
        nb = argv[0]
        from_base = argv[1]
        to_base = argv[2]
        for i in range(0, len(nb)):
            if nb[i] not in from_base:
                print("Число не в заданной системе счисления\nИспользуйте ввод типа\npython task1.py nb 01234567 0123456789abcdef\nгде nb - число для конвертации\n01234567 - система счисления, из которой конвертируем\n0123456789abcdef - система счисления, в которую конвертируем")
                return
        print(itoBase(nb, from_base, to_base))
    else:
        print("Используйте ввод типа\npython task1.py nb 01234567 0123456789abcdef\nгде nb - число для конвертации\n01234567 - система счисления, из которой конвертируем\n0123456789abcdef - система счисления, в которую конвертируем\nИли\npython task1.py nb 01234567\nгде nb - десятичное число для конвертации\n01234567 - система счисления, в которую конвертируем")

main(sys.argv[1:])
