import re
import requests


# task 2
URL = "https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs"
result = requests.get(URL)
a = result.text
logs = re.split(r'\n', a)

record = open("result.txt", "w", encoding="utf-8")

for i in logs:
    ip = re.findall(r'\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}[ -][ -]', i)
    ip = "".join(ip).replace(" -", "")

    date = re.findall(r'\d{1,2}[/]\w\w\w[/]\d{1,4}[:]\d{1,2}[:]\d{1,2}[:]\d{1,2}[ ][+]\d{1,4}', i)
    date = "".join(date)

    HEAD = re.findall(r'[H][E][A][D]', i)
    HEAD = "".join(HEAD)
    GET = re.findall(r'[G][E][T]', i)
    GET = "".join(GET)

    downloads = re.findall(r'[/][d][o][w][n][l][o][a][d][s][/][p][r][o][d][u][c][t][_]\d{1,2}', i)
    downloads = "".join(downloads)

    number = re.findall(r'[ ]\d{,3}[ ]\d{0,7}[ ]', i)
    number = "".join(number)

    record.writelines(f'{ip}, {date}, {HEAD}, {GET}, {downloads}, {number};\n')

record.close()


# task 3
def type_logger(x):
    def ttype(x):
        print(f'{x}: {type(x)}')
    return ttype


@type_logger
def calc_cube(t):
    a = t ** 3
    print(a)


calc_cube(5)


# task 4
# def val_checker(t):
#     def error(t):
#         if t > 0:
#             print(t ** 3)
#         elif t < 0:
#             raise ValueError
#     return error
#
#
# @val_checker
# def calc_cube(x):
#     return x ** 3
#
#
# calc_cube(5)

