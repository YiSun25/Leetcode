from typing import List

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = set()
        duplicates = []
        for num in nums:
            if num in seen:
                duplicates.append(num)
                if len(duplicates) == 2:
                    break
            else:
                seen.add(num)
        return duplicates
    
solution =  Solution()
number = [1,2,3,1,3,4,]
print (solution.getSneakyNumbers(number))
