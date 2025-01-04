from typing import List, Callable, Optional

def reduce(function: Callable, iterable: List[int], initializer: Optional[int]=None) -> int:
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value

def maxSubArray(nums: List[int]) -> int:
    """
    :type nums: List[int]
    :rtype: int
    """
    maxSum = -10000
    def kadanes(prevSum: int, curElem: int) -> int:
        nonlocal maxSum
        maxSum = max(curElem, maxSum+curElem)
        return max(prevSum,maxSum)
    return reduce(kadanes, nums, maxSum)

#Resource: https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d

