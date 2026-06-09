from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i+1, len(matrix)):
                matrix[i][j], matrix[j][i] =  matrix[j][i], matrix[i][j]


"""
Algorithm
1) Reverse the matrix vertically:
    ** the first row becomes the last
    ** the last row becomes the first
2) Transpose the matrix:
        swap elements across the main diagonal
        for all i < j, swap matrix[i][j] with matrix[j][i]
3) The matrix is now rotated 90 degrees clockwise in-place.

Transposing: 
After reversing the rows, the next phase is a transpose. 
A transpose swaps elements across the main diagonal, 
so every element in the upper triangle is exchanged with its symmetric partner in the lower triangle, 
while diagonal elements stay in place. 
Not every upper-triangle element swaps with every lower-triangle element. 
Each element swaps with its transpose partner: 
for each upper-triangle element (i, j) with j > i, 
swap it with its mirrored lower-triangle element (j, i) across the main diagonal.”  
That is exactly the definition of a transpose. 
(i,j)↔(j,i) 

For any matrix, the element at position (i, j) and the element at position (j, i) are mirror images of 
each other across the main diagonal. 

Examples in a 4×4 matrix: 
(0,0) (0,1) (0,2) (0,3)
(1,0) (1,1) (1,2) (1,3)
(2,0) (2,1) (2,2) (2,3)
(3,0) (3,1) (3,2) (3,3)

Diagonal positions are:
(0,0)
(1,1)
(2,2)
(3,3)

Mirror pairs: 
(0,1) ↔ (1,0)
(0,2) ↔ (2,0)
(0,3) ↔ (3,0)
(1,2) ↔ (2,1)
(1,3) ↔ (3,1)
(2,3) ↔ (3,2)


"""