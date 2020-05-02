from List import List


class Matrix2d(object):
    def __init__(self, m, n):
        self.data = self.__create(m, n)
        self.m = m
        self.n = n

    @staticmethod
    def __create(m, n):
        response = List()
        row = List(0 for _ in range(m))
        [response.append(row.copy()) for _ in range(n)]
        return response

    # def __setattr__(self, name, value):
    #     if name is not "data":
    #         # print(name)
    #         self.__dict__[name] = value + 20
    #     else:
    #         # print(name)
    #         self.__dict__[name] = value

    # def __getattribute__(self, name):
    #     return object.__getattribute__(self, name)
