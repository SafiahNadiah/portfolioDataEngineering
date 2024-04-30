def find_closest_number(numbers, target):
    if not numbers:
        return None
 
    closest = numbers[0]  # Initialize closest with the first number in the list
    min_difference = abs(target - closest)
 
    for num in numbers:
        difference = abs(target - num)
        if difference < min_difference:
            closest = num
            min_difference = difference
 
    return closest

"""
Find The Closest Number
Write a function that finds the first closest number in a list



In: ([2, 4, 8, 10], 6)

Out: 4
"""
