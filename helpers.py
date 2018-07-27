from enum import Enum


class Operation(Enum):
    """Operations"""

    DELETED = 1
    INSERTED = 2
    SUBSTITUTED = 3

    def __str__(self):
        return str(self.name.lower())


def distances(a, b):
    """Calculate edit distance from a to b"""
# a = "Yale"
# b = "Harvard"
    # Создаем матрицу
    matrix = [[(0, None) for x in range(len(b) + 1)] for y in range(len(a) + 1)]

    # если второй файл пустой
    for i in range(len(a) + 1):
        matrix[i][0] = (i, Operation.DELETED)

    # если первый файл пустой
    for j in range(len(b) + 1):
        matrix[0][j] = (j, Operation.INSERTED)
    matrix[0][0] = (0, None)

    # заполняем матрицу
    for i in range(1, len(a) + 1):

        for j in range(1, len(b) + 1):

            delete = matrix[i - 1][j][0] + 1
            insert = matrix[i][j - 1][0] + 1
            if a[i - 1] == b[j - 1]:
                subs = matrix[i - 1][j - 1][0]
            else:
                subs = matrix[i - 1][j - 1][0] + 1
            if delete <= insert and delete <= subs:
                matrix[i][j] = (delete, Operation.DELETED)

            elif insert <= delete and insert <= subs:
                matrix[i][j] = (insert, Operation.INSERTED)

            else:
                matrix[i][j] = (subs, Operation.SUBSTITUTED)
    # print matrix
    print(matrix[0])
    return matrix