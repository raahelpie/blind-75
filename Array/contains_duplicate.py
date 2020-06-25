"""
Given an array of integers, find if the array contains any duplicates.

Your function should return true if any value appears at least twice in the array,
and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
"""

'''
EXPLANATION:

This is also a search problem, we can solve this just as we have solved the two_sum problem. Store the elements
we have already seen and for every element we check if the element is in the set, if yes return true and if we reached
the end without returning anything, we haven't found any duplicates hence return false.

Every thing is just like the two_sum solution, except that we use a set here.
If the element is already in set, we return True, if its not in set, we add it.
'''

'''
What datastructure did we use and why?

We used a set() datastructure because:
    1. The lookup time is O(1)
'''


def contains_duplicates(nums):
    seen = set()
    for each in nums:
        if each in seen:
            return True
        else:
            seen.add(each)
    return False


print(contains_duplicates([1, 2, 3, 4]))
