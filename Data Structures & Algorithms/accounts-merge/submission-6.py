class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        for p in range(len(accounts)):
            i=0
            l=len(accounts)
            
            shouldbreak=False
            while i<l:
                orig=accounts[i]
                orset=set()
                new=[]
                for x in orig[1:]:
                    if x not in orset:
                        new.append(x)
                        orset.add(x)
                accounts[i]=[orig[0]]
                accounts[i].extend(new)
                orig=accounts[i]
                for j in range(i+1,len(accounts)):
                    
                    if shouldbreak:
                        shouldbreak=False
                        break
                    acc = accounts[j]
                    if acc[0]==accounts[i][0]:
                        for s in orig[1:]:
                            if shouldbreak:
                                break
                            if s in acc[1:]:
                                for f in acc[1:]:
                                    if f not in orig[1:]:
                                        orig.append(f)
                                accounts.pop(j)
                                l-=1
                                shouldbreak=True
                i+=1
        return accounts