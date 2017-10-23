# -*- coding: utf-8 -*-


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = []
        i = 0
        j = 0
        len1 = len(nums1)
        len2 = len(nums2)
        _len = len1 + len2
        while i < len1 or j < len2:
            if i >= len1 and j < len2:
                nums.append(nums2[j])
                j += 1
                continue
            if i < len1 and j >= len2:
                nums.append(nums1[i])
                i += 1
                continue

            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i += 1
            elif nums1[i] > nums2[j]:
                nums.append(nums2[j])
                j += 1
            else:
                nums.append(nums1[i])
                nums.append(nums2[j])
                i += 1
                j += 1
        if _len % 2 == 0:
            return (nums[_len / 2] + nums[_len / 2 - 1]) / 2.0
        else:
            return nums[_len / 2]


def main():
    s = Solution()
    print s.findMedianSortedArrays([1, 2, 4], [1, 3, 6, 7])


if __name__ == '__main__':
    main()
