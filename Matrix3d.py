from Matrix2d import Matrix2d


class Matrix3d(object):
    def __init__(self, m, n):
        super().__init__()
        self.r = Matrix2d(m, n)
        self.g = Matrix2d(m, n)
        self.b = Matrix2d(m, n)
        self.m = m
        self.n = n

    def set_data(self, dataValue):
        row, col = 0, 0
        for i in range(0, len(dataValue), 3):
            col = int(i % self.n)
            row = int(i / self.n)
            self.r.data[row][col] = dataValue[i]
            self.g.data[row][col] = dataValue[i+1]
            self.b.data[row][col] = dataValue[i+2]

    def __str__(self):
        return type(self).__name__ + "\n"+str(self.m) + "rows " + str(self.n)+"cols " + "\n" + "Red Channel\n" + str(self.r.data.__str__() + "\n") + "Green Channel\n" + str(self.g.data.__str__() + "\n") + "Blue Channel\n" + str(self.b.data.__str__() + "\n")
