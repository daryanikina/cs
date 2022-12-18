R, N, L = 1, 0, -1 #сдвиги
lnt = list(input())
state = 'q0'
i = 0
 
states = {
    'q0':{'a': ['a', R, 'q1'], 'b': ['b', R, 'q0'], 'c' :['c', R, 'q0'], ' ': [' ', R, 'q0']},
    'q1':{'a': ['a', L, 'qaL'], 'b': ['b', L, 'qbL'], 'c': ['c', L, 'qcL'], ' ': [' ', L, 'qaL']},
    'qaL':{'a':['a', L, 'qaL'], 'b': ['b', L, 'qaL'], 'c': ['c', L, 'qaL'], ' ': [' ', R, 'qaR']},
    'qbL':{'a':['a', L, 'qbL'], 'b': ['b', L, 'qbL'], 'c': ['c', L, 'qbL'], ' ': [' ', R, 'qbR']},
    'qcL':{'a':['a', L, 'qcL'], 'b': ['b', L, 'qcL'], 'c': ['c', L, 'qcL'], ' ': [' ', R, 'qcR']},
    'qaR':{'a':['a', R, 'qaR'], 'b': ['b', R, 'qaR'], 'c': ['c', L, 'qac'], ' ':[' ', N, 'q2']},
    'qbR':{'a':['a', R, 'qbR'], 'b': ['b', R, 'qbR'], 'c': ['c', L, 'qbc'], ' ':[' ', N, 'q2']},
    'qcR':{'a':['a', R, 'qcR'], 'b': ['b', R, 'qcR'], 'c': ['c', L, 'qcc'], ' ':[' ', N, 'q2']},
    'qac':{'a':['a', N, 'q2'], 'b':['a', N, 'q2'], 'c': ['a', N, 'q2'], ' ':['a', N, 'q2']},
    'qbc':{'a':['b', N, 'q2'], 'b':['b', N, 'q2'], 'c': ['b', N, 'q2'], ' ':['b', N, 'q2']},
    'qcc':{'a':['c', N, 'q2'], 'b':['c', N, 'q2'], 'c': ['c', N, 'q2'], ' ':['c', N, 'q2']}
}
 
while state != 'q2':
    s = lnt[i]
    print(state)
    s2 = states[state][s]
    lnt[i] = s2[0]
    i += s2[1]
    state = s2[2]
print(*lnt, sep='')
