import numpy as np
from numpy import linalg as LA


def check_collision(bot1: np.ndarray, bot2: np.ndarray) -> tuple:
    mx = np.matrix((bot1[0:2],
                    bot2[0:2]))
    arr = -np.array((bot1[2], bot2[2]))
    solve = LA.solve(mx, arr)
    return tuple(np.round(solve, 2))


def check_surface(point1: np.ndarray, point2: np.ndarray, point3: np.ndarray) -> np.ndarray:
    mx = np.matrix((point1[0:2],
                    point2[0:2],
                    point3[0:2]))
    mx = np.hstack((mx, np.ones((3, 1))))
    arr = np.array((point1[2], point2[2], point3[2]))
    try:
        return np.round(LA.solve(mx, arr), 2)
    except LA.LinAlgError: # matrix is Singular
        return None


def check_rotation(vec: np.ndarray, rad: float) -> np.ndarray:
    # Create rotation_matrix
    cos, sin = np.cos(rad), np.sin(rad)
    rotation_matrix = np.matrix([[cos, -sin, 0],
                                 [sin, cos, 0],
                                 [0, 0, 1]])

    return np.round(np.dot(rotation_matrix, vec), 2)[0]  # Just np.dot return matrix
