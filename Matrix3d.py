from Matrix2d import Matrix2d


class Matrix3d(object):
    def __init__(self, m, n):
        super().__init__()
        self.r = Matrix2d(m, n)
        self.g = Matrix2d(m, n)
        self.b = Matrix2d(m, n)
