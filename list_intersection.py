"""
  0
    1 4 5
7 3

3 8 13 18
2 5

lowest common multiple - length of nodes in common

2 5 8 11 14
3 7 11

guess: 4 * 5 - 2
2 6 10 14 18
3 8 13 18

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def checkLL(LL):
    if LL == None:
        print("None")
    elif LL == []:
        print("Empty list")
    while LL:
        print(LL.val)
        LL = LL.next

def createLL(L):
    if not L:
        return None
    head = ListNode(L[0])
    curr = head
    if len(L) == 1:
        return head
    for val in L[1:]:
        newNode = ListNode(val)
        curr.next = newNode
        curr = newNode
    return head

def getIntersectionNode(headA, headB):
    currA = headA
    currB = headB
    lenA = 0
    while currA:
        lenA += 1
        currA = currA.next
    lenB = 0
    while currB:
        lenB += 1
        currB = currB.next
    diff = lenB - lenA  # 1
    """
      0
        1
    2 3
    """
    currA, currB = headA, headB
    if diff < 0:
        for i in range(-1 * diff):
            currA = currA.next
    else:
        for i in range(diff):
            currB = currB.next
    while currB and currA:
        if currA == currB:
            return currA
        currB = currB.next
        currA = currA.next

    # while currA.next:
    #     if currA:
    #         currA = currA.next
    # while currB.next
    #     if currB:
    #         currB = currB.next
    # if currA != currB:
    #     return None
    # currA = headA
    # currB = headB
    # while True:
    #     if currA and currA == currB:
    #         return currA
    #     currA = currA.next
    #     currB = currB.next
    #     if not currA:
    #         currA = headA
    #     if not currB:
    #         currB = headB


    # intersection = None
    # while headA:
    #     headA.val = "A"
    #     headA = headA.next
    # while headB:
    #     if headB.val = "A":
    #         return headB
    #     headB = headB.next
    # return intersection

    # nodes = set()
    # intersection = None
    # while headA:
    #     nodes.add(headA)
    #     headA = headA.next
    # while headB:
    #     if headB in nodes:
    #         return headB
    #     headB = headB.next
    # return intersection

listA = [4,1,8,4,5]
listB = [5,6,1,8,4,5]
# listA = [0]
# listB = [0]
headA = createLL(listA)
headB = createLL(listB)
checkLL(headA)
print()
checkLL(headB)
# print(getIntersectionNode(headA, headB))
