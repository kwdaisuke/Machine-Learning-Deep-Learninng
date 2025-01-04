from typing import List

def intersect(nums1: List[int], nums2: List[int]) -> List[int]:
    return list(set(nums1) & set(nums2))

def intersect_with_skip(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: List[int]
    """

    result = []
    for num in nums1:
        if num in nums2:
            result.append(num)
            nums2.remove(num)
    return result


