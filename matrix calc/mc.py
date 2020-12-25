class Matrix:

    def __init__(self, rows=None, cols=None, array=None):
        self.rows = rows
        self.cols = cols
        self.array = array
        self.result_array = [[0] * self.cols] * self.rows

    def print_matrix(self, r_matrix=None):
        print("The result is:")
        result = self.result_array
        if r_matrix:
            result = r_matrix
        for i in result:
            for j in i:
                print(j, end=" ")
            print()
        print()

    def add(self, cls):
        result = self.array[:]
        if self.rows == cls.rows and self.cols == cls.cols:
            for row in range(len(self.array)):
                for element in range(len(self.array[row])):
                    result[row][element] = self.array[row][element] + cls.array[row][element]
            self.print_matrix(result)
        else:
            print("The operation cannot be performed.\n")

    def multiply_by_constant(self, constant):
        result = self.array[:]
        for i in range(len(self.array)):
            for j in range(len(self.array[i])):
                result[i][j] = self.array[i][j] * constant
        self.print_matrix(result)

    def matrix_by_matrix(self, cls):
        if self.cols == cls.rows:
            result = [[sum(x * y for x, y in zip(m1_r, m2_c)) for m2_c in zip(*cls.array)] for m1_r in self.array]
            self.print_matrix(result)
        else:
            print("The operation cannot be performed.\n")

    def transpose(self, t="main", cof=None):
        if cof:
            return list(map(list, (zip(*cof))))
        if t == "main":
            self.print_matrix(list(map(list, (zip(*self.array)))))
        elif t == "side":
            self.print_matrix(list(reversed([list(reversed(x)) for x in zip(*self.array)])))
        elif t == "vertical":
            self.print_matrix([list(reversed(x)) for x in self.array])
        else:
            self.print_matrix(list(reversed(self.array)))

    def determinant(self, array):
        if len(array) == 1:
            return array[0][0]

        return sum(
            x * self.determinant(self.minor(array, 0, i)) * (-1) ** i
            for i, x in enumerate(array[0])
        )

    def minor(self, matrix, row, column):
        minor = matrix[:row] + matrix[row + 1:]
        return [row[:column] + row[column + 1:] for row in minor]

    def inverse(self, matrix):
        det = self.determinant(matrix)
        if det == 0:
            print("This matrix doesn't have an inverse.")

        matrix_minor = [
            [self.determinant(self.minor(matrix, i, j)) for j in range(len(matrix))]
            for i in range(len(matrix))
        ]

        cofactors = [
            [x * (-1) ** (row + col) for col, x in enumerate(matrix_minor[row])]
            for row in range(len(matrix))
        ]
        adjugate = self.transpose(cof=cofactors)
        n = 1 / det
        self.print_matrix([[x * n for x in row] for row in matrix])

def enter_size(s=None):
    if s is None:
        string = "Enter size of matrix:"
    elif s == "transpose":
        string = "Enter matrix size:"
    else:
        string = f"Enter size of {s} matrix:"
    x, y = map(int, input(string).split())
    return x, y


def enter_matrix(rows, s=None):
    if s is None:
        string = "Enter matrix:"
    else:
        string = f"Enter {s} matrix:"
    print(string)
    matrix = []
    for _ in range(rows):
        matrix.append(input().split())
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if "." in matrix[i][j]:
                matrix[i][j] = float(matrix[i][j])
            else:
                matrix[i][j] = int(matrix[i][j])
    return matrix


while True:
    print("""1. Add matrices
    2. Multiply matrix by a constant
    3. Multiply matrices
    4. Transpose matrix
    5. Calculate a determinant
    6. Inverse matrix
    0. Exit""")
    choice = input("Your choice:")
    if choice == "0":
        exit(0)
    elif choice == "1":
        x1, y1 = enter_size("first")
        m1 = enter_matrix(x1, "first")
        x2, y2 = enter_size("second")
        m2 = enter_matrix(x2, "second")
        matrix1 = Matrix(x1, y1, m1)
        matrix2 = Matrix(x2, y2, m2)
        matrix1.add(matrix2)
    elif choice == "2":
        x, y = enter_size()
        m = enter_matrix(x)
        c = input("Enter constant:")
        if "." in c:
            c = float(c)
        else:
            c = int(c)
        matrix = Matrix(x, y, m)
        matrix.multiply_by_constant(c)
    elif choice == "3":
        x1, y1 = enter_size("first")
        m1 = enter_matrix(x1, "first")
        x2, y2 = enter_size("second")
        m2 = enter_matrix(x2, "second")
        matrix1 = Matrix(x1, y1, m1)
        matrix2 = Matrix(x2, y2, m2)
        matrix1.matrix_by_matrix(matrix2)
    elif choice == "4":
        print()
        print("""1. Main diagonal
        2. Side diagonal
        3. Vertical line
        4. Horizontal line""")
        t_choice = input("Your choice:")
        if t_choice == "1":
            x, y = enter_size("transpose")
            m = enter_matrix(x)
            matrix = Matrix(x, y, m)
            matrix.transpose()
        elif t_choice == "2":
            x, y = enter_size("transpose")
            m = enter_matrix(x)
            matrix = Matrix(x, y, m)
            matrix.transpose("side")
        elif t_choice == "3":
            x, y = enter_size("transpose")
            m = enter_matrix(x)
            matrix = Matrix(x, y, m)
            matrix.transpose("vertical")
        else:
            x, y = enter_size("transpose")
            m = enter_matrix(x)
            matrix = Matrix(x, y, m)
            matrix.transpose("Hanan Loves Essa")
    elif choice == "5":
        x, y = enter_size("transpose")
        m = enter_matrix(x)
        matrix = Matrix(x, y, m)
        print("The result is:\n")
        print(matrix.determinant(m))
    elif choice == "6":
        x, y = enter_size("transpose")
        m = enter_matrix(x)
        matrix = Matrix(x, y, m)
        matrix.inverse(m)

# works up to stage 5
