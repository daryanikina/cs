lenta = list(input())

tur = { 'q0': {'a': ['a', 1, 'q1'], 'b': ['b', 1, 'q0'], 'c' :['c', 1, 'q0'], ' ': [' ', 1, 'q0']},
        'q1': {'a': ['a', -1, 'qa-'], 'b': ['b', -1, 'qb-'], 'c': ['c', -1, 'qc-'], ' ': [' ', -1, 'qa-']},
        'qa-': {'a':['a', -1, 'qa-'], 'b': ['b', -1, 'qa-'], 'c': ['c', -1, 'qa-'], ' ': [' ', 1, 'qa+']},
        'qa+': {'a':['a', 1, 'qa+'], 'b': ['b', 1, 'qa+'], 'c': ['c', -1, 'qaw'], ' ':[' ', 0, 'qend']},
        'qaw': {'a':['a', 0, 'qend'], 'b':['a', 0, 'qend'], 'c': ['a', 0, 'qend'], ' ':['a', 0, 'qend']},
        'qb-':{'a':['a', -1, 'qb-'], 'b': ['b', -1, 'qb-'], 'c': ['c', -1, 'qb-'], ' ': [' ', 1, 'qb+']},
        'qb+':{'a':['a', 1, 'qb+'], 'b': ['b', 1, 'qb+'], 'c': ['c', -1, 'qbw'], ' ':[' ', 0, 'qend']},
        'qbw':{'a':['b', 0, 'qend'], 'b':['b', 0, 'qend'], 'c': ['b', 0, 'qend'], ' ':['b', 0, 'qend']},
        'qc-':{'a':['a', -1, 'qc-'], 'b': ['b', -1, 'qc-'], 'c': ['c', -1, 'qc-'], ' ': [' ', 1, 'qc+']},
        'qc+':{'a':['a', 1, 'qc+'], 'b': ['b', 1, 'qc+'], 'c': ['c', -1, 'qcw'], ' ':[' ', 0, 'qend']},
        'qcw':{'a':['c', 0, 'qend'], 'b':['c', 0, 'qend'], 'c': ['c', 0, 'qend'], ' ':['c', 0, 'qend']}
        }

sost = 'q0'
i=0
move = 0
write = ''

cond_mass = ['q0']


while(sost != 'qend'):
    symbol, direction, sost = tur[sost][lenta[i]]
    lenta[i] = symbol
    i += direction
    cond_mass.append(sost)

print("".join(lenta))
print(*cond_mass)
