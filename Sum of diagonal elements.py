def sum_of_diagonals(matrix):
    n = len(matrix)
    main_diagonal_sum = 0
    secondary_diagonal_sum = 0

    for i in range(n):
        main_diagonal_sum += matrix[i][i]
        secondary_diagonal_sum += matrix[i][n - 1 - i]

    return main_diagonal_sum, secondary_diagonal_sum


# Example matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

main_diagonal_sum, secondary_diagonal_sum = sum_of_diagonals(matrix)
print(f"Sum of main diagonal elements: {main_diagonal_sum}")
print(f"Sum of secondary diagonal elements: {secondary_diagonal_sum}")
