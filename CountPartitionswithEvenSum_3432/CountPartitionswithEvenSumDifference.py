class Solution:
    def countPartitions(self, nums: list[int]) -> int:
        return 0 if sum(nums) % 2 else len(nums) - 1
    
solution = Solution()
input = [2, 5, 6, 1, 8]
print(solution.countPartitions(input))
