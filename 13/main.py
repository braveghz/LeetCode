# -*-coding=utf-8-*-


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = d[s[len(s)-1]]
        i = len(s) - 2
        while i >= 0:
            if d[s[i]] >= d[s[i+1]]:
                ans += d[s[i]]
            else:
                ans -= d[s[i]]
            i -= 1

        return ans


def main():
    s = Solution()
    print s.romanToInt("DI")  # 501
    print s.romanToInt("DL")  # 550
    print s.romanToInt("DXXX")  # 530
    print s.romanToInt("DCCVII")  # 707
    print s.romanToInt("DCCCXC")  # 890
    print s.romanToInt("MDCCC")   # 1800
    print s.romanToInt("XLVIII")  # 48
    print s.romanToInt("IV")


if __name__ == '__main__':
    main()
