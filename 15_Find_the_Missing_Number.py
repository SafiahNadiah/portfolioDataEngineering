
def find_missing_number(nums):
    n = len(nums)
    total_sum = (n * (n + 1)) // 2  # Sum of first n+1 natural numbers
 
    return total_sum - sum(nums)
