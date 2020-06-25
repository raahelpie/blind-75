"""
Given an array nums of n integers where n > 1,
return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

Constraint:
It's guaranteed that
the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity?
(The output array does not count as extra space for the purpose of space complexity analysis.)
"""

'''
EXPLANATION:
The idea is to think of the solution in a differently framed way.
Product of all the elements in the array except self is the same as the product of all elements to left of the number
with the product of all elements to the right of it.

For each element, the product of elements to the left of it will be the immediate element in the left of it multiplied
with the lefts of that immediate element. And for that - the lefts will be the immediate left multiplied to the lefts of
the before element going up until the first element for which the lefts is 1 since there are no elements to the left.

The same with the rights.

We have two extra arrays other than the result array, one for storing the products to the left of each element of og arr
and the other for storing the products to the right of each element in the og array.

For the first element in the og array, there's no elements to the left of it - so lefts[0] = 1
For the last element, there's no element to the right of it - so rights[-1] = 1

Now that we already have the lefts[0], we start from the 1st index till the end of array:
    
    lefts[idx] = nums[idx-1]*lefts[idx - 1]
    
Since in python, we cant do list assignment for indices that dont already exist, we rewrite the above formula this way:

    lefts.append(nums[i-1]*lefts[-1])
    
This way, every time we append lefts[-1] points to the lefts of the previous index. 

    
    
Similarly for rights, we come from behind (leaving last element) -
 
    rights[idx] = nums[idx+1]*right[idx+1]
    
Hence we need to append the rights of the next index to the beginning of the rights array:

    rights.insert(0, nums[idx+1]*rights[0])
    
Now that we have the lefts and rights of all elements in the array: the result array will be:

    result[idx] = lefts[idx] * rights[idx]
    

But the fact that there are 2 extra arrays might be irksome - hence we can do some more optimization

We have the lefts. Now we can have a variable initialized to 1.
If we multiply 1 with the lefts of the last element, we will be done with the results of the last element.
Now we can update the variable by multiplying it with the last element of the array - because that will be the rights of 
the last but one element of the array:

so we multiply the lefts of the last but one with the variable that is now multiplied by the last element

lefts[i] = lefts[i] * variable * nums[i+1]

Variable stars off with value 1 and we update this lefts array coming from the end  
'''

'''
What did we do and what benefit did it give to us?

We know that the lefts of each element only differ by one element - so instead of - for every element coming from the 
beginning to that index and storing it. We stored the lefts and got the lefts of rest of the elements by just multiplying
the prev element with the lefts of it

We identified and eliminated doing repetitive work by storing the work and utilizing it whenever needed.
'''


def product_but_self(nums):
    n = len(nums)
    lefts = [1]
    for i in range(1, n):
        lefts.append(lefts[-1]*nums[i-1])
    factor = 1
    for i in range(n-1, -1, -1):
        lefts[i] *= factor
        factor *= nums[i]
    return lefts
    # rights = [1]
    # ans = []
    # for i in range(n-2, -1, -1):
    #     rights.insert(0, rights[0]*nums[i+1])
    # for i in range(n):
    #     ans.append(lefts[i]*rights[i])
    # return ans


print(product_but_self([1, 2, 3, 4]))