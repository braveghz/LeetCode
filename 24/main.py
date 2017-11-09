# -*- coding:utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        if head.next is None:
            return head

        pre, curr = self, head
        while curr and curr.next:
            currn = curr.next
            pre.next = currn
            curr.next = currn.next
            currn.next = curr
            pre = curr
            curr = curr.next
        return self.next


"""
要考虑交换的 curr 和 curr.next的前面和后面
"""
