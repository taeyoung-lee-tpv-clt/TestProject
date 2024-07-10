def change(n, coinArr):
    if(n == 0): return 0
    best = -1
    for coin in coinArr:
        if(coin <= n):
            nextTry = change(n - coin, coinArr)
        if(best < 0 or best > nextTry + 1):
            best = nextTry + 1
    return best