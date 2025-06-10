class Solution:
    def minCount(self, coins: list[int]) -> int:
        return sum(((i+1)//2) for i in coins) 
        # (i + 1) // 2 == i // 2 + i % 2

solution = Solution()
coins1 = [4, 2, 1]
coins2 = [2, 3, 10]
print(solution.minCount(coins1))