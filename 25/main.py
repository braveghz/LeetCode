# -*- coding:utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None
        curr = head
        l = []

        length = 0
        while curr:
            l.append(curr.val)
            curr = curr.next
            length += 1
        if length < k:
            return head
        ll = []
        i = 0
        while i < length:
            if i + k <= length:
                for j in range(i+k-1, i-1, -1):
                    ll.append(l[j])
                i += k
            else:
                for j in range(i, length):
                    ll.append(l[j])
                break
        curr = head
        for i in range(length):
            curr.val = ll[i]
            curr = curr.next
        return head
