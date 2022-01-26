def find_longest_word():
    longest_word = set()
    with open(r'C:\Users\leo20\Desktop\ten-minentExercise\F1750_exercises\jupyer_notebook\data\text2.txt', 'r') as fh:
        for i in fh:
            longest_word.update(i.replace('.', '').split())

    return sorted(longest_word, key=len)[-1]


print(find_longest_word())