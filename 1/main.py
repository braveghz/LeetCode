# -*- coding: utf-8 -*-

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        size = len(nums)
        re_num = {}
        for i in range(size):
            tofind = target - nums[i]
            if tofind in re_num:
                return [re_num[tofind], i]
            re_num[nums[i]] = i


def main():
    s = Solution()
    print s.twoSum([2, 7, 11, 15], 9)
    print s.twoSum([3, 2, 4], 6)
    print s.twoSum([2, 5, 5, 11], 10)


if __name__ == '__main__':
    main()
