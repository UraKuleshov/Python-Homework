import re


# task 1
class Date:
    data = []

    def __init__(self, date):
        self.date = date

    @classmethod
    def integer(cls, data):
        day = re.findall(r'\d\d', data[0:2])
        day = "".join(day)
        cls.data.append(int(day))

        month = re.findall(r'[-]\d\d[-]', data)
        month = "".join(month)
        month = re.sub("-", "", month)
        cls.data.append(int(month))

        year = re.findall(r'\d\d\d\d', data)
        year = "".join(year)
        cls.data.append(int(year))
        print(cls.data)

    @staticmethod
    def validation():
        if Date.data[0] > 31:
            print("День месяца не может быть больше 31!")

        if Date.data[1] > 12:
            print("Месяц не может иметь значение больше 12!")


Date.integer("30-12-2022")
Date.validation()


# task 2
class ZeroDivision(ZeroDivisionError):
    def __init__(self, mistake):
        self.mistake = mistake

    def __str__(self):
        print(self.mistake)


human = ""
number = int(input("Введите число, которое хотите поделить: "))

while human != "exit":
    try:
        human = input("Введите делитель, для выхода введите 'exit': ")
        if int(human) == 0:
            raise ZeroDivision("На 0 делить нельзя!")
    except ZeroDivision:
        a = ZeroDivision("На 0 делить нельзя!")
        a.__str__()
    except ValueError:
        print(f'Вы ввели не число!')


# task 3
class NumbersOnly:
    def __init__(self, number):
        self.number = number

    def int_or_not(self):
        check = self.number.isnumeric()
        if check == False:
            print("Вы ввели не число!")
        elif check == True:
            number = self.number
            return number


numbers = []
human = ""
while human != "stop":
    human = input("Введите число(для остановки ввести stop): ")
    a = NumbersOnly(human)
    if a.int_or_not():
        numbers.append(a.int_or_not())
    elif human == "stop":
        break
print(numbers)


# task 4, 5, 6
class Warehouse:
    warehouse = {"диван": 10, "кресло": 20}
    office = {}
    divisions = ["склад", "офис"]

    def __init__(self, equipment):
        self.equipment = equipment

    @classmethod
    def availability(cls):
        print(f'На складе: {cls.warehouse}')
        print(f'На офисе: {cls.office}')

    @classmethod
    def show_divisions(cls):
        print(f'У компании есть: {cls.divisions}')

    def entrance(self):
        if self.equipment[0] not in self.warehouse:
            self.warehouse[self.equipment[0]] = int(self.equipment[1])
        elif self.equipment[0] in self.warehouse:
            self.warehouse[self.equipment[0]] = self.warehouse[self.equipment[0]] + int(self.equipment[1])
            print(f'{self.equipment[0]} уже есть на складе! {self.equipment[0]} добавлен к основному количеству на складе.')

    def write_downs(self):
        if self.equipment[0] in self.warehouse:
            self.warehouse[self.equipment[0]] = self.warehouse[self.equipment[0]] - int(self.equipment[1])
            if self.warehouse[self.equipment[0]] == 0:
                del self.warehouse[self.equipment[0]]
        elif self.equipment[0] not in self.warehouse:
            print(f'{self.equipment[0]} нету на складе! Списание не произведено!')

    @classmethod
    def moving(cls, from_where, where, product, quantity):
        if from_where == "склад" and where == "офис":
            if product not in cls.warehouse:
                print("Ошибка! На складе такого товара нету!")
            elif product in cls.warehouse:
                cls.warehouse[product] -= int(quantity)
                if cls.warehouse[product] == 0:
                    del cls.warehouse[product]
                if product not in cls.office:
                    cls.office[product] = int(quantity)
                elif product in cls.office:
                    cls.office[product] += int(quantity)
        elif from_where == "офис" and where == "склад":
            if product not in cls.office:
                print("Ошибка! На офисе такого товара нету!")
            elif product in cls.office:
                cls.office[product] -= int(quantity)
                if cls.office[product] == 0:
                    del cls.office[product]
                if product not in cls.warehouse:
                    cls.warehouse[product] = int(quantity)
                elif product in cls.warehouse:
                    cls.warehouse[product] += int(quantity)


class Office_Equipment:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def __str__(self):
        a = []
        a.append(self.product)
        a.append(self.quantity)
        return a


human = ""
while human != "stop":
    print("Показать остатки - 1\n"
          "Добавить товар на склад - 2\n"
          "Убрать товар со склада - 3\n"
          "Показать подразделения - 4\n"
          "Переместить товар - 5")
    human = input("Что будем делать?: ")
    if human == "1":
        Warehouse.availability()
    elif human == "2":
        product = input("Введите название товара: ")
        quantity = input("Введите количество товара(должно быть числом): ")
        check = ""
        while check != True:
            check = quantity.isnumeric()
            if check == False:
                quantity = input("Вы ввели не число! Попробуйте еще раз.: ")
        a = Office_Equipment(product, quantity)
        b = Warehouse(a.__str__())
        b.entrance()
    elif human == "3":
        print("Чтобы убрать товар, сначало его нужно вернуть на склад!")
        product = input("Введите название товара: ")
        quantity = input("Введите количество товара(должно быть числом): ")
        check = ""
        while check != True:
            check = quantity.isnumeric()
            if check == False:
                quantity = input("Вы ввели не число! Попробуйте еще раз.: ")
        a = Office_Equipment(product, quantity)
        b = Warehouse(a.__str__())
        b.write_downs()
    elif human == "4":
        Warehouse.show_divisions()
    elif human == "5":
        from_where = input("Введите название подразделения из которого нужно переместить товар(склад/офис): ")
        where = input("Куда нужно переместить?(склад/офис): ")
        product = input("Что нужно переместить?: ")
        quantity = input("Сколько?: ")
        check = ""
        while check != True:
            check = quantity.isnumeric()
            if check == False:
                quantity = input("Вы ввели не число! Попробуйте еще раз.: ")
        Warehouse.moving(from_where, where, product, quantity)


# task 7
class Operations:
    def __init__(self, num, num_2):
        self.num = num
        self.num_2 = num_2

    def __add__(self):
        print(self.num + self.num_2)

    def __mul__(self):
        print(self.num * self.num_2)


class ComplexNumber:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return self.number


a = ComplexNumber(1)
b = ComplexNumber(2)

c = Operations(a.__str__(), b.__str__())
c.__add__()
c.__mul__()
