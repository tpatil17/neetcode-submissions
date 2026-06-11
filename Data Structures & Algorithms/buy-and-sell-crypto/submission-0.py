class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = 0
        sell = buy+1

        profit = 0

        while sell < len(prices):

            profit = max(prices[sell]-prices[buy], profit)

            print(profit)

            if prices[sell] < prices[buy]:
                buy = sell
                sell = buy+1
            else:
                sell+=1
        
        return profit



        