def findThreeLargestNumbers(array):
    # 動的計画法のように結果の数だけリストを準備
    threeLargest = [None, None, None]

    # updateLargest関数の中でひとつづつ数値の大きさを確認する
    for num in array:
        updateLargest(threeLargest, num)
    return threeLargest


def updateLargest(threeLargest, num):
    # idx==2 がnullの時または、数値がその時のarrayの値より大きい時は格納する。
    if threeLargest[2] is None or num > threeLargest[2]:
        shiftAndUpdate(threeLargest, num, 2)
    elif threeLargest[1] is None or num > threeLargest[1]:
        shiftAndUpdate(threeLargest, num, 1)
    elif threeLargest[0] is None or num > threeLargest[0]:
        shiftAndUpdate(threeLargest, num, 0)


def shiftAndUpdate(array, num, idx):

    # 前から昇順になるように値を入れ直す。
    # idxの位置にnumを入れてelseで残りを大きい値として格納していく。
    for i in range(idx + 1):
        if i == idx:
            array[i] = num
        else:
            array[i] = array[i + 1]
