import numpy as np


def check_collision(bot1, bot2):
    matrix_a = np.array([[bot1[0], bot1[1]], [bot2[0], bot2[1]]])
    vector_b = np.array([-bot1[2], -bot2[2]])
    if np.linalg.matrix_rank(matrix_a) != 2:
        return None
    else:
        array = np.linalg.solve(matrix_a, vector_b)
        array = np.around(array, decimals = 2)
        result = tuple(result)
        return result


def check_surface(point1, point2, point3):
    matrix_a = np.array([[point1[0], point1[1], 1],[point2[0], point2[1], 1], [point3[0], point3[1], 1]])
    vector_b = np.array([point1[2], point2[2], point3[2]])
    if np.linalg.matrix_rank(matrix_a) != 3:
        return None
    else:
        result = np.linalg.solve(matrix_a, vector_b)
        result = np.around(result, decimals = 2)
        return result

def check_rotation(vec, rad):
    matrix = np.array([[np.cos(rad), -np.sin(rad), 0], [np.sin(rad), np.cos(rad), 0], [0, 0, 1]])
    result = matrix.dot(vec)
    result = np.around(result, decimals = 2)
    return result
