# -*- coding:utf-8 -*-


INF = 2147483647

# 498 ms 不过很慢就是了....
class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        dic = dict()
        ans = dict()
        length1 = len(list1)
        length2 = len(list2)
        index = INF

        for i in range(length1):
            dic[list1[i]] = i
        keys = dic.keys()

        for i in range(length2):
            if list2[i] in keys:
                if dic[list2[i]] + i < index:
                    ans.clear()
                    index = dic[list2[i]] + i
                    ans[list2[i]] = index
                elif dic[list2[i]] + i == index:
                    ans[list2[i]] = index
        keys = ans.keys()
        return keys


def main():
    s = Solution()
    print s.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"])
    print s.findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"], ["KFC", "Shogun", "Burger King"])


if __name__ == '__main__':
    main()
