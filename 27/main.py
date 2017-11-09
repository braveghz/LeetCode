# -*- coding:utf-8 -*-


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        i = 0
        while i < len(nums):
            if nums[i] == val:
                del nums[i]
            else:
                i += 1
        return len(nums)


def main():
    s = Solution()
    print s.removeElement([3, 2, 2, 3], 3)


if __name__ == '__main__':
    main()
