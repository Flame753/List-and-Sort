import math
import numpy as np


class Encrypt:
    def __init__(self, message, encrypted_matrix_key=np.array([[1, 0], [0, 1]])):
        """
        :param message: A string or message
        :param encrypted_matrix_key: A key that is in a square matrix form
        """
        self.message = message
        self.encrypted_matrix_key = encrypted_matrix_key
        self.encrypted_matrix_message = np.zeros((2, 2))
        self.encrypted_message = ""

    # setter method for message
    def setMessage(self, message):
        self.message = message

    # getter method for message
    def getMessage(self):
        return self.message

    # setter method for encrypted key
    def setEncryptedMatrixKey(self, encrypted_matrix_key):
        self.encrypted_matrix_key = encrypted_matrix_key

    # getter method for encrypted key
    def getEncryptedMatrixKey(self):
        return self.encrypted_matrix_key

    # setter method for encrypted matrix message
    def setEncryptedMatrixMessage(self, encrypted_matrix_message):
        self.encrypted_matrix_message = encrypted_matrix_message

    # getter method for encrypted matrix message
    def getEncryptedMatrixMessage(self):
        return self.encrypted_matrix_message

    # setter method for encrypted matrix message
    def SetEncryptedMessage(self, encrypted_message):
        self.encrypted_message = encrypted_message

    # getter method for encrypt message
    def getEncryptedMessage(self):
        return self.encrypted_message


def charToNum():
    """
    :return: List of numbers that correspond to the letters in a string
    """
    string = ' abcdefghijklmnopqrstuvswxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,!?@$'
    encrypted = dict()
    count = 0
    for i in string:
        encrypted[i] = count
        count = count + 1
    return encrypted


def numOfRow(X):
    """
    :param X: A mxn matrix
    :return: Length of the rows
    """
    return len(X)


def numOfCol(X):
    """
    :param X: A mxn matrix
    :return: Length of the columns
    """
    return len(X[0])


def matrixSize(X):
    """
    :param X: A mxn matrix
    :return: size of matrix [row, col]
    """
    return [numOfRow(X), numOfCol(X)]


def squareMatrix(X):
    """
    :param X: A nxn matrix
    :return: True if the matrix is square (nxn) or False if its not square (mxn)
    """
    many_col_equal_to_row = [1 for i in range(len(X)) if len(X[i]) == len(X)]
    return len(X) == len(many_col_equal_to_row)


def sameSizeSquareMatrix(X, Y):
    """
    :param X: A nxn matrix
    :param Y: Another nxn matrix
    :return: True if both matrix has the same size or False if not same size
    """
    if squareMatrix(X) and squareMatrix(Y):
        if len(X) == len(Y):
            same_col = [1 for i in range(len(X)) and range(len(Y)) if len(X[i]) == len(Y[i])]
            return len(X) == len(same_col)
        return False
    return False


def encryptedMessage(string):
    """
    :param string: A message or text
    :return: A list of number that corresponds to its own character
    """
    string_list = list(string)
    in_coded = charToNum()
    count = 0
    for i, in string_list:
        string_list[count] = in_coded[i]
        count = count + 1
    return string_list


# Not Done
def listToMatrix(lis, size):
    new_lis = encryptedMessage(lis)
    a = 0
    b = 0
    array = np.zeros((math.ceil(len(lis)/size), size))
    for i in new_lis:
        array[a][b] = i
        b = b + 1
        if (b % size) == 0:
            b = 0
            a = a + 1
    return array


# Not finished
def twoByTwoInvertibleMatrix(matrix):
    copy = matrix.copy()
    det = (matrix[0][0] * matrix[1][1] - (matrix[0][1] * matrix[1][0]))
    print(det)
    matrix[0][0] = copy[1][1]
    matrix[0][1] = -copy[0][1]
    matrix[1][0] = -copy[1][0]
    matrix[1][1] = copy[0][0]
    return 1 / det * matrix


if __name__ == '__main__':
    identity_matrix = np.array(
        [[1, 0, 0],
         [0, 1, 0],
         [0, 0, 1]])

    # matrix2 = np.array([[3, 2], [-2, 1]])
    # print(twoByTwoInvertibleMatrix(matrix2))
    # print(encryptedMessage("jacob"))
    print(listToMatrix(list("Hello World"), 4))
    # print(len(charToNum()))
