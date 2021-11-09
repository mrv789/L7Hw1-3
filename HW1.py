# методом тыка и безкрайнего простора интернета что-то вышло, но вот верно ли....

class Matrix:
    def __init__(self, my_list):
        self.my_list = my_list


    def __str__(self):
        return str('\n'.join(['\t'.join([str(el) for el in i]) for i in self.my_list]))

    def __add__(self, other):
        for i in range(len(self.my_list)):
            for i_2 in range(len(other.my_list[i])):
                self.my_list[i][i_2] = self.my_list[i][i_2] + other.my_list[i][i_2]
        return Matrix.__str__(self)

val = [
    [31, 22],
    [37, 43],
    [51, 86]
    ]
val_2 = [
    [3, 25, 32],
    [2, 4, 6],
    [-1, 64, -8]
    ]

a = Matrix(val)
b = Matrix(val_2)
print(a)
print(b.__add__(a))add__(new_m))