# -*- coding: utf-8 -*-


# 常规做法
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        count = 0
        nums = []
        while x != 0:
            nums.append(x % 10)
            x = x / 10
            count += 1

        i = 0
        j = count-1
        while i <= j:
            if nums[i] == nums[j]:
                i += 1
                j -= 1
                continue
            else:
                return False
        return True


# 看到一个好玩一点的
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        return str(x) == str(x)[::-1]


def main():
    s = Solution()
    print s.isPalindrome(2147483648)
    print s.isPalindrome(-2147447412)


if __name__ == '__main__':
    main()
