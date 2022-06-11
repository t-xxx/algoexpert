def productSum(array, multiplier=1):
    prod_sum = 0
    for element in array:
        if type(element) is list:
            prod_sum += productSum(element, multiplier + 1)
        else:
            prod_sum += element
    return prod_sum * multiplier
