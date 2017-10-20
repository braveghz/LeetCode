# -*- coding: utf-8 -*-
from collections import Counter


class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        c = Counter(moves)
        return c['U'] == c['D'] and c['L'] == c['R']


def main():
    s = Solution()
    print s.judgeCircle("UDUD")


if __name__ == '__main__':
    main()

"""
解析：判断是否回到原点，只要判断是否 左==右 and 上==下
"""