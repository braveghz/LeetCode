# -*- coding:utf-8 -*-


INF = 2147483647


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        min_abs = INF
        ans = 0

        for i in range(length):
            l = i + 1
            r = length - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]
                tmp_abs = abs(s - target)
                if tmp_abs < min_abs:
                    min_abs = tmp_abs
                    ans = s
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    return ans
        return ans


def main():
    s = Solution()
    print s.threeSumClosest([-1, 2, 1, - 4], 2)
    print s.threeSumClosest([1, 1, 1, 0], -100)
    print s.threeSumClosest([0, 2, 1, -3], 1)


if __name__ == '__main__':
    main()
