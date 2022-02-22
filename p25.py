def myxml(tag, content = '', **arges):
    print(f"<{tag}", end='')

    for j, k in arges.items():
        print(f" {j}=\"{k}\"", end='')

    print(f">", end='')
    if content != '':
        print(f"{content}", end='')
    print(f"</{tag}>")


myxml("Hi", "12", a=1, b=2, c=3)
