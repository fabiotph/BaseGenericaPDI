class FileHandler:
    def __init__(self, fileName):
        super().__init__()
        self.file = open(file=fileName, mode="r")

    def read_next_line(self):
        response = self.file.readline()
        if not response:
            return None
        return response

    def save(self, matrix2d, typeMatrix, fileName="result", grayScaleValue=255):
        file = open(file=fileName, mode="w")
        file.write(typeMatrix+"\n")
        file.write("#Created by Fabio Tondin\n")
        file.write(str(matrix2d.m)+" "+str(matrix2d.n)+"\n")
        if(typeMatrix == "P2"):
            file.write(str(grayScaleValue)+"\n")
        for i in range(matrix2d.m):
            for j in range(matrix2d.n):
                file.write(str(matrix2d.data[i][j])+" ")
            file.write("\n")
