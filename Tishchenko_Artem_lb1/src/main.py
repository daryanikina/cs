import numpy as np


def check_crossroad(robot, point1, point2, point3, point4) -> bool:
    r, p1, p3 = map(np.array, [robot, point1, point3])
    vec1, vec2 = (r - p1) >= 0, (p3 - r) >= 0
    return bool(np.prod(vec1) and np.prod(vec2))


def check_collision(coefficients) -> list:
    ans = []
    for i in range(len(coefficients)):
        for j in range(i + 1, len(coefficients)):
            eq1 = np.array(coefficients[i][:2])
            eq2 = np.array(coefficients[j][:2])
            if np.linalg.det(np.vstack((eq1, eq2))):
                ans.append((i, j))
                ans.append((j, i))
    return ans


def check_path(points_list) -> float:
    path = 0
    for i in range(1, len(points_list)):
        vec1, vec2 = np.array(points_list[i - 1]), np.array(points_list[i])
        path += np.linalg.norm(vec2 - vec1, ord=2)
    return round(path, 2)
