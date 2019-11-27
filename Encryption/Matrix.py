import numpy as np


def checkPivots(matrix):
    for i in range(matrix.shape[0]):
        for j in range(matrix.shape[1]):
            if i == j and matrix[i][j] != 1:
                return False
    return True


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def getMatrix(self):
        """
        :return: Getting a Matrix
        """
        return self.matrix

    def setMatrix(self, matrix):
        """
        :param matrix: Setting a Matrix
        """
        self.matrix = matrix

    def swapRow(self, matrix):
        if matrix[0][0] == 1:
            return matrix
        else:
            for i in range(matrix.shape[0]):
                if matrix[i + 1][0] == 1:
                    return

    def reducePivot(self):
        pass

    def combine(self):
        pass

    def ref(self):
        pass

    def rref(self):
        pass


if __name__ == '__main__':
    identity_matrix = np.array(
        [[1, 0, 0],
         [0, 1, 0],
         [0, 0, 1]])
# checkPivots(identity_matrix)
    Matrix.swapRow(identity_matrix)
