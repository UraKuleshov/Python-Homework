import time


# task 1
class TrafficLight:
    def __init__(__color):
        __color.red = "Red"
        __color.yellow = "Yellow"
        __color.green = "Green"

    def running(__color):
        previous_mode = "g"
        a = "g"
        while a != "":
            a = input("Выберите режим светофора(r - red, y - yellow, g - green, "" - exit) ")
            if a == "r":
                if previous_mode != "g":
                    print("Выбран не верный режим!")
                    continue
                print(f'Режим светофора: {__color.red}')
                previous_mode = "r"
                time.sleep(7)
            elif a == "y":
                if previous_mode != "r":
                    print("Выбран не верный режим!")
                    continue
                print(f'Режим светофора: {__color.yellow}')
                previous_mode = "y"
                time.sleep(2)
            elif a == "g":
                if previous_mode != "y":
                    print("Выбран не верный режим!")
                    continue
                print(f'Режим светофора: {__color.green}')
                previous_mode = "g"
                time.sleep(15)


traffic_light = TrafficLight()

traffic_light.running()


# task 2
class Road:
    def __init__(self, __length, __width):
        self.length = __length
        self.width = __width
        self.calc = __length * __width * 25 * 5 / 1000

    def show(self):
        print(f'Масса асфальта, необходимая для покрытия всей дороги слставляет: {int(self.calc)} т.')


calculation = Road(20, 5000)
calculation.show()


# task 3
class Worker:
    def __init__(self, name, surname, position, _income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = _income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        print(f'Сотрудник {self.name} {self.surname} работает на должности: {self.position}')

    def get_total_income(self):
        result = self._income["wage"] / 100 * self._income["bonus"]
        print(f'Доход с учетом премии составляет: {result + self._income["wage"]}')


worker = Position("Виталий", "Сергеев", "бухгалтер", {"wage": 1200, "bonus": 10})
worker.get_full_name()
worker.get_total_income()

worker_2 = Position("Андрей", "Андреев", "директор", {"wage": 2000, "bonus": 20})
worker_2.get_full_name()
worker_2.get_total_income()


# task 5
class Title:
    def __init__(self, a):
        self.a = a

    def draw(self):
        print(f'Запускается {self.a}')


class Pen(Title):
    def __init__(self, a):
        super().__init__(a)
        self.b = "ручки"

    def draw(self):
        print(f'Запускается {self.a} "{self.b}"')


class Pencil(Title):
    def __init__(self, a):
        super().__init__(a)
        self.b = "весёлого карандаша"

    def draw(self):
        print(f'Запускается {self.a} "{self.b}"')


class Handle(Title):
    def __init__(self, a):
        super().__init__(a)
        self.b = "красного маркера"

    def draw(self):
        print(f'Запускается {self.a} "{self.b}"')


# a = Pen("отрисовка")
# a.draw()
#
# b = Pencil("отрисовка")
# b.draw()
#
# c = Handle("отрисовка")
# c.draw()
