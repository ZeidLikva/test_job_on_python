import math
import sys
import re

class Sphere():
    def __init__(self, parameters):
        center = re.search(r'center: [-]?\[\d*[.]?\d*, [-]?\d*[.]?\d*, [-]?\d*[.]?\d*]', parameters).group()
        radius = re.search(r'radius: \d*[.]?\d*', parameters).group()
        center = re.findall(r'[-]?\d+[.]?\d*', center)
        self.center = [float(item) for item in center]
        self.radius = float(re.search(r'\d+[.]?\d*', radius).group())

class Line():
    def __init__(self, parameters):
        block = re.search(r'\{\[[-]?\d+[.]?\d*, [-]?\d+[.]?\d*, [-]?\d+[.]?\d*\], [-]?\[\d+[.]?\d*, [-]?\d+[.]?\d*, [-]?\d+[.]?\d*\]', parameters).group()
        dots = re.findall(r'[-]?\d+[.]?\d*', block)
        dot1 = dots[:-3]
        dot2 = dots[3:]
        self.dot1 = [float(item) for item in dot1]
        self.dot2 = [float(item) for item in dot2]

def get_collision(sphere_center, sphere_ragius, dot1, dot2):
    a = math.pow((dot1[0] - dot2[0]), 2) + math.pow((dot1[1] - dot2[1]), 2) + math.pow((dot1[2] - dot2[2]), 2)
    b = 2*((sphere_center[0] - dot1[0])*(dot1[0] - dot2[0]) + (sphere_center[1] - dot1[1])*(dot1[1] - dot2[1]) + (sphere_center[2] - dot1[2])*(dot1[2] - dot2[2]))
    c = math.pow((dot1[0] - sphere_center[0]), 2) + math.pow((dot1[0] - sphere_center[0]), 2) + math.pow((dot1[0] - sphere_center[0]), 2) - math.pow(sphere_ragius, 2)
    D = math.pow(b, 2) - 4*a*c
    if D < 0:
        print("Коллизий не найдено\n")
    if D == 0:
        t = -b / (2*a)
        x = dot1[0] + t*(dot2[0] - dot1[0])
        y = dot1[1] + t*(dot2[1] - dot1[1])
        z = dot1[2] + t*(dot2[2] - dot1[2])
        collision = [x, y, z]
        print(f'{collision}\n')
    if D > 0:
        t1 = -(b + math.sqrt(D))/(2*a)
        t2 = -(b - math.sqrt(D))/(2*a)
        x1 = dot1[0] + t1*(dot2[0] - dot1[0])
        y1 = dot1[1] + t1*(dot2[1] - dot1[1])
        z1 = dot1[2] + t1*(dot2[2] - dot1[2])
        collision1 = [x1, y1, z1]
        x2 = dot1[0] + t2*(dot2[0] - dot1[0])
        y2 = dot1[1] + t2*(dot2[1] - dot1[1])
        z2 = dot1[2] + t2*(dot2[2] - dot1[2])
        collision2 = [x2, y2, z2]
        print(f'{collision1}\n{collision2}\n')

def main(argv):
    if argv.__len__() == 1:
        f = open(argv[0])
        parameters = f.read()
        sphere = Sphere(parameters)
        line = Line(parameters)
        f.close()
        get_collision(sphere.center, sphere.radius, line.dot1, line.dot2)
    else:
        print("Файл не найден\nИспользуйте ввод типа\npython task2.py ./coordinates.txt\nгде ./coordinates.txt - файл с координатами")

main(sys.argv[1:])