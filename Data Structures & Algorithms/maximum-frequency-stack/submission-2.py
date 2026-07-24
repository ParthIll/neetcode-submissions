class FreqStack:

    def __init__(self):
        self.freq={}
        self.infreq={}
        self.mfreq=0
    def push(self, val: int) -> None:
        if val not in self.freq:
            self.freq[val]=0
        self.freq[val]+=1
        '''if self.freq[val]-1 in self.infreq:
            self.infreq[self.freq[val]-1].remove(val)'''
        if self.freq[val] not in self.infreq :
            self.mfreq=self.freq[val]
            self.infreq[self.freq[val]]=[]
        self.infreq[self.freq[val]].append(val)
        

    def pop(self) -> int:
        top=self.infreq[self.mfreq][-1]
        '''if self.mfreq>1:
            self.infreq[self.mfreq-1].append(top)'''
        self.freq[top]-=1
        self.infreq[self.mfreq].pop()
        if not self.infreq[self.mfreq]:
            self.mfreq-=1
            del self.infreq[self.mfreq+1]
        return top
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()