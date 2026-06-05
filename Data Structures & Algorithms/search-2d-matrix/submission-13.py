class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        
        r_l = 0
        r_r = len(matrix)-1

        while r_l < r_r:
            
            row = r_l + (r_r-r_l)//2
            print(row)
            l = 0
            r = len(matrix[row])-1

            if matrix[row][l] <= target <= matrix[row][r]:

                while l < r:

                    mid = l+ (r-l)//2
                    print(mid)
                    if matrix[row][mid] == target:
                        return True
                    else:
                        if matrix[row][mid] > target:
                            r = mid
                        else:
                            l = mid+1
                
                if l == r:
                    if matrix[row][l]==target:
                        return True
                    else:
                        return False


            else:
                if target > matrix[row][r]:
                    r_l = row+1
                elif target < matrix[row][l]:
                    r_r = row

        if r_l == r_r:

            l = 0
            r = len(matrix[r_l])-1

            if matrix[r_l][l] <= target <= matrix[r_l][r]:

                while l < r:

                    mid = l+ (r-l)//2
                    print(mid)
                    if matrix[r_l][mid] == target:
                        return True
                    else:
                        if matrix[r_l][mid] > target:
                            r = mid
                        else:
                            l = mid+1
                
                if l == r:
                    if matrix[r_l][l]==target:
                        return True
                    else:
                        return False

        return False
            
                    