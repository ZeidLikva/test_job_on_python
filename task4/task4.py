# -*- coding: UTF-8 -*-
from sys import argv
import sys

def compare_str(str1, str2):
    j = 0
    i = 0
    while i != (len(str2)-1):
        while (str2[i] == '*'):
            if i != (len(str2)-1):
                i += 1
                continue
            else:
                return 'OK'
        if (str1[j] != str2[i]):
            return 'KO'
        if ((j == (len(str1)-1)) and ((i != (len(str2)-1)) and (str2[i+1] != '*'))) or ((j != (len(str1)-1)) and (i == (len(str2)-1))):
            return 'KO'
        if j != (len(str1)-1):
            j += 1
        i += 1
    return 'OK'


def main(argv):
    if len(argv) == 2:
        str1 = argv[0]
        str2 = argv[1]
        print(f'{compare_str(str1, str2)}\n')
    else:
        print("Неверный ввод. Используйте ввод типа\npython task4.py str1 str2\nгде\nstr1 - первая строка\nstr2 - вторая строка\n")

main(sys.argv[1:])