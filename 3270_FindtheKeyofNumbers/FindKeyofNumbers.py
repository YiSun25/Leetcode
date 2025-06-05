class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        # 补齐成 4 位字符串
        s1 = str(num1).zfill(4)
        s2 = str(num2).zfill(4)
        s3 = str(num3).zfill(4)

        # 计算每一位的最小值
        result_digits = [str(min(int(s1[i]), int(s2[i]), int(s3[i]))) for i in range(4)]

        # 拼接成字符串再转换为整数，自动去掉前导0
        return int("".join(result_digits))
    
solution = Solution()
num1 = 1987
num2 = 2879
num3 = 698

print(solution.generateKey(num1, num2, num3))


######## Better Solution ########
# class Solution:
#     def generateKey(self, x: int, y: int, z: int) -> int:
#         ans = 0
#         pow10 = 1
#         while x and y and z:
#             ans += min(x % 10, y % 10, z % 10) * pow10
#             x //= 10
#             y //= 10
#             z //= 10
#             pow10 *= 10
#         return ans

