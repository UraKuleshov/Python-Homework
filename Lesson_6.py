import sys

# task 3
name = []
hobby = []
result = {}

with open('name.txt', 'r', encoding="utf-8") as f:
    for i in f:
        b = i.replace(",", " ")
        name.append(b)

with open('hobby.txt', 'r', encoding="utf-8") as f:
    for i in f:
        b = i.replace(",", ", ")
        hobby.append(b)

count = 0

if len(hobby) > len(name):
    print("1")
    sys.exit()

try:
    for i in name:
        result[i] = hobby[count]
        count += 1
except IndexError:
    result[i] = "None"


record = open('result.txt', 'w', encoding="utf-8")
record.write(str(result))
