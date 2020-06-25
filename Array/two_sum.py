"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

'''
EXPLANATION:

The first thought would be - for every element, we need to check if the compliment (target - element) exists.
A brute-force solution would be - for every element, go through all elements to the right of it and see if they add up
to the given target and return the indices if we did find.

For every element, we check for sum with all other elements:
    That gives us an O(n^2) working solution but it is not good enough for Amazon.

Instead, what we can do is - rather than checking for the compliment for elements we are yet to see, we can check the
elements that we have already seen. The difference being, here we use a hashmap to store the elements we have seen
along with their respective indices. This hashmap helps us avoid going through every other element to check for the
compliment- as the lookup for an element is just O(1).

For every element, we check only those we have seen yet and they are in a hashmap:
    That gives us an O(n) working solution which is what Amazon wants.
    
'''

'''
What datastructure did we use for this solution and why?

We brought in a hashmap (a dictionary in python) for two reasons:
    1. The lookup time is O(1)
    2. It helps us store elements and maps them to its indices
'''


def two_sum(array, target):
    n = len(array)                  # Getting length of array
    seen = {}                       # Declaring the empty hashmap
    for i in range(n):              # Loop start --> O(n) time
        comp = target - array[i]    # Storing the compliment
        if comp in seen:            # Checking if it is already seen --> O(1) time
            return [seen[comp], i]  # If we end up finding the comp, we return the comp's index and current element idx
        else:
            seen[array[i]] = i      # If we don't find the comp, we store the index of curr element as seen in dict
    return -1                       # If we don't return while in the loop, there's no such pair, hence return -1


print(two_sum([1, 6, 3, 5, 2], 22))