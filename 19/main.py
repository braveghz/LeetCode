# -*- coding:utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next

        nn = length + 1 - n
        curr = head
        count = 1

        if nn == 1:
            head = head.next
            return head
        while curr and count < nn - 1:
            curr = curr.next
            count += 1
        if count == nn - 1:
            curr.next = curr.next.next
        else:
            return None
        return head
