# -*- coding: UTF-8 -*-
import csv
import codecs
from sys import argv
import sys
import datetime
import re

class Barrel():
    def __init__(self, log, time1, time2):
        self.time1 = datetime.datetime.strptime(time1, '%Y-%m-%dT%H:%M:%S')
        self.time2 = datetime.datetime.strptime(time2, '%Y-%m-%dT%H:%M:%S')
        f = codecs.open(log, "r", "utf-8")
        text = f.read()
        lines = re.split('\r\n', text)
        self.log = lines[3:]
        self.start_value = int(re.compile(r'\d*').findall(lines[2])[0])
        f.close()

def check_log(log, start_value, time1, time2):
    nbr_tries_top_up = 0
    nbr_fail_top_up = 0
    value_top_up = 0
    value_not_top_up = 0
    nbr_tries_scoop = 0
    nbr_fail_scoop = 0
    value_scoop = 0
    value_not_scoop = 0
    end_value = 0
    for i in range(log.__len__()-1):
        line = re.split(' - ', log[i])
        date = datetime.datetime.strptime(line[0], '%Y-%m-%dT%H:%M:%S.%fZ')
        value = int(re.findall(r'\d*', re.split('l', re.split(' - ', log[i])[2])[0])[-2])
        if date < time1:
            if ('top up' and 'успех') in line[2]:
                start_value = start_value + value
            if ('успех' and 'scoop') in line[2]:
                start_value = start_value - value
        if (date >= time1) and (date <= time2):
            if 'top up' in line[2]:
                nbr_tries_top_up +=1
                if 'успех' in line[2]:
                    value_top_up = value_top_up + value
                else:
                    nbr_fail_top_up +=1
                    value_not_top_up = value_not_top_up + value
            if 'scoop' in line[2]:
                nbr_tries_scoop +=1
                if 'успех' in line[2]:
                    value_scoop = value_scoop + value
                else:
                    nbr_fail_scoop +=1
                    value_not_scoop = value_not_scoop + value
        if date > time2:
            if nbr_tries_top_up == 0 and nbr_tries_scoop == 0:
                return "Выбранный период не найден в файле"
            end_value = start_value + value_top_up - value_scoop
            prc_fails_top_up = int(nbr_fail_top_up / nbr_tries_top_up * 100)
            prc_fails_scoop = int(nbr_fail_scoop / nbr_tries_scoop * 100)
            statistic = [nbr_tries_top_up, prc_fails_top_up, value_top_up, value_not_top_up, nbr_tries_scoop, prc_fails_scoop, value_scoop, value_not_scoop, start_value, end_value]
            return statistic 

def write_to_csv(statistic):
    with open('log.csv', "w", newline="") as file:
        fieldnames = ['Attempt of top up', 'Procent of failing top up', 'Value top up', 'Value not top up', 'Attempts of scoop', 'Procent of failing scoop', 'Value scoop', 'Value not scoop', 'Value in the start of period', 'Value in the end of period']
        writer = csv.writer(file, dialect=csv.excel)
        writer.writerow(fieldnames)
        writer.writerow(statistic)

def main(argv):
    if argv.__len__() == 3:
        log = argv[0]
        time1 = argv[1]
        time2 = argv[2]
        barrel = Barrel(log, time1, time2)
        statistic = check_log(barrel.log, barrel.start_value, barrel.time1, barrel.time2)
        if statistic == "Выбранный период не найден в файле":
            print(f'{statistic}\n')
            return
        write_to_csv(statistic)
    else:
        print("Неверный ввод. Используйте ввод типа\npython task3.py ./log.log 2020-01-01T12:30:00 2020-01-01T13:00:00\nгде\n./log.log - путь к файлу лога\n2020-01-01T12:30:00 - начальная точка временного интервала\n2020-01-01T13:00:00 - его конечная точка\n")

main(sys.argv[1:])