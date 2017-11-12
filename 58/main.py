# -*- coding:utf-8 -*-


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        if length == 0:
            return 0
        while length > 0 and s[length-1] == " ":
            length -= 1
        for i in range(length-1, -1, -1):
            if s[i] == " ":
                return length-1-i
        return length


def main():
    s = Solution()
    print s.lengthOfLastWord("hello world")
    print s.lengthOfLastWord("w ")


if __name__ == '__main__':
    main()