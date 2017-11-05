# -*- coding:utf-8 -*-


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# 405ms
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        head1 = headA
        head2 = headB
        if head1 is None or head2 is None:
            return None

        length1 = 0
        length2 = 0
        while head1:
            length1 += 1
            head1 = head1.next
        while head2:
            length2 += 1
            head2 = head2.next
        cnt = abs(length1 - length2)
        head1 = headA
        head2 = headB
        if length1 > length2:
            while cnt:
                head1 = head1.next
                cnt -= 1
        else:
            while cnt:
                head2 = head2.next
                cnt -= 1
        while head1 and head2:
            if head1 == head2:
                return head1
            else:
                head1 = head1.next
                head2 = head2.next

        return None


"""
找到相同的开始位置，长的linked移动到开始的位置，然后一起++
"""
