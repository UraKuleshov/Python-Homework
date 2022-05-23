# task 1
duration = float(input("Введите количество секунд: "))

if duration <= 60:
    print(int(duration), "сек")
elif duration <= 3540:
    minutes = duration // 60
    seconds = duration % 60
    print(int(minutes), "мин", int(seconds), "сек")
elif duration > 3600 and duration < 86400:
    hour = duration // 3600
    duration = duration - hour * 3600
    minutes = duration // 60
    seconds = duration - minutes * 60
    print(int(hour), "час", int(minutes), "мин", int(seconds), "сек")
elif duration > 86400:
    days = duration // 86400
    duration = duration - days * 86400
    hour = duration // 3600
    duration = duration - hour * 3600
    minutes = duration // 60
    seconds = duration - minutes * 60
    print(int(days), "дн", int(hour), "час", int(minutes), "мин", int(seconds), "сек")

# task 2
cub_numbers = [i**3 for i in range(1, 1001) if i % 2 != 0]
print(cub_numbers)

# tack2_a
count = 0
b2 = [count + i for i in cub_numbers if sum(map(int, str(i))) % 7 == 0]
print(sum(b2))


# task2_b
count = 0
summa = [i + 17 for i in cub_numbers]
sum_of_numbers = [count + i for i in summa if sum(map(int, str(i))) % 7 == 0]
print(sum(sum_of_numbers))


# task2_c
score = 0
for i in cub_numbers:
    i = i + 17
    if sum(map(int, str(i))) % 7 != 0:
        cub_numbers[score] = 0
    elif sum(map(int, str(i))) % 7 == 0:
        cub_numbers[score] = i
    score = score + 1
print(sum(cub_numbers))
