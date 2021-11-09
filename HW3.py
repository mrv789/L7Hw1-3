# не пойму, у меня где-то ошибка?

class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        a = self.cells - other.cells
        if a >= 0:
            return Cell(a)
        else:
            print(f"Ошибка. Меньше нуля!")

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    def make_order(self, cells_in_row):
        row = ''
        for i in range(self.cells // cells_in_row):
            row += '*' * cells_in_row + '\n'
        row += '*' * (self.cells % cells_in_row) + '\n'
        return row


vol_1 = Cell(12)
vol_2 = Cell(15)
print(vol_1.make_order(5))
print(vol_2.make_order(5))

print(vol_1 + vol_2)
print(vol_1 - vol_2)
print(vol_1 * vol_2)
print(vol_1 / vol_2)
print(vol_2 - vol_1)
