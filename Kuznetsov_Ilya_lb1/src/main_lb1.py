import numpy as np


def len_way(a, b):
    delt_x = a[0] - b[0]
    delt_y = a[1] - b[1]
    return ((delt_x ** 2 + delt_y ** 2) ** (0.5))


def check_crossroad(robot, point1, point2, point3, point4):
    if (point3[0] >= robot[0] >= point1[0]) and (point4[1] >= robot[1] >= point2[1]):
        return True
    return False


def check_collision(coefficients):
    ans = []
    for i in range(len(coefficients)):
        for j in range(i + 1, len(coefficients)):
            matrix = np.array([[coefficients[i][0], coefficients[i][1]], [coefficients[j][0], coefficients[j][1]]])
            b = np.array([[coefficients[i][2]], [coefficients[j][2]]])
            rang1 = np.linalg.matrix_rank(matrix)
            matrix = np.hstack((matrix, b))
            rang2 = np.linalg.matrix_rank(matrix)
            if rang1 == rang2:
                ans.append((i, j))
                ans.append((j, i))
    return sorted(ans)


def check_path(points_list):
    way = 0
    for i in range(len(points_list) - 1):
        way += len_way(points_list[i + 1], points_list[i])
    return round(way, 2)

