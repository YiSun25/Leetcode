class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        list1 = []
        list2 = []
        for i in range (1,n+1):
            if i%m != 0:
                list1.append(i)
            else:
                list2.append(i)

        num1 = sum(list1)
        num2 = sum(list2)

        return num1 - num2
    
"""

Other Solutions:
1. 
class Solution(object):
  def differenceOfSums(self, n, m):
      num1=0
      num2=0
      for i in range(1,n+1):
          if  i%m==0:
              num2+=i
          else:
              num1+=i
      return num1-num2

      
2. 
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        return n * (n + 1) // 2 - n // m * (n // m + 1) * m

        
"""