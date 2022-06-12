import sys
from itertools import islice
import pprint


def show_sales():
    with open("sales_amounts.txt", "r", encoding="utf-8") as file:
        a = file.read()
        print(a)


def start_iteration(beginning):
    with open("sales_amounts.txt", "r", encoding="utf-8") as file:
        i = islice(file, int(beginning)-1, 100000)
        print(list(i))


def stop_iteration(start, stop):
    with open("sales_amounts.txt", "r", encoding="utf-8") as file:
        i = islice(file, int(start)-1, int(stop))
        print(list(i))


if len(sys.argv) == 1:
    show_sales()
elif len(sys.argv) == 2:
    beginning = sys.argv[1]
    start_iteration(beginning)
elif len(sys.argv) > 2:
    start = sys.argv[1]
    stop = sys.argv[2]
    stop_iteration(start, stop)
