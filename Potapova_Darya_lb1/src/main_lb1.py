import numpy as np


def check_crossroad(robot, point1, point2, point3, point4):
    x, y = robot[0], robot[1]
    x1, y1 = point1[0], point1[1]
    x2, y2 = point2[0], point2[1]
    x3, y3 = point3[0], point3[1]
    x4, y4 = point4[0], point4[1]
    return ((x1 <= x <= x2) and (y1 <= y <= y4))


def check_collision(coefficients):
    rez = []
    for i in range(0, len(coefficients)):
        for j in range(i + 1, len(coefficients)):
            mat1 = np.array([coefficients[i][:2], coefficients[j][:2]])
            coefficients[i][2] = coefficients[i][2] * (-1)
            coefficients[j][2] = coefficients[j][2] * (-1)
            mat2 = np.array([coefficients[i], coefficients[j]])
            if np.linalg.matrix_rank(mat1) == np.linalg.matrix_rank(mat2):
                rez.append((i, j))
                rez.append((j, i))
    return sorted(rez)


def check_path(points_list):
    rez = 0
    for i in range(0, len(points_list) - 1):
        s1 = np.array(points_list[i])
        s2 = np.array(points_list[i + 1])
        rez += np.linalg.norm(s2 - s1, ord=2)
    return round(rez, 2)

