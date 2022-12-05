import numpy as np

def check_crossroad(robot, point1, point2, point3, point4):
    xfirst = max(point1[0], point2[0], point3[0])
    xsecond = min(point1[0], point2[0], point3[0])
    yfirst = max(point1[1], point2[1], point3[1])
    ysecond = min(point1[1], point2[1], point3[1])
    x, y = robot
    return  xfirst >= x >= xsecond and  yfirst >= y >=ysecond

def check(a):
    return np.linalg.matrix_rank(a) == 2

def check_collision(coefficients):
    clsins = []
    for i in range(len(coefficients)):
        tmp = coefficients[i][:2]
        for j in range(i, len(coefficients)):
            if check(np.vstack((tmp, coefficients[j][:2]))):
                clsins.append((i, j))
    return clsins


def check_path(points_list):
    points_list = np.array(points_list)
    length = 0
    for i in range(len(points_list) - 1):
        length += np.linalg.norm((points_list[i] - points_list[i+1]))
    return round(length, 2)
