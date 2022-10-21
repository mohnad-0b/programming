class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        
        
        
        if r*c != len(mat)*len(mat[0]) :
            return mat
        
        arr = []
        # conver matrix to arrye
        for i in  mat:
            for j in i:
                arr.append(j)
        # new mat 
        new_mat=[]
        for raw in range(r):
            m=[]
            for col in range(c):
                m.append(arr[col+raw*c])
            new_mat.append(m)
        
        return new_mat
            