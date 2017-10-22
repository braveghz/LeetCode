# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ans = ListNode(0)
        curr = ans
        extra = 0
        while l1 or l2 or extra:
            curr.next = ListNode(((l1.val if l1 else 0) + (l2.val if l2 else 0) + extra) % 10)
            # print curr.next.val
            extra = ((l1.val if l1 else 0) + (l2.val if l2 else 0) + extra) / 10
            # print extra
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next

        return ans.next


def main():
    s = Solution()
    l1 = ListNode(1)
    l2 = ListNode(9)
    l2.next = ListNode(9)
    l2.next.next = ListNode(9)
    print s.addTwoNumbers(l1, l2).next.next.next.val


if __name__ == '__main__':
    main()

"""
Hint:是两个链表代表的两个数字，1->3->5 代表了531，2->4->6代表了642，然后相加，得到结果链表3711。
就是从个位开始相加...题目好难理解到正确意思...

写错了一个地方看了半天
l1.val = 1 l2.val = 3
print (l1.val if l1 else 0) + (l2.val if l2 else 0) = 3
print (l1.val if l1 else 0 + l2.val if l2 else 0)   = 1
"""
