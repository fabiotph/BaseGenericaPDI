from src.Matrix3d import Matrix3d
from pathlib import Path

path = Path("./img/")


class FileHandler:
    def __init__(self, fileName):
        super().__init__()
        self.file = open(file=path/fileName, mode="r")

    def read_next_line(self):
        response = self.file.readline()
        if not response:
            return None
        return response

    def save(self, matrix, typeMatrix, fileName="result.ppm", grayScaleValue=255):
        file = open(file=path/fileName, mode="w")
        file.write(typeMatrix+"\n")
        file.write("#Created by Fabio Tondin\n")
        file.write(str(matrix.m)+" "+str(matrix.n)+"\n")

        if type(matrix).__name__ == 'Matrix2d':
            self.__saveMatrix2d(matrix, typeMatrix, file,
                                grayScaleValue=grayScaleValue)
        elif type(matrix).__name__ == 'Matrix3d':
            self.__saveMatrix3d(matrix, typeMatrix,
                                file)

    def __saveMatrix2d(self, matrix2d, typeMatrix, file, grayScaleValue=255):
        if(typeMatrix == "P2"):
            file.write(str(grayScaleValue)+"\n")
        for i in range(matrix2d.m):
            for j in range(matrix2d.n):
                file.write(str(matrix2d.data[i][j])+" ")
            file.write("\n")

    def __saveMatrix3d(self, matrix3d, typeMatrix, file):
        for i in range(matrix3d.m):
            for j in range(matrix3d.n):
                file.write(str(matrix3d.r.data[i][j])+" ")
                file.write(str(matrix3d.g.data[i][j])+" ")
                file.write(str(matrix3d.b.data[i][j])+" ")
            file.write("\n")

    def saveMatrix3dToMatrix2d(self, matrix3d, typeMatrix, fileName="result.pgm"):
        fileName = fileName.split(".")
        fileNameR = fileName[0]+"R"+fileName[len(fileName)-1]
        fileNameG = fileName[0]+"G"+fileName[len(fileName)-1]
        fileNameB = fileName[0]+"B"+fileName[len(fileName)-1]

        self.save(matrix3d.r, "P2", fileNameR)
        self.save(matrix3d.g, "P2", fileNameG)
        self.save(matrix3d.b, "P2", fileNameB)

    def saveMatrix2dToMatrix3d(self, matrix2dR, matrix2dG, matrix2dB, fileName="result.ppm"):
        matrix3d = Matrix3d(matrix2dR, matrix2dG, matrix2dB)
        self.save(matrix3d, "P3", fileName)
