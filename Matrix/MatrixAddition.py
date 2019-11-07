x = [[12, 1, 3],
     [4, 5, 6],
     [7, 8, 9]]

y = [[5, 4, 8],
     [6, 3, 7],
     [4, 5, 2]]


def square_matrix(X):
    many_col_equal_to_row = [1 for i in range(len(X)) if len(X[i]) == len(X)]
    return len(X) == len(many_col_equal_to_row)


def same_matrix(X, Y):
    if square_matrix(X) and square_matrix(Y):
        if len(X) == len(Y):
            same_col = [1 for i in range(len(X)) and range(len(Y)) if len(X[i]) == len(Y[i])]
            return len(X) == len(same_col)
        return False
    return False


def matrix_addition(X, Y):
    result = [[X[i][j] + Y[i][j] for j in range(len(X[0]))] for i in range(len(X))]
    return result


print(same_matrix(x, y))
print(matrix_addition(x, y))
