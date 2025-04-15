class Solution:
    def differenceOfSum(self, nums: list[int]) -> int:
        elementSum, digitSum = 0, 0
        for num in nums:
            elementSum += num
            while num > 0:
                # print(num)
                # print("num%10",num%10)
                digitSum += num % 10
                # print(digitSum)
                num //= 10
                # print("num")
                # print(num)
        return elementSum - digitSum
    
solution = Solution()
nums = [1,15,6,3]
print(solution.differenceOfSum(nums))
