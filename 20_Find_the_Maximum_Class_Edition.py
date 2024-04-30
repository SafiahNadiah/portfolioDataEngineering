class MaxNumberFinder:
    def __init__(self, nums):
        self.nums = nums
 
    def find_max_number(self):
        if not self.nums:
            return None
 
        return max(self.nums)
