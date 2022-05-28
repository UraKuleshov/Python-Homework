import heapq


# task 1
a = 15 * 3
print(type(a))
b = 15 / 3
print(type(b))
c = 15 // 2
print(type(c))
d = 15 ** 2
print(type(d))


# task 3
print("")
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

minus_plus = ["+", "-"]

temp = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

count = 0

for i in temp:
    if i[-1] in numbers and i[0] not in minus_plus:
        if len(i) < 2 and int(i) > 0:
            i = "0" + i
        if len(i) < 2 and int(i) == 0:
            i = "0" + i
        i = '"' + i + '"'
        temp[count] = i
    elif i[-1] in numbers and i[0] == "+":
        k = i
        if len(i) < 3 and int(i[-1]) > 0:
            k = i.replace("+", "+0")
        k1 = '"' + k + '"'
        temp[count] = k1
    elif i[-1] in numbers and i[0] == "-":
        k = i
        if len(i) < 3 and int(i[-1]) > 0:
            k = i.replace("+", "+0")
        k1 = '"' + k + '"'
        temp[count] = k1
    count = count + 1

print(" ".join(temp))


# task 4
print("")
staff = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

meaning = 0

for i in staff:
    small_letters = i.lower()
    staff[meaning] = small_letters
    meaning = meaning + 1

score = 0
for i in staff:
    if "игорь" in i:
        find_name = i.find("игорь")
        not_necessary = i[0:find_name]
        delete = i.replace(not_necessary, "")
        staff[score] = f'Привет, {delete.capitalize()}!'
    elif "марина" in i:
        find_name = i.find("марина")
        not_necessary = i[0:find_name]
        delete = i.replace(not_necessary, "")
        staff[score] = f'Привет, {delete.capitalize()}!'
    elif "николай" in i:
        find_name = i.find("николай")
        not_necessary = i[0:find_name]
        delete = i.replace(not_necessary, "")
        staff[score] = f'Привет, {delete.capitalize()}!'
    elif "аэлита" in i:
        find_name = i.find("аэлита")
        not_necessary = i[0:find_name]
        delete = i.replace(not_necessary, "")
        staff[score] = f'Привет, {delete.capitalize()}!'
    score = score + 1

print(" ".join(staff))


# task 5.a
print("")
prices = [57.8, 46.51, 97, 55.23, 99.1, 87.45, 55, 1.23, 4.53, 9.1]

result = []


def transformation(i):
    global result
    fractional_part = i % 1
    fractional_part = round(fractional_part, 2)
    fractional_part = str(fractional_part).replace("0.", "")
    whole_part_1 = i // 1
    whole_part_1 = str(i).replace(".0", "")
    whole_part_1 = int(i)
    fractional_part = int(fractional_part)
    view = f"{whole_part_1:02d} руб {fractional_part:02d} коп"
    result.append(view)


for i in prices:
    transformation(i)
print(", ".join(result))


# task 5.b
print("")
print(id(prices))
print(type(prices))
prices.sort()
print(prices)
print(id(prices))
print(type(prices))


# task 5.c
print("")
prices_1 = prices
prices_1.sort(reverse=True)
print(prices_1)


# # task 5.d
# print("")
# largest = heapq.nlargest(5, prices)
# largest.sort()
# print(largest)
