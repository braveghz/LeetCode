# -*- coding:utf-8 -*-


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        i = 0
        j = len(height) - 1
        ans = 0

        while i <= j:
            if height[i] < height[j]:
                ans = max(ans, (j - i) * height[i])
                i += 1
            else:
                ans = max(ans, (j - i) * height[j])
                j -= 1
        return ans


def main():
    s = Solution()
    print s.maxArea([4, 2, 3, 5])


if __name__ == '__main__':
    main()


"""
Hint

                |
|               |
|           |   |       y
|   |       |   |                木桶宽width  高height 容积V
|   |       |   |
---------------------------
1   2       3   4       x


刚开始在l=x1和r=x4
假设l不动，如果y1<y4，桶的高度是由y1决定的，所以动r的话，width减小，V肯定变小，所以在y1>y4的时候动r
【y1>y4】

if y3<y4，r左移容积肯定减小；y3>y4的话，容积可能不知道大小，判断一下如果>max就更新max
那么这样的话 r=x3
岂不是r=x4的时候 l=x2 x3..的这些情况都丢了？
r=x4，动l，只有当后面的y2 y3..>y1的时候V可能会变大
既然要动r 前面已经说明了【y1>y4】，所以高度h是由y4决定的，就算y2 y3..>y1容积V也不会变大

所以要判断 l和r的y值，小的往中间移动再判断V
"""
