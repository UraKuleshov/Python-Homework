
# task 1
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        matrix_2 = [list(i) for i in zip(*self.matrix)]
        for i in matrix_2:
            print(i)

    def __add__(self):
        matrix_2 = [list(i) for i in zip(*self.matrix)]
        result = map(lambda x, y, a: x + y + a, matrix_2[0], matrix_2[1], matrix_2[2])
        print(list(result))


a = Matrix([[5, 5, 1], [1, 2, 6], [5, 5, 9]])
a.__str__()
a.__add__()


# task 2
# class Clothes:
#     def __init__(self, clothes):
#         self.clothes = clothes
#         self.a = {}
#
#     def expenditure_coat(self):
#         result = self.clothes["пальто"] / 6.50 + 0.5
#         self.a["пальто"] = result
#
#     def expenditure_suit(self):
#         result = self.clothes["костюм"] * 2 + 0.3
#         self.a["костюм"] = result
#
#     def amount(self):
#         v = self.a["костюм"] + self.a["пальто"]
#         print(f'Итоговый расход ткани составляет: {v}')
#
#
# e = Clothes({"пальто": 20, "костюм": 30})
# e.expenditure_coat()
# e.expenditure_suit()
# e.amount()
