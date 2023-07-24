"""Author: ParadoxicaL"""
# Transpose of matrices of any shape.

def transpose(mat):
    transp = []
    for j in range(len(mat[0])):
        row = []
        for i in range(len(mat)):
            row.append(mat[i][j])
        transp.append(row)
    return transp

"""
    Pseudocode for finding transpose
    
(1) get a matrix of any shape (say m x n)
(2) initialize traspose to be empty
(3) initialize row_of_transpose to be empty
(4) for j in range of n (number of columns)
(5)     make row_of_transpose empty
(6)     for i in range of m (number of rows)
(7)         add the element in mat[i][j] to row_of_transpose
(8)     add row_of_transpose to transpose
(9) return transpose

"""
