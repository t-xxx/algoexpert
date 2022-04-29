# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    print(head.next.value, k)
    counter = 1
    first = head
    second = head
    print(second.next.value)

    # 削除対象のnextをsecondに格納
    while counter <= k
    second = second.next
    counter += 1

    # 最終番目(今回だと10番目)の場合、second.nextは最後のnullを示すため、以下の条件となる
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return
        # 以下、nextに進むに従って最終的にnullになるまでfirstを更新。
        # 止まったところでfirstの2つ先のnextとvalueに更新する。
    while second.next is not None:
        second = second.next
        first = first.next
        print(first.next.value, first.value)
    first.next = first.next.next
