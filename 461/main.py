
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        ans = 0
        z = x ^ y
        while z:
            if z & 1:
                ans = ans + 1
            z >>= 1
        return ans


def main():
    s = Solution()
    print s.hammingDistance(1, 4)


if __name__ == '__main__':
    main()
