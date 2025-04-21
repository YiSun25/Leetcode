class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:
        res = 0
        n = len(nums)
        def dfs(val, idx): # Depth First Search
            nonlocal res
            if idx == n:
                res += val
                return
            dfs(val ^ nums[idx], idx + 1)
            dfs(val, idx + 1)
        
        dfs(0, 0)
        return res


"""
Notes: https://www.51cto.com/article/614590.html
"""