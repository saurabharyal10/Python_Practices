subjects = [
    'Account',
    'Science',
    'Math'
    ]

sub_code = [
    52,
    38,
    21
]

weight = [
    1.21,
    1.62,
    1.12
]

inv = zip(subjects, sub_code, weight)
# print(list(inv))

s, c, w = zip(*inv)
print(s,c,w)

