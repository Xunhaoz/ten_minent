import csv


def passwd_to_csv():
    l = []
    with open(r"C:\Users\leo20\Desktop\ten-minentExercise\F1750_exercises\py\data\passwd.csv", 'r') as f_read:
        csv_reader = csv.reader(f_read, delimiter=":")

        for line in csv_reader:
            l.append(line)

    with open(r"C:\Users\leo20\Desktop\ten-minentExercise\F1750_exercises\py\data\passwd.csv", 'w') as f_write:
        csv_writer = csv.writer(f_write, delimiter='\t', lineterminator='\n')
        for line in l:
            csv_writer.writerow([line[0], line[2]])


passwd_to_csv()
