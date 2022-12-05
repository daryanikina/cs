R, N, L = 1, 0, -1
table = {
    "start": {'a': ['a', R, "found_a"], 'c': ['c', R, "found_c"], ' ': [' ', R, "start"], 'b': ['b', R, "start"]},
    "found_a": {"a": ["a",L,"found_a_a"], "b" : ['b',L,"found_a_b"], 'c': ['c', L, "found_a_c"]},
    "found_a_c": {"a": ["c",N,"end"], "b" : ['c',N,"end"], ' ': ['c', N, "end"], 'c': ['c', N, "end"]},
    "found_a_b": {"a": ["a",R,"found_a_b"], "b" : ['b',R,"found_a_b"], ' ': [' ', R, "found_a_b"], 'c': ['c', L, "found_a_b_c"]},
    "found_a_a": {"a": ["a",R,"found_a_a"], "b" : ['b',R,"found_a_a"], ' ': [' ', R, "found_a_a"], 'c': ['c', L, "found_a_a_c"]},
    "found_a_b_c": {"a": ["b",N,"end"], "b" : ['b',N,"end"], ' ': ['b', N, "end"], 'c': ['b', N, "end"]},
    "found_a_a_c": {"a": ["a",N,"end"], "b" : ['a',N,"end"], ' ': ['a', N, "end"], 'c': ['a', N, "end"]},
    "found_c": {"a": ["a",R,"found_c_a"], "b" : ['b',R,"found_c"], ' ': [' ', R, "found_c"], 'c': ['c', R, "found_c"]},
    "found_c_a": {"a": ["a",L,"found_c_a_a"], "b" : ['b',L,"found_c_a_b"], ' ': [' ', L, "found_c_a_a"], 'c': ['c', L, "found_c_a_c"]},
    "found_c_a_b": {"a": ["a",L,"found_c_a_b"], "b" : ['b',L,"found_c_a_b"], ' ': [' ', L, "found_c_a_b_start"], 'c': ['c', L, "found_c_a_b"]},
    "found_c_a_c": {"a": ["a",L,"found_c_a_c"], "b" : ['b',L,"found_c_a_c"], ' ': [' ', L, "found_c_a_c_start"], 'c': ['c', L, "found_c_a_c"]},
    "found_c_a_a": {"a": ["a",L,"found_c_a_a"], "b" : ['b',L,"found_c_a_a"], ' ': [' ', L, "found_c_a_a_start"], 'c': ['c', L, "found_c_a_a"]},
    "found_c_a_b_start": {"a": ["a",R,"found_c_a_b_start"], "b" : ['b',R,"found_c_a_b_start"], ' ': [' ', R, "found_c_a_b_start"], 'c': ['c', L, "found_c_a_b_start_c"]},
    "found_c_a_a_start": {"a": ["a",R,"found_c_a_a_start"], "b" : ['b',R,"found_c_a_a_start"], ' ': [' ', R, "found_c_a_a_start"], 'c': ['c', L, "found_c_a_a_start_c"]},
    "found_c_a_c_start": {"a": ["a",R,"found_c_a_c_start"], "b" : ['b',R,"found_c_a_c_start"], ' ': [' ', R, "found_c_a_c_start"], 'c': ['c', L, "found_c_a_c_start_c"]},
    "found_c_a_c_start_c": {"a": ["c",N,"end"], "b" : ['c',N,"end"], ' ': ['c', N, "end"], 'c': ['c', N, "end"]},
    "found_c_a_a_start_c": {"a": ["a",N,"end"], "b" : ['a',N,"end"], ' ': ['a', N, "end"], 'c': ['a', N, "end"]},
    "found_c_a_b_start_c": {"a": ["b",N,"end"], "b" : ['b',N,"end"], ' ': ['b', N, "end"], 'c': ['b', N, "end"]},
}
mem = list(input())
state = "start"
ind = 0
while state != "end":
    symbol = mem[ind]
    next_s = table[state][symbol]
    mem[ind] = next_s[0]
    ind += next_s[1]
    state = next_s[2]
print(*mem, sep='')