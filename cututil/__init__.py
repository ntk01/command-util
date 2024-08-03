import csv


def proc(ifilename: str, ofilename: str, delimiter: str, quotechar: str, fields: list[int]):
    with open(ofilename, 'w', newline='') as writefile:
        with open(ifilename, newline='') as readfile:
            reader = csv.reader(readfile, delimiter, quotechar)
            writer = csv.writer(writefile, delimiter, quotechar)
            for row in reader:
                writer.writerow(list(map(lambda x: row[x], fields)))
