matrix_3_3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
matrix_3_3[0][1] = 20
print (matrix_3_3)
print (matrix_3_3[0][1])

for row in matrix_3_3:
    for item in row:
        print(item)