class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        height = len(matrix) - 1

        while low <= height:
            row = matrix[(low+height)//2]
            if target > row[-1]:
                low += 1
            elif target < row[0]:
                height -= 1
            else:
                low1 = 0
                height1 = len(row) - 1
                while low1 <= height1:
                    mid1 = (low1+height1)//2
                    if row[mid1] > target:
                        height1 -=1
                    elif row[mid1] < target:
                        low1 += 1
                    else:
                        return True
                return False
        return False


            

        