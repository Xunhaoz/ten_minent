def read_final_line():
    with open(r'C:\Users\leo20\Desktop\ten-minentExercise\login.txt', 'r') as fh:
        for i in fh.readlines():
            line = i
        print(line)


read_final_line()
