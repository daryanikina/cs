R, N, L = 1, 0, -1
table = {
    "start": {'a': ['a', N, "find_b"], 'b' : ['b', N, "find_b"], 'c' : ['c', N, "find_b"], ' ' : [' ', R, "start"]},
    "find_b" : {'a': ['a', R, "find_b"], 'b' : ['b', R, "first_letter"], 'c' : ['c', R, "find_b"], ' ' : [' ', L, "none_b"]},
    "none_b" : {'a': ['a', L, "none_b"], 'c' : ['c', L, "none_b"], ' ' : [' ', R, "delete_symbol"]},
    "delete_symbol" : {'a': [' ', N, "end"], 'b' : [' ', N, "end"], 'c' : [' ', N, "end"], ' ' : [' ', N, "end"]},
    "first_letter" : {'a': ['a', R, "second_letter"], 'b' : ['b', R, "second_letter"], 'c' : ['c', R, "second_letter"], ' ' : [' ', L, "delete_symbol"]},
    "second_letter" : {'a': ['a', R, "third_letter"], 'b' : ['b', R, "third_letter"], 'c' : ['c', R, "third_letter"], ' ' : [' ', L, "delete_symbol"]},
    "third_letter" : {'a': ['a', L, "A"], 'b' : ['b', L, "B"], 'c' : ['c', L, "C"], ' ' : [' ', L, "delete_s"]},
    "A" : {'a': ['a', L, "A1"], 'b' : ['b', L, "A1"], 'c' : ['c', L, "A1"]},
    "A1" : {'a': ['a', R, "first_letter"], 'b' : ['a', R, "first_letter"], 'c' : ['a', R, "first_letter"]},
    "B" : {'a': ['a', L, "B1"], 'b' : ['b', L, "B1"], 'c' : ['c', L, "B1"]},
    "B1" : {'a': ['b', R, "first_letter"], 'b' : ['b', R, "first_letter"], 'c' : ['b', R, "first_letter"]},
    "C" : {'a': ['a', L, "C1"], 'b' : ['b', L, "C1"], 'c' : ['c', L, "C1"]},
    "C1" : {'a': ['c', R, "first_letter"], 'b' : ['c', R, "first_letter"], 'c' : ['c', R, "first_letter"]},
    "delete_s" : {'a': [' ', L, "delete_symbol"], 'b' : [' ', L, "delete_symbol"], 'c' : [' ', L, "delete_symbol"]}
}
tape = list(input())
state = "start"
ind = 0
while state != "end":
    symbol = tape[ind];
    tape[ind] = table[state][symbol][0]
    ind += table[state][symbol][1]
    state = table[state][symbol][2]
print("".join(tape))
