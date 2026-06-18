class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix)-1
    
        while l<=r:
            mid=(l+r)//2
            if target>=matrix[mid][0]and target<=matrix[mid][-1]:
                ans = mid
                break
            elif target>matrix[mid][-1]:
                l=mid+1
            else:
                r=mid-1
        if l>r:
            return False
        
        search = matrix[ans]
        l=0
        r = len(search)-1
        while l<=r:
            mid = (l +r)//2
            if search[mid]==target:
                return True
            elif target>search[mid]:
                l=mid+1
            else:
                r=mid-1
        return False