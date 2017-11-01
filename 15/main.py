# -*- coding:utf-8 -*-


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        nums.sort()
        length = len(nums)

        for i in range(length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = length - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l += 1
                elif s > 0:
                    r -= 1
                else:
                    ans.append([nums[i], nums[l], nums[r]])
                    while l < length - 1 and nums[l] == nums[l + 1]:
                        l += 1
                    while r > 0 and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
        return ans


def main():
    s = Solution()
    print s.threeSum([-1, 0, 1, 2, -1])
    print s.threeSum([-2, 0, 0, 2, 2])
    print s.threeSum([0, 0, 0])


if __name__ == '__main__':
    main()
