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


# Manacher算法
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length == 0 or length == 1:
            return s

        mx = 0  # 边界
        id = 0  # 中点
        p = [0] * 2010

        i = 0
        j = 1
        ss = ""
        while i < length and j < length * 2 + 1:
            ss += "#"
            j += 1
            ss += s[i]
            i += 1
            j += 1
        ss += "#"
        # print ss

        for i in range(0, length * 2 + 1):
            p[i] = min(p[2 * id - i], mx - i) if mx > i else 1
            while i >= p[i] and i + p[i] < 2 * length + 1 and (ss[i - p[i]] == ss[i + p[i]]):
                p[i] += 1

            if i + p[i] > mx:
                mx = i + p[i]
                id = i

        # 输出得到的p数组
        # k = 0
        # while p[k] != 0:
        #     print p[k]
        #     k += 1

        maxlength = 0
        for i in range(len(p)):
            if p[i] > maxlength:
                maxlength = p[i]
                id = i
        # maxlength - 1是最长的回文串长度

        ans = ""
        j = 0
        for i in range(id-maxlength+1, id+maxlength):
            if ss[i] == "#":
                continue
            else:
                ans += ss[i]
                j += 1
        return ans


def main():
    s = Solution()
    print s.longestPalindrome("caba")
    print s.longestPalindrome("caabbaa")
    print s.longestPalindrome("cbb")


if __name__ == '__main__':
    main()

"""
Hint: 回文串 ：正读和反读都一样的字符串
代码一：分回文串为奇数or偶数，遍历i，以i为中心判断左右两边是否相同
代码二：Manacher算法

Manacher算法参考
https://github.com/julycoding/The-Art-Of-Programming-By-July/blob/master/ebook/zh/01.05.md
http://ztmark.github.io/2016/02/20/LeetCode%20Longest%20Palindromic%20Substring%20%E9%A2%98%E8%A7%A3/


写了一个蠢bug
原意是如果length == 0 或者 length ==1 直接返回length

if length == 0 or 1:
    return length

这样是不管length等于几都直接返回了，因为1永远是对的啊hhhh
"""
