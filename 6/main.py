# -*- coding: utf-8 -*-


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        length = len(s)
        if numRows == 1 or length <= numRows:
            return s
        str = ""
        for i in range(numRows):
            j = i
            while j < length:
                str += s[j]
                if numRows != i + 1 and j + 2 * (numRows - i - 1) < length and i != 0:
                    str += s[j + 2 * (numRows - i - 1)]
                j += 2 * (numRows - 1)

        return str


def main():
    s = Solution()
    print s.convert("PAYPALISHIRING", 3)
    print s.convert("ABC", 2)


if __name__ == '__main__':
    main()

"""
参考：http://cs-cjl.com/2016/06_27_leetcode_6_zigzag_conversion
"""