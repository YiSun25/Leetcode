class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        return sum(nums)%k
        
solution = Solution()
nums = [3,2]
k = 6
print(solution.minOperations(nums,k))