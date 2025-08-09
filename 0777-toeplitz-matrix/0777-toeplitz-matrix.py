class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        flag=True

        def inBound(r, c):
            return 0 <= r < row and 0 <= c < col

        for i in range (row):
            for j in range (col):
               if inBound(i+1, j+1) and matrix[i][j]!=matrix[i+1][j+1]:
                  return False
                  flag=False
                  break
            if flag == False:
                break
        else:
            return True
        

