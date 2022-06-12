import sys


def add_sale(price):
    with open("sales_amounts.txt", "a", encoding="utf-8") as record:
        record.write(str(price + "\n"))


command = sys.argv[1]
add_sale(command)
