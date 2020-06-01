from src.List import List


class Matrix2d(object):
    def __init__(self, m, n):
        self.data = self.__create(m, n)
        self.m = m
        self.n = n

    @staticmethod
    def __create(m, n):
        response = List()
        row = List(0 for _ in range(n))
        [response.append(row.copy()) for _ in range(m)]
        return response

    def set_data(self, dataValue):
        row, col = 0, 0
        for i in range(len(dataValue)):
            col = int(i % self.n)
            row = int(i / self.n)
            self.data[row][col] = dataValue[i]

    def __str__(self):
        return type(self).__name__ + "\n"+str(self.m) + "rows " + str(self.n)+"cols " + "\n" + str(self.data.__str__())
