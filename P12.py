import operator

grades = [
    ('Alice', 'Wooding', 69),
    ('Bob', 'Johnson', 86),
    ('cindy', 'Letterman', 93),
    ('David', 'Moor', 86),
    ('Eddie', 'Williams', 91),
]


def sort_grade(data):
    views = ""
    for i in sorted(data, key=operator.itemgetter(2), reverse=True):
        views += f'{i[1]:12s}{i[0]:10s}{i[2]:.2f}\n'

    return views


print(sort_grade(grades))
