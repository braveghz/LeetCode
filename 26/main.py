# -*- coding:utf-8 -*-


# 去重不符合in-place?
# class Solution(object):
#     def removeDuplicates(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         dic = dict.fromkeys(nums)
#         _list = list(dic.keys())
#         return len(_list)


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0

        ans = 0
        nums[ans] = nums[0]
        for i in range(1, length):
            if nums[i] != nums[i-1]:
                ans += 1
                nums[ans] = nums[i]
        for i in range(length-ans-1):
            nums.pop()
        return ans+1


def main():
    s = Solution()
    print s.removeDuplicates([1, 1, 2])
    print s.removeDuplicates([1, 1])
    print s.removeDuplicates([1, 1, 2, 3, 3, 3, 4])


if __name__ == '__main__':
    main()
