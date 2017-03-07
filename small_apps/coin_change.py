import sys

# HARD, DON'T GET IT

def make_change(coins, n):
    coins.sort()
    results = [0 for _ in range(n + 1)]
    # initiate results[0, 0, 0, 0] # 0 ways to get money n, using coin i
    results[0] = 1
    for coin in coins:
        for i in range(coin, n + 1):
            results[i] += results[i - coin]
    print results
    return results[n]


n, m = raw_input().strip().split(' ')
# n, a number of dollars
# m, number of distinct coins
n, m = [int(n), int(m)]
coins = map(int, raw_input().strip().split(' '))
# a list of dollar values for m distinct coins
print make_change(coins, n)


# find & print the number of different ways I can make change for n dollars

