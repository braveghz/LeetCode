# -*- coding: utf-8 -*-


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        longest = 0

        if length == 0 or length == 1:
            return s

        for i in range(0, length):
            j = 0
            while i - j >= 0 and i + j < length:
                if s[i - j] != s[i + j]:
                    break
                tmp = j * 2 + 1
                j += 1
            if tmp > longest:
                longest = tmp
                j -= 1
                ans = s[i-j:i+j+1]

            j = 0
            while i - j >= 0 and i + j + 1 < length:
                if s[i - j] != s[i + j + 1]:
                    break
                tmp = j * 2 + 2
                j += 1

            if tmp > longest:
                longest = tmp
                j -= 1
                ans = s[i-j:i+j+2]

        return ans


def main():
    s = Solution()
    print s.longestPalindrome("a")
    print s.longestPalindrome("aba")
    print s.longestPalindrome("cbbd")


if __name__ == '__main__':
    main()

"""
Hint: 回文串 ：正读和反读都一样的字符串
分回文串为奇数or偶数，遍历i，以i为中心判断左右两边是否相同

原意是如果length == 0 或者 length ==1 直接返回length

if length == 0 or 1:
    return length
    
这样是不管length等于几都直接返回了，因为1永远是对的啊hhhh
"""
