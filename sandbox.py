from Matrix2d import Matrix2d
from Tokenizer import Tokenizer
from FileHandler import FileHandler

handle = FileHandler("a.txt")
file = Tokenizer()
file.tokenize(fileHandler=handle)
print(file.typeMatrix)
print(file.row)
print(file.col)
print(file.data)

matrix = Matrix2d(file.row, file.col)
print(matrix)
matrix.set_data(file.data)
print(matrix)
handle.save(matrix, file.typeMatrix, fileName="save2.ppm")
