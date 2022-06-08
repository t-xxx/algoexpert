# "未整列な配列"から1つずつ値を取り出し"整列済み配列"の適切な位置に挿入する
# 前から順に2つの数値を比べて昇順に並べ替えていく方法

def insertionSort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            swap(j, j-1, array)
            j -= 1
    return array


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
