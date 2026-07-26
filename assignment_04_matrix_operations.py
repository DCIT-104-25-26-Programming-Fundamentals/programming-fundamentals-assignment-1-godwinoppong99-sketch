# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def read_matrix(rows, cols):
    matrix = []

    for i in range(rows):
        row = input("Enter row " + str(i + 1) + ": ").split()

        for j in range(cols):
            row[j] = float(row[j])

        matrix.append(row)

    return matrix

def display_matrix(matrix):
    for row in matrix:
        for value in row:
            print(value, end="  ")
        print()

def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    result = []

    for i in range(cols):
        new_row = []

        for j in range(rows):
            new_row.append(matrix[j][i])

        result.append(new_row)

    return result

def add_matrices(matrix1, matrix2):
    result = []

    rows = len(matrix1)
    cols = len(matrix1[0])

    for i in range(rows):
        row = []

        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])

        result.append(row)

    return result

def multiply_matrices(matrix1, matrix2):
    result = []

    rows = len(matrix1)
    cols = len(matrix2[0])
    common = len(matrix2)

    for i in range(rows):
        row = []

        for j in range(cols):
            total = 0

            for k in range(common):
                total = total + matrix1[i][k] * matrix2[k][j]

            row.append(total)

        result.append(row)

    return result

def part_a():
    print("\n--- TRANSPOSE MATRIX ---")

    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix = read_matrix(rows, cols)

    print("\nOriginal Matrix:")
    display_matrix(matrix)

    result = transpose_matrix(matrix)

    print("\nTransposed Matrix:")
    display_matrix(result)

def part_b():
    print("\n--- ADD MATRICES ---")

    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("Matrix A")
    matrix1 = read_matrix(rows, cols)

    print("Matrix B")
    matrix2 = read_matrix(rows, cols)

    result = add_matrices(matrix1, matrix2)

    print("\nSum of Matrices:")
    display_matrix(result)

def part_c():
    print("\n--- MULTIPLY MATRICES ---")

    rows_a = int(input("Enter rows of Matrix A: "))
    cols_a = int(input("Enter columns of Matrix A: "))

    rows_b = int(input("Enter rows of Matrix B: "))
    cols_b = int(input("Enter columns of Matrix B: "))

    if cols_a != rows_b:
        print("Matrix multiplication is not possible.")
        return

    print("Matrix A")
    matrix1 = read_matrix(rows_a, cols_a)

    print("Matrix B")
    matrix2 = read_matrix(rows_b, cols_b)

    result = multiply_matrices(matrix1, matrix2)

    print("\nProduct of Matrices:")
    display_matrix(result)

def main():

    part_a()

    part_b()

    part_c()


main()