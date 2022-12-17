L, N, R = -1, 0, +1

alphabet = {
    'a': 0, 'b': 1, 'c': 2, ' ': 3
}

states = {
    # Начальное состояние
    'q0': {
        'write': ['a', ' ', ' ', ' '],
        'move': [R, R, R, R],
        'nextState': ['q1', 'q2', 'q3', 'q0']
    },

    # Получение последней буквы
    'q1': {
        'write': ['a', 'b', 'c', ' '],
        'move': [R, R, R, R],
        'nextState': ['q1', 'q2', 'q3', 'q7']
    },
    'q2': {
        'write': ['a', 'b', 'c', ' '],
        'move': [R, R, R, R],
        'nextState': ['q1', 'q2', 'q3', 'q8']
    },
    'q3': {
        'write': ['a', 'b', 'c', ' '],
        'move': [R, R, R, R],
        'nextState': ['q1', 'q2', 'q3', 'q9']
    },

    # Перемещение к началу второго слова
    'q4': {
        'write': ['a', 'b', 'c', ' '],
        'move': [L, L, L, L],
        'nextState': ['q4', 'q4', 'q4', 'q5']
    },

    # Возврат на первое слово и удаление последней буквы
    'q5': {
        'write': [' ', ' ', ' ', ' '],
        'move': [L, L, L, L],
        'nextState': ['q6', 'q6', 'q6', 'q5']
    },

    # Перенаправление на путь к новому слову
    'q6': {
        'write': ['a', 'b', 'c', ' '],
        'move': [R, R, R, N],
        'nextState': ['q10', 'q11', 'q12', 'q13']
    },

    # Запись буквы в новое слово
    'q7': {
        'write': ['a', 'b', 'c', 'a'],
        'move': [R, R, R, L],
        'nextState': ['q7', 'q7', 'q7', 'q4']
    },
    'q8': {
        'write': ['a', 'b', 'c', 'b'],
        'move': [R, R, R, L],
        'nextState': ['q8', 'q8', 'q8', 'q4']
    },
    'q9': {
        'write': ['a', 'b', 'c', 'c'],
        'move': [R, R, R, L],
        'nextState': ['q9', 'q9', 'q9', 'q4']
    },

    # Перемещение к концу второго слова
    'q10': {
        'write': ['a', 'b', 'c', ' '],
        'move': [R, R, R, R],
        'nextState': ['q7', 'q7', 'q7', 'q10']
    },
    'q11': {
        'write': ['a', 'b', 'c', ' '],
        'move': [R, R, R, R],
        'nextState': ['q8', 'q8', 'q8', 'q11']
    },
    'q12': {
        'write': ['a', 'b', 'c', ' '],
        'move': [R, R, R, R],
        'nextState': ['q9', 'q9', 'q9', 'q12']
    },
}

if __name__ == '__main__':
    tape = list(input())
    tape += ((len(tape) + 2) * ' ')

    state = 'q0'
    index = 0
    while state != 'q13':
        oldValue = tape[index]

        tape[index] = states[state]['write'][alphabet[oldValue]]
        index += states[state]['move'][alphabet[oldValue]]
        state = states[state]['nextState'][alphabet[oldValue]]

    print(''.join(tape))
