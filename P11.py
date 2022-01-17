import operator

people = [
    ('Joe', 'Biden', 'Biden1837@gmail.com'),
    ('Emmanuel', 'Macron', 'Macron89@gmail.com'),
    ('Justin', 'Trudeau', 'Biden1837@gmail.com'),
]


def alphabetize_names(arg):
    for i in sorted(arg, key=operator.itemgetter(1, 0)):
        print(f'{i[0]}, {i[1]}: {i[2]}')
    return


alphabetize_names(people)
