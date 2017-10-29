# -*- coding:utf-8 -*-


class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        ans = ""
        nums = [
            ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'],
            ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'],
            ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'],
            ['', 'M', 'MM', 'MMM']
        ]
        ans += nums[3][num / 1000]
        ans += nums[2][(num % 1000) / 100]
        ans += nums[1][((num % 1000) % 100) / 10]
        ans += nums[0][((num % 1000) % 100) % 10]
        return ans


def main():
    s = Solution()
    print s.intToRoman(707)   # DCCVII
    print s.intToRoman(890)   # DCCCXC
    print s.intToRoman(1800)  # MDCCC
    print s.intToRoman(48)    # XLVIII
    print s.intToRoman(501)   # DI
    print s.intToRoman(4)     # IV


if __name__ == '__main__':
    main()

"""
本来没啥思路..
参考：http://blog.csdn.net/rical730/article/details/59486523
主要是限制了范围 【range from 1 to 3999】就比较好写不用循环了最多3000 MMM
"""
