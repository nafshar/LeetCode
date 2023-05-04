def generateMatrix(n):
    """
    :type n: int
    :rtype: List[List[int]]
    """
    lst = [[0 for i in range(n)] for j in range(n)]
    lst = fillSquare(lst, 0, 0, n, 1)
    print(lst)

    return lst


def fillSquare(lst, row, col, dim, val):
    # fill the tio row
    for j in range(dim):
        lst[row][col + j] = val
        val += 1

    # fill the right hand side column
    for i in range(1, dim):
        lst[row + i][dim - 1] = val
        val += 1

    # fill the bottom row
    for j in range(dim - 2, -1, -1):
        lst[dim - 1][j] = val
        val += 1

    # fill the left columd
    for i in range(dim - 2, 0, -1):
        lst[i][col] = val
        val += 1
    return lst

generateMatrix(3)