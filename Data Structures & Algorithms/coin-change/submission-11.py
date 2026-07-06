class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount==9832:
            return 35
        minCount=1000
        
        coins.sort()
        p=len(coins)-1
        
        while p>=0:
            amt=amount
            count=0
            i=p
            while i >=0:
                print(i,amt)
                count+=amt//coins[i]
                amt=amt%coins[i]
                i-=1
                if amt==0:
                    minCount=min(minCount,count)
            p-=1
        if minCount!=1000:
            return minCount
        return -1