def turing(tape):
    table = {
        # Find a word
        'q1': {
            ' ': [' ', 1, 'q1'],
            'a': ['a', 1, 'q2'],
            'b': ['b', 1, 'q2'],
            'c': ['c', 1, 'q2']
        },
        # Go to the end of word
        'q2': {
            ' ': [' ', -1, 'q3'],
            'a': ['a', 1, 'q2'],
            'b': ['b', 1, 'q2'],
            'c': ['c', 1, 'q2']
        },
        # Find one 'a'
        'q3': {
            'a': ['a', -1, 'q4'],
            'b': ['b', -1, 'q3'],
            'c': ['c', -1, 'q3']
        },
        # Find the last couple of 'a' in a row
        'q4': {
            'a': ['a', -1, 'q5'],
            'b': ['b', -1, 'q3'],
            'c': ['c', -1, 'q3']
        },
        # Branching: Define a replacement character
        'q5': {
            'a': ['a', 1, 'q6'],
            'b': ['b', 1, 'q9'],
            'c': ['c', 1, 'q12']
        },
        # Branch of 'a':
        # Go back
        'q6': {
            'a': ['a', 1, 'q7']
        },
        'q7': {
            'a': ['a', 1, 'q8']
        },
        # Replace with 'a'
        'q8': {
            'a': ['a', 0, 'q0'],
            'b': ['a', 0, 'q0'],
            'c': ['a', 0, 'q0'],
            ' ': ['a', 0, 'q0']
        },
        # Branch of 'b':
        # Go back
        'q9': {
            'a': ['a', 1, 'q10']
        },
        'q10': {
            'a': ['a', 1, 'q11']
        },
        # Replace with 'b'
        'q11': {
            'a': ['b', 0, 'q0'],
            'b': ['b', 0, 'q0'],
            'c': ['b', 0, 'q0'],
            ' ': ['b', 0, 'q0']
        },
        # Branch of 'c':
        # Go back
        'q12': {
            'a': ['a', 1, 'q13']
        },
        'q13': {
            'a': ['a', 1, 'q14']
        },
        # Replace with 'c'
        'q14': {
            'a': ['c', 0, 'q0'],
            'b': ['c', 0, 'q0'],
            'c': ['c', 0, 'q0'],
            ' ': ['c', 0, 'q0']
        },
    }
    state = 'q1'
    i = 0
    while state != 'q0':
        tape[i], move, state = table[state][tape[i]]
        i += move


if __name__ == '__main__':
    tape = list(input())
    turing(tape)
    print(''.join(tape))
