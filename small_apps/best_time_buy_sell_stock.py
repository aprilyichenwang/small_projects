def maxProfit(prices):
    """
    :type prices: List[int],
    an array for which the ith element is the price of a given price of a given stock on day i
    :rtype: int
    """


    min = prices[0]
    ls=[]
    for i, price in enumerate(prices):
        if price < min:
            min=price
        if price >= min:
            ls.append(price-min)  # a profit is registered
    return max(ls)


def maxProfit2(prices):
    min=prices[0]
    profit_ls=[]
    for price in prices:
        if price <min:
            min=price
        if price > min:
            profit_ls.append(price-min)
            min=price
    return sum(profit_ls)



print maxProfit([7, 6, 4, 3, 1])
print maxProfit([7, 1, 5, 3, 6, 4])

# say I can only buy one and sell one, find max profit

print maxProfit2([7, 6, 4, 3, 1])
print maxProfit2([7, 1, 5, 3, 6, 4])