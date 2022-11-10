import numpy as np


def check_crossroad(robot, point1, point2, point3, point4):
    if robot[0] >= point1[0] and robot[0] <= point3[0]\
            and robot[1] >= point2[1] and robot[1] <= point4[1]:
        return True
    else:
        return False


def check_collision(coefficients):
    N = coefficients.shape[0]
    result = []
    for i in range(N):
        for j in range(i+1, N):
            AB = np.array([coefficients[i][:2], coefficients[j][:2]])
            C = np.array([[coefficients[i][2]],[coefficients[j][2]]])
            ABC = np.hstack((AB, C))
            rank_AB = np.linalg.matrix_rank(AB)
            rank_ABC = np.linalg.matrix_rank(ABC)
            if rank_AB == rank_ABC:
                result.append((i, j))
                result.append((j, i))
    result = sorted(result)
    return (result)


def check_path(points_list):
    result = 0.0
    for i in range(len(points_list) - 1):
        A = np.array(points_list[i])
        B = np.array(points_list[i+1])
        result += np.linalg.norm(B - A, ord=2)
    return (np.round(result, 2))