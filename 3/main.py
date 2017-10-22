# -*- coding: utf-8 -*-


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        maxLength = 0
        str = {}

        for i in range(len(s)):
            if s[i] in str and str[s[i]] >= start:
                start = str[s[i]]+1
            else:
                maxLength = max(maxLength, i - start + 1)
            str[s[i]] = i
        return maxLength


def main():
    s = Solution()
    print s.lengthOfLongestSubstring("pwwkew")
    print s.lengthOfLongestSubstring("tmsmzuxt")


if __name__ == '__main__':
    main()


"""
Hint: 要记得str[s[i]] >= start，start之前的字符就不要了
"""