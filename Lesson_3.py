import random
from pprint import pprint

# task 2
numerals = {"one": "один", "two": "два", "three": "три", "four": "четыре", "five": "пять", "six": "шесть",
            "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}


def num_translate_adv(words):
    if words.islower() == False:
        words_1 = words.lower()
        new_word = (numerals[words_1])
        new_word_1 = new_word.capitalize()
        print(new_word_1)
    elif words.islower() == True:
        print(numerals[words])


num_translate_adv("four")


# task 3
def thesaurus(*args):
    names = {}
    for i in args:
        letter_name = i[0]
        if letter_name in names:
            g = [i]
            names[letter_name].append(i)
        elif letter_name not in names:
            names[letter_name] = [i]
    pprint(names)


thesaurus("Иван", "Мария", "Петр", "Илья", "Юлиана", "Мария", "Юлия", "Евгений", "Сергей")


# task 5
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

g = []


def get_jokes(meaning, repeats=0):
    """
    Возвращает meaning шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)
    Любое значение необязательного аргумента, которое больше 0 влияет на то, будут ли повторяться слова
    в каждой группе слов
    """
    meaning_1 = meaning
    try:
        if repeats == 0:
            while meaning > 0:
                v = f'{random.choice(nouns)} {random.choice(adverbs)} {random.choice(adjectives)}'
                g.append(v)
                meaning -= 1
        elif repeats > 0:
            while meaning > 0:
                group_1 = random.choice(nouns)
                nouns.remove(group_1)
                group_2 = random.choice(adverbs)
                adverbs.remove(group_2)
                group_3 = random.choice(adjectives)
                adjectives.remove(group_3)
                v = f'{group_1} {group_2} {group_3}'
                g.append(v)
                meaning -= 1
    except IndexError:
        print(f'Невозможно получить {meaning_1} уникальных значений из 5 доступных!!!')


get_jokes(5, 1)

print(g)
