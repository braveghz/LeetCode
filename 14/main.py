# -*- coding:utf-8 -*-


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        strs.sort()
        s = strs[0]
        ss = strs[len(strs)-1]
        ans = ""
        i = 0
        if s == "":
            return ""

        min_length = min(len(s), len(ss))
        while i < min_length:
            if s[i] == ss[i]:
                ans += s[i]
                i += 1
            else:
                break
        return ans


def main():
    s = Solution()
    print s.longestCommonPrefix([])
    print s.longestCommonPrefix(["", ""])
    print s.longestCommonPrefix(["c", "c"])
    print s.longestCommonPrefix(["flower", "flow", "flight"])
    print s.longestCommonPrefix(["flawer", "flaaaw", "flaaaaaght"])


if __name__ == '__main__':
    main()
