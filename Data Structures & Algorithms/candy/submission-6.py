class Solution:
    def candy(self, ratings: List[int]) -> int:
        candList = [1]*len(ratings)
        for i in range(len(ratings)-1):
            if ratings[i]>ratings[i+1]:
                candList[i]+=1
        for i in range(len(ratings)-1,0,-1):
            if ratings[i]>ratings[i-1] and candList[i]==candList[i-1]:
                candList[i]+=1
        for i in range(len(candList)):
            if i-1 in range(len(candList)) and ratings[i]>ratings[i-1]:
                candList[i] = max(candList[i],candList[i-1]+1)
            if i+1 in range(len(candList)) and ratings[i]>ratings[i+1]:
                candList[i] = max(candList[i],candList[i+1]+1)
        for i in range(len(candList)-1,-1,-1):
            if i-1 in range(len(candList)) and ratings[i]>ratings[i-1]:
                candList[i] = max(candList[i],candList[i-1]+1)
            if i+1 in range(len(candList)) and ratings[i]>ratings[i+1]:
                candList[i] = max(candList[i],candList[i+1]+1)
        
        return sum(candList)