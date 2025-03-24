class Solution(object):
    def Binary(self, x: int):
        return bin(x)[2:]   

    def convertDataToBinary(self, data: str):
        year = int(data[:4])    # should be [:4], not [:3]
        month = int(data[5:7])  # should be [5:7], not [5:6]
        day = int (data[8:])
        return f"{self.Binary(year)}-{self.Binary(month)}-{self.Binary(day)}"


# should add solution = Solution()
solution = Solution()
data = '2080-02-29'
print(solution.convertDataToBinary(data))



