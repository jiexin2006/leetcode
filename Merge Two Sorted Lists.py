class ListNode:
    def __init__(self, val=0, next=None):
             self.val = val
             self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        d = ListNode()
        current = d
        while list1 and list2:
            if list1.val > list2.val:
                current.next = list2
                current = list2
                list2 = list2.next
            else:
                current.next = list1
                current = list1
                list1 = list1.next

        current.next = list1 if list1 else list2

        return d.next













        # fin_length = len(list1) + len(list2)
        # res = []
        # if list1[0] > list2[0]:
        #     res.append(list2[0])
        #     list2.pop(0)
        # else:
        #     res.append(list1[0])
        #     list1.pop(0)
        # for i in range(1, fin_length):
        #     try:
        #         if (list1[0]-res[i-1]) < (list2[0]-res[i-1]):
        #             res.append(list1[0])
        #             list1.pop(0)
        #         else:
        #             res.append(list2[0])
        #             list2.pop(0)
        #     except IndexError:
        #         if len(list2) == 0:
        #             res.append(list1)
        #         else:
        #             res.append(list2)
        # return res



