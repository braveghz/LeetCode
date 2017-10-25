# -*- coding: utf-8 -*-

INF = 2147483647


class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            flag = False
        else:
            flag = True

        x = abs(x)
        num = []
        count = 0
        ans = 0
        while x != 0:
            r = x % 10
            x = x / 10
            count += 1
            num.append(r)

        for i in range(count):
            ans += num[i] * 10**(count-i-1)

        if ans > INF:
            return 0
        if flag is True:
            return ans
        else:
            return -ans


def main():
    s = Solution()
    print s.reverse(-123)
    print s.reverse(1534236469)


if __name__ == '__main__':
    main()
