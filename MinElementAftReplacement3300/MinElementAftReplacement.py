class Solution:
    def minElement(self, nums: list[int]) -> int:
        for i in range(len(nums)):  # Note: it's different from "for num in nums:". Compare with 2535.
            num = nums[i]
            digitSum = 0
            while num > 0:
                digitSum += num % 10
                num //= 10
            nums[i] = digitSum
        return min(nums) 

solution = Solution()
nums = [999,19,199]
print(solution.minElement(nums))


"""
# Better Solution:
class Solution:
    def minElement(self, nums: list[int]) -> int:
        ans = inf
        for num in nums: 
            digitSum = 0
            while num:
                digitSum += num%10
                num //= 10
            ans = min(ans, digitSum)  # Don't need to save new digitSum back to the List! Better solution!
        return ans
"""