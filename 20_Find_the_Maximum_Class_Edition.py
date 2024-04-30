class MaxNumberFinder:
    def __init__(self, nums):
        self.nums = nums
 
    def find_max_number(self):
        if not self.nums:
            return None
 
        return max(self.nums)
"""
Find the Maximum Class Edition
Similarly to the previous exercise, find the maximum number of a list. This time, use a class instead. When initializing MaxNumberFinder you will need to provide nums as an argument



finder = MaxNumberFinder([1,3,4,2])
finder.find_max_number() #output 4
"""
