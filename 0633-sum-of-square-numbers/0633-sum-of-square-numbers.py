class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c<0 : return False

        left=0  
        right=int(c**0.5)
        
        while (left<=right):
            sum=left**2+right**2

            if sum==c:
                return True
            elif sum<c:
                left+=1
            else:
                right-=1
        
        return False