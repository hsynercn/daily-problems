# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    stack_a = []
    stack_b = []
    stack_a.append(l1.val)
    stack_b.append(l2.val)
    temp_a = l1.next
    temp_b = l2.next
    while temp_a != None:
        stack_a.append(temp_a.val)
        temp_a = temp_a.next
    while temp_b != None:
        stack_b.append(temp_b.val)
        temp_b = temp_b.next
    last_common = None
    previous = None
    extra = 0
    while len(stack_a) != 0 and len(stack_b) != 0:
        val_a = stack_a.pop()
        val_b = stack_b.pop()
        sum = val_a + val_b + extra
        extra = sum//10
        sum %= 10
        last_common = ListNode(sum)
        last_common.next = previous
        previous = last_common

    if len(stack_a) != 0 or len(stack_b) != 0:
        while len(stack_a) != 0:
            val_a = stack_a.pop()
            sum = val_a + extra
            extra = sum // 10
            sum %= 10
            last_common = ListNode(sum)
            last_common.next = previous
            previous = last_common
        while len(stack_b) != 0:
            val_b = stack_b.pop()
            sum = val_b + extra
            extra = sum // 10
            sum %= 10
            last_common = ListNode(sum)
            last_common.next = previous
            previous = last_common

    if extra == 1:
        last_common = ListNode(1)
        last_common.next = previous
        previous = last_common
    return last_common

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print result.val,
  result = result.next
# 7 0 8