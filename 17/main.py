# -*- coding:utf-8 -*-


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {
            '0': "",
            '1': "",
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'}
        if len(digits) == 0:
            return []
        ans = [""]
        for i in digits:
            temp = []
            chars = dic[i]
            for j in chars:
                for k in ans:
                    temp.append(k + j)
            ans = temp
        return ans


def main():
    s = Solution()
    print s.letterCombinations("23")


if __name__ == '__main__':
    main()
