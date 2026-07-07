class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        coins.sort(reverse=True)
        q=deque()
        for coin in coins:
            q.append((coin,1))
        reached = set()
        while q:
            coin=q.popleft()
            if coin[0] in reached:
                continue
            
            reached.add(coin[0])
            
            if amount==coin[0]:
                return coin[1]
            if amount-coin[0] in coins:
                return coin[1]+1
            else:
                for c in coins:
                    if c+coin[0]<amount:
                        q.append((c+coin[0],coin[1]+1))
        return -1