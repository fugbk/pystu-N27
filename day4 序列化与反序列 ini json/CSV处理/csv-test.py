# encoding = utf-8
__author__ = "Ang Li"

import csv

row = [
    ("id", "name", "age", "sex", "class"),
    [1, "tom", "14", "m", "N27"],
    (2, "jerry", "15", "w", "N17"),
    [3, 'mar', 14, 'w', 'N26"-"1']
]

filename = "student.csv"

with open(filename, "w+", encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(row[0])
    writer.writerows(row[1:])

with open(filename, encoding='utf-8', newline='') as f:
    reader = csv.reader(f)   # csv.reader（） 返回的是一个迭代器
    print(next(reader))
    for line in reader:
        print(line)
