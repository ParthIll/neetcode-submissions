class FreqStack:

    def __init__(self):
        self.freq=defaultdict(int)
        self.infreq=defaultdict(list)
        self.mfreq=0
    def push(self, val: int) -> None:
        self.freq[val]+=1
        if not self.infreq[self.freq[val]] :
            self.mfreq=self.freq[val]
        self.infreq[self.freq[val]].append(val)
        

    def pop(self) -> int:
        top=self.infreq[self.mfreq].pop()
        self.freq[top]-=1
        
        if not self.infreq[self.mfreq]:
            self.mfreq-=1
        return top
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()