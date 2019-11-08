import math
import numpy as np

class Encrypt:
    def __init__(self, message, encrypted_key):
        self.message = message
        self.encrypted_key = encrypted_key
        self.encrypted_message

    # setter method for string
    def set_string(self, message):
        self.message = message

    # getter method for string
    def get_string(self):
        return self.message

    # setter method for string
    def set_encrypted_code(self, encrypted_key):
        self.encrypted_key = encrypted_key

    # getter method for string
    def get_encrypted_code(self):
        return self.encrypted_key


def char_to_num():
    string = 'abcdefghijklmnopqrstuvswxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .!?@$'
    encrypted = dict()
    count = 0
    for i in string:
        encrypted[i] = count
        count = count + 1
    return encrypted


def separator(string):
    return list(string)


def incoding(string):
    lis = list(string)
    length = math.floor(len(lis)/9) + len(lis)%9
    print(len(lis))
    print(len(lis)/9)
    print(len(lis)%9)
    print(length)
    return


incoding("timeline and smell")
identity_matrix = (
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1])

print(identity_matrix)
