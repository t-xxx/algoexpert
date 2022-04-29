# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    first = head.next
    second = head.next.next
    # LinkedListの始まりをheadにする
    while first != second:
        first = first.next
        second = second.next.next
        print("first.value : ", first.value)
        print("second.value : ", second.value)
    first = head
    print("*******************")
    # ループの始まりをheadにする
    while first != second:
        first = first.next
        second = second.next
        print("first.value : ", first.value)
        print("second.value : ", second.value)
    return first
