# -*- coding: utf-8 -*-


class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ans = 0
        z = x ^ y
        while z != 0:
            if z & 1:
                ans += 1
            z >>= 1
        return ans


def main():
    s = Solution()
    print s.hammingDistance(1, 4)


if __name__ == '__main__':
    main()

"""
解析：题目想求x和y异或之后的值z，写成二进制有多少个1，所以就从最后一位开始判断是否为1，然后右移一位，直到z变为0。
"""
