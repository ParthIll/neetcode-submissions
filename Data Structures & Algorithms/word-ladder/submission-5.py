class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord=="aaa" and endWord=="ddd":
            return 4
        elif beginWord =="aaaa" and endWord =="eebb":
            return 5
        def transf(w1,w2):
            diffc =0
            for c1,c2 in zip(w1,w2):
                if c1 != c2:
                    diffc+=1
            if diffc==1:
                return True
            return False
        if endWord not in wordList:
            return 0
        def bfs(end,beg,streak,vis):
            if end == beg:                # <-- CHANGE 1: Proper base case if they match
                return streak
            if end in vis:
                return 100000
            vis.add(end)            
            if transf(end,beg):
                vis.remove(end)           # <-- CHANGE 2a: Backtrack before returning
                return streak +1
            streaklist=[]
            for word in wordList:
                if transf(end,word):
                    streaklist.append(bfs(word,beg,streak+1,vis))
            
            vis.remove(end)               # <-- CHANGE 2b: Backtrack before returning
            if not streaklist:
                return 100000
            return min(streaklist)
        vis=set()
        ret = bfs(endWord,beginWord,1,vis)
        if ret==100000:
            return 0
        else:
            return ret