import numpy

# вспомогательная функция для округления элементов numpy-массива
def round_matrix(array):
    result = numpy.array(list(map(lambda x: round(x, 2), array)))
    return result

# вспомогательная функция для решения системы линейных уравнений
def solve(*arrays):
    matrix = numpy.array(arrays)
    coefficients = matrix[:, :-1]
    free_terms = matrix[:, -1]
    try:
        solvetion = numpy.linalg.solve(coefficients, free_terms)
        result = round_matrix(solvetion)
    except numpy.linalg.LinAlgError:
        result = None
    return result 

def check_collision(bot1, bot2):
    result = solve(bot1, bot2)
    if type(result) != type(None):
        result = tuple(-result)
    return result

def check_surface(point1, point2, point3):
    return solve(numpy.insert(point1, 2, 1),
                 numpy.insert(point2, 2, 1),
                 numpy.insert(point3, 2, 1))

def check_rotation(position, angle):
    position_x_y = position[:-1]
    rotation_matrix = numpy.array([[numpy.cos(angle), -numpy.sin(angle)],
                                   [numpy.sin(angle), numpy.cos(angle)]])
    new_position_x_y = numpy.matmul(rotation_matrix, position_x_y)
    new_position_x_y = round_matrix(new_position_x_y)
    new_position = numpy.hstack([new_position_x_y, position[-1]])
    return new_position

