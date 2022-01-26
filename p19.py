import pprint


def passwd_to_dict(filename):
    dic = {}
    with open(filename, 'r') as fh:
        for i in fh:
            i = i.split(':')
            dic.update({i[0]: i[2]})
    return (dic)


pprint.pprint(
    passwd_to_dict(r"C:\Users\leo20\Desktop\ten-minentExercise\F1750_exercises\jupyer_notebook\data\passwd.cfg"),
    sort_dicts=False)
