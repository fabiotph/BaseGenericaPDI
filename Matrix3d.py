from Matrix2d import Matrix2d


class Matrix3d(object):
    def __init__(self, m, n):
        super().__init__()
        self.r = Matrix2d(m, n)
        self.g = Matrix2d(m, n)
        self.b = Matrix2d(m, n)
        self.m = m
        self.n = n

    def __init__(self, matrix2dR, matrix2dG, matrix2dB):
        self.r = matrix2dR
        self.g = matrix2dG
        self.b = matrix2dB
        self.m = matrix2dR.m
        self.n = matrix2dR.n

    def set_data(self, dataValue):
        row, col = 0, 0
        print(dataValue)
        for i in range(int(len(dataValue)/3)):
            col = int(i % self.n)
            row = int(i / self.n)
            print("i", i)
            print("row", row)
            print("col", col)
            self.r.data[row][col] = dataValue[3*i]
            self.g.data[row][col] = dataValue[3*i+1]
            self.b.data[row][col] = dataValue[3*i+2]

    def __str__(self):
        return type(self).__name__ + "\n"+str(self.m) + "rows " + str(self.n)+"cols 3channels" + "\n" + "Red Channel\n" + str(self.r.data.__str__() + "\n") + "Green Channel\n" + str(self.g.data.__str__() + "\n") + "Blue Channel\n" + str(self.b.data.__str__() + "\n")
