class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        l = 0
        r = (len(matrix) * len(matrix[0])) - 1

        while l <= r:
            mid = l + (r-l)//2
            x = mid // len(matrix[0])
            y = mid % len(matrix[0])
            print(mid, matrix[x][y])
            if matrix[x][y] == target:
                return True
            elif matrix[x][y] < target:
                l = mid + 1
            else:
                r = mid - 1
            print(l,r)
        return False
