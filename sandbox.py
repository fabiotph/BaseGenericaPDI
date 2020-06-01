from Matrix2d import Matrix2d
from Matrix3d import Matrix3d
from Tokenizer import Tokenizer
from FileHandler import FileHandler

handle = FileHandler("b.txt")
file = Tokenizer()
file.tokenize(fileHandler=handle)

handle2 = FileHandler("b.txt")
file2 = Tokenizer()
file2.tokenize(fileHandler=handle2)

handle3 = FileHandler("b.txt")
file3 = Tokenizer()
file3.tokenize(fileHandler=handle3)

# matrix = Matrix3d(file.row, file.col)
# print(matrix)
# matrix.set_data(file.data)
# print(matrix)
# handle.saveMatrix3dToMatrix2d(matrix, file.typeMatrix, fileName="save2.ppm")

matrixR = Matrix2d(file.row, file.col)
matrixG = Matrix2d(file.row, file.col)
matrixB = Matrix2d(file.row, file.col)

matrixR.set_data(file.data)
matrixG.set_data(file2.data)
matrixB.set_data(file3.data)
print(matrixR, matrixG, matrixB)

handle.saveMatrix2dToMatrix3d(matrixR, matrixG, matrixB)
