from src.FileHandler import FileHandler
from src.Tokenizer import Tokenizer
from src.Matrix3d import Matrix3d
from src.Matrix2d import Matrix2d

handle = FileHandler("b.pgm")
file = Tokenizer()
file.tokenize(fileHandler=handle)

handle2 = FileHandler("b.pgm")
file2 = Tokenizer()
file2.tokenize(fileHandler=handle2)

handle3 = FileHandler("b.pgm")
file3 = Tokenizer()
file3.tokenize(fileHandler=handle3)


matrixR = Matrix2d(file.row, file.col)
matrixG = Matrix2d(file.row, file.col)
matrixB = Matrix2d(file.row, file.col)

matrixR.set_data(file.data)
matrixG.set_data(file2.data)
matrixB.set_data(file3.data)
print(matrixR, matrixG, matrixB)

handle.saveMatrix2dToMatrix3d(matrixR, matrixG, matrixB)
