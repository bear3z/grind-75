# Time: O(n)
# Space: O(n)

class Solution(object):
    def twoSum(self, nums, target):
        table = {}
        for index, currentNumber in enumerate(nums):
            if target - currentNumber in table:
                return [table[target - currentNumber], index]
            table[currentNumber] = index
        return []