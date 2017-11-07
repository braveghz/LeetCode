# -*- coding:utf-8 -*-


class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        length = len(nums)
        for i in range(length):
            for j in range(i + 1, length):
                k = j + 1
                kk = length - 1
                while k < kk:
                    if nums[i] + nums[j] + nums[k] + nums[kk] == target:
                        if [nums[i], nums[j], nums[k], nums[kk]] not in ans:
                            ans.append([nums[i], nums[j], nums[k], nums[kk]])
                        k += 1
                        kk -= 1
                        continue
                    if nums[i] + nums[j] + nums[k] + nums[kk] < target:
                        k += 1
                    else:
                        kk -= 1
        return ans


def main():
    s = Solution()
    print s.fourSum([1, 0, -1, 0, -2, 2], 0)
    print s.fourSum([-3, -2, -1, 0, 0, 1, 2, 3], 0)
    print s.fourSum([0, 0, 0, 0], 0)


if __name__ == '__main__':
    main()
