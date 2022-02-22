import os
import p23


def print_dir_scores(ls):
    for name in ls:
        if name.endswith('.json'):
            p23.printscore(os.path.join(r"./F1750_exercises/py/data/scores", name))


print_dir_scores(os.listdir(r"./F1750_exercises/py/data/scores"))
