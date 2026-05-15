class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            else:
                ganancia = prices[i] - min_price
                if ganancia > max_profit:
                    max_profit = ganancia
        return max_profit
