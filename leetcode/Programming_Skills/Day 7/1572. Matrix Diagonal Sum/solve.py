class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum_mat = 0
        for i in range(len(mat)):

            sum_mat += mat[i][i]
            if len(mat)%2 == 0 :
                sum_mat += mat[i][-(i+1)]
            elif i != len(mat)//2 :
                sum_mat += mat[i][-(i+1)]

        return sum_mat