# -*- coding:utf-8 -*-


class Stack(object):
    def __init__(self):
        self.item = []

    def isEmpty(self):
        if len(self.item) == 0:
            return True
        else:
            return False

    def pop(self):
        return self.item.pop()

    def push(self, item):
        return self.item.append(item)

    def peek(self):
        if not self.isEmpty():
            return self.item[len(self.item) - 1]


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = Stack()

        for i in s:
            if i == '}':
                while stack.isEmpty() is False and stack.peek() != '{':
                    p = stack.peek()
                    if p == '(' or p == '[':
                        return False
                    stack.pop()
                if stack.peek() == '{':
                    stack.pop()
                else:
                    stack.push(i)
            elif i == ')':
                while stack.isEmpty() is False and stack.peek() != '(':
                    p = stack.peek()
                    if p == '{' or p == '[':
                        return False
                    stack.pop()
                if stack.peek() == '(':
                    stack.pop()
                else:
                    stack.push(i)
            elif i == ']':
                while stack.isEmpty() is False and stack.peek() != '[':
                    p = stack.peek()
                    if p == '(' or p == '{':
                        return False
                    stack.pop()
                if stack.peek() == '[':
                    stack.pop()
                else:
                    stack.push(i)
            else:
                stack.push(i)

        if stack.isEmpty() is False:
            return False
        else:
            return True


def main():
    s = Solution()
    print s.isValid("")
    print s.isValid("()}}")
    print s.isValid("[sss]{ss}")
    print s.isValid("[sss]{ss}")


if __name__ == '__main__':
    main()
