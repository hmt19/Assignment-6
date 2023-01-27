class SumZero:
    def __init__(self,nums):
        self.nums = nums

    def sumZero(self):
        result = []
        for i in range(len(self.nums)):
            for j in range(i + 1, len(self.nums)):
                for k in range(j + 1, len(self.nums)):
                    if(self.nums[i] + self.nums[j] + self.nums[k] == 0):
                        result.append([self.nums[i], self.nums[j], self.nums[k]])
        return result

nums = [-25, -10, -7, -3, 2, 4, 8, 10]
sz = SumZero(nums)
print(sz.sumZero())
