def nonConstructibleChange(coins):
    coins.sort()

    counter = 0
    for coin in coins:
        print(coin, counter)
        if coin > counter + 1:
            print(coin, counter)
            return counter + 1
        counter += coin

    print(counter + 1)
    return counter + 1
