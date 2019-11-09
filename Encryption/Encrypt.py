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
    def set_message(self, message):
        self.message = message

    # getter method for message
    def get_message(self):
        return self.message

    # setter method for encrypted key
    def set_encrypted_matrix_key(self, encrypted_matrix_key):
        self.encrypted_matrix_key = encrypted_matrix_key

    # getter method for encrypted key
    def get_encrypted_matrix_key(self):
        return self.encrypted_matrix_key

    # setter method for encrypted matrix message
    def set_encrypted_matrix_message(self, encrypted_matrix_message):
        self.encrypted_matrix_message = encrypted_matrix_message

    # getter method for encrypted matrix message
    def get_encrypted_matrix_message(self):
        return self.encrypted_matrix_message

    # setter method for encrypted matrix message
    def Set_encrypted_message(self, encrypted_message):
        self.encrypted_message = encrypted_message

    # getter method for encrypt message
    def get_encrypted_message(self):
        return self.encrypted_message


def char_to_num():
    """
    :return: List of numbers that correspond to the letters in a string
    """
    string = 'abcdefghijklmnopqrstuvswxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .!?@$'
    encrypted = dict()
    count = 0
    for i in string:
        encrypted[i] = count
        count = count + 1
    return encrypted


def num_of_row(X):
    """
    :param X: A mxn matrix
    :return: Length of the rows
    """
    return len(X)


def num_of_col(X):
    """
    :param X: A mxn matrix
    :return: Length of the columns
    """
    return len(X[0])


def matrix_size(X):
    """
    :param X: A mxn matrix
    :return: size of matrix [row, col]
    """
    return [num_of_row(X), num_of_col(X)]


def square_matrix(X):
    """
    :param X: A nxn matrix
    :return: True if the matrix is square (nxn) or False if its not square (mxn)
    """
    many_col_equal_to_row = [1 for i in range(len(X)) if len(X[i]) == len(X)]
    return len(X) == len(many_col_equal_to_row)


def same_size_square_matrix(X, Y):
    """
    :param X: A nxn matrix
    :param Y: Another nxn matrix
    :return: True if both matrix has the same size or False if not same size
    """
    if square_matrix(X) and square_matrix(Y):
        if len(X) == len(Y):
            same_col = [1 for i in range(len(X)) and range(len(Y)) if len(X[i]) == len(Y[i])]
            return len(X) == len(same_col)
        return False
    return False


def encrypted(string):
    """
    :param string: A message or text
    :return: A list of number that corresponds to its own character
    """
    string_list = list(string)
    in_coded = char_to_num()
    count = 0
    for i, in string_list:
        string_list[count] = in_coded[i]
        count = count + 1
    return string_list


if __name__ == '__main__':
    identity_matrix = np.array(
        [[1, 0, 0],
         [0, 1, 0],
         [0, 0, 1],
         [1, 2, 3]])

    print(encrypted("victor"))
