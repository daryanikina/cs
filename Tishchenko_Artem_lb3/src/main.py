R = +1
L = -1
N = 0

table = {
'q0': {'a': ('a', R, 'q1'), 'b': ('b', R, 'q2'), 'c': ('c', R, 'q1'),   ' ': (' ', R, 'q0')},
'q1': {'a': ('a', R, 'q1'), 'b': ('b', R, 'q2'), 'c': ('c', R, 'q1'),   ' ': (' ', L, 'q4')},
'q2': {'a': (' ', R, 'q3'), 'b': (' ', R, 'q3'), 'c': (' ', R, 'q3'),   ' ': (' ', L, 'q6')},
'q3': {'a': (' ', R, 'q7'), 'b': (' ', R, 'q7'), 'c': (' ', R, 'q7'),   ' ': (' ', N, 'ex')},
'q4': {'a': ('a', L, 'q4'),                      'c': ('c', L, 'q4'),   ' ': (' ', R, 'q5')},
'q5': {'a': (' ', N, 'ex'),                      'c': (' ', N, 'ex'),},
'q6': {                     'b': (' ', N, 'ex'),},
'q7': {'a': (' ', L, 'q8'), 'b': (' ', L, 'q12'), 'c': (' ', L, 'q14'), ' ': (' ', N, 'ex')},
'q8': {                                                                 ' ': (' ', L, 'q9')},
'q9': {                                                                 ' ': ('a', R, 'q10')},
'q10': {                                                                ' ': (' ', R, 'q11')},
'q11': {                                                                ' ': (' ', R, 'q7')},
'q12': {                                                                ' ': (' ', L, 'q13')},
'q13': {                                                                ' ': ('b', R, 'q10')},
'q14': {                                                                ' ': (' ', L, 'q15')},
'q15': {                                                                ' ': ('c', R, 'q10')},
'ex': 'exit'
}

def turing(program: dict, tape: list, start: str) -> (list, str):
    cell = 0
    state = start
    res = ''
    while True:
        res += state + ' '
        rows = program[state]
        if rows == 'exit': break
        cur_row = rows[tape[cell]]
        tape[cell] = cur_row[0]
        cell += cur_row[1]
        state = cur_row[2]
    return tape, res



print(*turing(table, list(input()), 'q0')[0], sep='')
