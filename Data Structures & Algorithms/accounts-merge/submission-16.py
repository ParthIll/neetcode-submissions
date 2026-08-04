class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        accs=defaultdict(list)
        accounts.sort()
        x=1
        for acc in accounts:
            print(accs)
            if acc[0] not in accs:
                accs[acc[0]].append(set(acc[1:]))
            else:
                added=False
                for i in range(len(accs[acc[0]])):
                    if set(acc[1:]) & accs[acc[0]][i]:
                        accs[acc[0]][i]|=set(acc[1:])
                        added=True
                        break
                if not added:
                    accs[acc[0]].append(set(acc[1:]))
                added=False
        def merge_intersecting_sets(set_list):
            i = 0
            while i < len(set_list):
                j = i + 1
                while j < len(set_list):
                    if not set_list[i].isdisjoint(set_list[j]):
                        set_list[i] |= set_list[j]
                        set_list.pop(j)
                        i = 0
                        j = 1
                    else:
                        j += 1
                i += 1
            return set_list       
        ret=[]
        for k in accs:
            accs[k]=merge_intersecting_sets(accs[k])
            for j in accs[k]:
                inret=[]
                inret.append(k)
                inret.extend((list(j)))
                ret.append(inret)
        return ret