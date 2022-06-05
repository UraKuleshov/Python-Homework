from itertools import zip_longest


# task 2
a = (i for i in range(0, 15 + 1) if i % 2 != 0)

print(type(a))
try:
    while True:
        print(next(a))
except StopIteration:
    pass


# task 3
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']

tutors_klasses = (i for i in zip_longest(tutors, klasses))

print(type(tutors_klasses))
try:
    while True:
        print(list(next(tutors_klasses)))
except StopIteration:
    pass


# task 4
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

m = [i for b, i in zip(src, src[1:]) if i > b]

print(m)


# task 5
# src_1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
#
# result_1 = [i for i in src_1 if src_1.count(i) < 2]
#
# print(result_1)
