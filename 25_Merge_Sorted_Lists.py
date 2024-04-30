def merge_sorted_lists(list1, list2):
    merged_list = []
 
    i, j = 0, 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
 
    # Append any remaining elements from both lists (if any)
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])
 
    return merged_list
"""
Merge Sorted Lists
Create a function called merge_sorted_lists that takes two sorted lists of integers as input and returns a single sorted list containing all the elements from both input lists. Your function should use only built-in Python tools.



>>> merge_sorted_lists([1, 3, 5], [2, 4, 6])
[1, 2, 3, 4, 5, 6]
>>> merge_sorted_lists([1, 2, 3], [4, 5, 6])
[1, 2, 3, 4, 5, 6]
>>> merge_sorted_lists([1, 4, 6], [2, 3, 5])
[1, 2, 3, 4, 5, 6]
>>> merge_sorted_lists([], [1, 2, 3])
[1, 2, 3]
>>> merge_sorted_lists([1, 2, 3], [])
[1, 2, 3]
>>> merge_sorted_lists([], [])
[]

merged_list: This is the list that will contain the sorted elements from both list1 and list2.

i, j = 0, 0: These are index pointers used to track the current position in list1 and list2.

while i < len(list1) and j < len(list2): This loop continues as long as there are elements to compare in both lists.

if list1[i] < list2[j]: Inside the loop, we compare the elements pointed to by i and j. If the element in list1 is smaller, it gets added to merged_list.

merged_list.append(list1[i]) and merged_list.append(list2[j]): These lines append the smaller element to the merged_list.

i += 1 and j += 1: These lines increment the index pointers i or j after appending an element from list1 or list2.

merged_list.extend(list1[i:]) and merged_list.extend(list2[j:]): After the loop, these lines add any remaining elements from list1 or list2 to merged_list.

The function assumes that both list1 and list2 are already sorted. It goes through both lists, compares each pair of elements, and builds a new list that is sorted. This is a common operation in merge sort algorithms, where two sorted halves of a list are merged into a single sorted list. The function handles the case where the lists are of different lengths by appending the remaining elements after the main loop.



"""
