class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        if abs(x-z) < abs(y-z) :
            return 1
        elif abs(x-z) > abs(y-z) :
            return 2
        else:
            return 0
        
solution = Solution()
x = 2 
y = 10
z = 5
print(solution.findClosest(x, y, z))
