Encrypt = {
    ('a', 'A'): 0,
    ('b', 'B'): 1,
    ('c', 'C'): 2,
    ('d', 'D'): 3,
    ('e', 'E'): 4,
    ('f', 'F'): 5,
    ('g', 'G'): 6,
    ('h', 'H'): 7,
    ('i', 'I'): 8,
    ('j', 'J'): 9,
    ('k', 'K'): 10,
    ('l', 'L'): 11,
    ('m', 'M'): 12,
    ('n', 'N'): 13,
    ('o', 'O'): 14,
    ('p', 'P'): 15,
    ('q', 'Q'): 16,
    ('r', 'R'): 17,
    ('s', 'S'): 18,
    ('t', 'T'): 19,
    ('u', 'U'): 20,
    ('v', 'V'): 21,
    ('w', 'W'): 22,
    ('x', 'X'): 23,
    ('y', 'Y'): 24,
    ('z', 'Z'): 25,
    ' ': 26,
    '.': 27,
    '@': 28
}
print(Encrypt)

def encrypt_dict(string):
    Encrypt = dict()
    count = 0
    for i in string:
        Encrypt[i] = count
        count = count + 1
    return Encrypt


def encrypt_dict2():
    string = list('abcdefghijklmnopqrstuvswxyzABCDEFGHIJKLMNOPQRSTUVWXYZ .!?@$')
    Encrypt = dict()
    count = 0
    for i in string:
        Encrypt[i] = count
        count = count + 1
    return Encrypt


b = encrypt_dict2()
print(b)
