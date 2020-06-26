"""
Given an integer array nums,
find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

'''
EXPLANATION:

The idea is to first consider the first element to be part of the max sum subarray and for every other element, 
we ask if we would want to add the next element to the existing sum or start all over again with the new element as a 
part of our new subarray.

We would only want to start over if the element is solely bigger than the maximum we have achieved till now + the element.
i.e., if maxTillNow + nums[i] or just nums[i] - we choose one of them and do that for all other elements.

MaxTillNow is achieved that way but starts out initially as the first element, and everytime we see if we want the
next element to hop onto our array or just start a new array on its own.
'''


def maximum_subarray(nums):
    maxi = nums[0]
    globalmaxi = maxi
    ans = [nums[0]]
    for i in range(1, len(nums)):
        if maxi + nums[i] > nums[i]:
            maxi = maxi + nums[i]
            if globalmaxi < maxi:
                ans.append(nums[i])
                globalmaxi = maxi
        else:
            maxi = nums[i]
            ans = [nums[i]]
    print(ans)
    return globalmaxi


print(maximum_subarray([-2, 1, -3, 4, -1, 2, 3, 2, 4]))