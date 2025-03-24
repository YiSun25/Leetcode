class Solution:
    def canAliceWin(self, nums: list[int]) -> bool:
        single_digit_sum = 0
        double_digit_sum = 0
        for num in nums:
            if num < 10:
                single_digit_sum += num
            else:
                double_digit_sum += num
        
        return single_digit_sum != double_digit_sum
    
solution = Solution()
input = [5,5,5,25]
print(solution.canAliceWin(input))
