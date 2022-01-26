def worldcount():
    with open(r'C:\Users\leo20\Desktop\ten-minentExercise\F1750_exercises\jupyer_notebook\data\text.txt', 'r') as fh:
        result = {
            "Characters": 0,
            "Words": 0,
            "Unique words": 0,
            "Lines": 0
        }
        different_word = set()
        for i in fh:
            words = i.split()
            result["Lines"] += 1
            result["Characters"] += len(i)
            result["Words"] += len(words)
            different_word.update(words)
        result["Unique words"] = len(different_word)
        for key, value in result.items():
            print(f"{key}: {value}")

worldcount()
