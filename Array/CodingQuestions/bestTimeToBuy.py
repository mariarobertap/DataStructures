#. 121. Best Time to Buy and Sell Stock

#Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

#Note: Use a left and right pointer to a linear solution

#Big O notation: Time O(n): Memory: O(1)

#######################################

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        
        profit = 0
        result = 0
        leftPointer = 0
        
        for rightPointer in range(len(prices)):
            
            if(prices[leftPointer] > prices[rightPointer]):
                leftPointer = rightPointer
                
            else:
                profit = prices[rightPointer] - prices[leftPointer]
                result = max(profit, result)
                
        return result
            
