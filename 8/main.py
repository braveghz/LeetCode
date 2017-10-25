# -*- coding: utf-8 -*-

MAX_INF = 2147483647
MIN_INF = -2147483648


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        length = len(str)
        nums = []
        count = 0
        ans = 0
        flag = True

        j = 0
        while j < length:
            if str[j] == " " or str[j] == "0":
                j += 1
                continue
            else:
                break

        if "-" in str and "+" in str:
            return 0
        if str.count("+") > 1 or str.count("-") > 1:
            return 0

        while length > 1 and j < length and str[j] == "-":
            flag = False
            j += 1
        while length > 1 and j < length and str[j] == "+":
            flag = True
            j += 1

        for i in range(j, length):
            try:
                nums.append(int(str[i]))
                count += 1
            except ValueError:
                break
                # return 0

        for i in range(count):
            ans += nums[i] * 10**(count - i - 1)

        if flag is True:
            if ans > MAX_INF:
                return MAX_INF
            return ans
        else:
            if -ans < MIN_INF:
                return MIN_INF
            return -ans


def main():
    s = Solution()
    print s.myAtoi("")
    print s.myAtoi("-")
    print s.myAtoi("    010")
    print s.myAtoi("     +004500")
    print s.myAtoi("-1111")
    print s.myAtoi("+1111")
    print s.myAtoi("+-2")  # 答案是0
    print s.myAtoi("-+1")  # 答案是0
    print s.myAtoi("abc")
    print s.myAtoi("002222")
    print s.myAtoi("00")
    print s.myAtoi("  -0012a42")
    print s.myAtoi("-2147483648")
    print s.myAtoi("-2147483649")


if __name__ == '__main__':
    main()
