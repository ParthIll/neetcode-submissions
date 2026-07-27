class LFUCache:

    def __init__(self, capacity: int):
        self.freq=defaultdict(int)
        self.infreq=defaultdict(list)
        self.kmap={}
        self.at=0
        self.cap=capacity

    def get(self, key: int) -> int:
        if key not in self.kmap:
            return -1
        ret = self.kmap[key]
        self.freq[key]+=1
        self.infreq[self.freq[key]-1].remove(key)
        if not self.infreq[self.freq[key]-1]:
            del self.infreq[self.freq[key]-1]
        self.infreq[self.freq[key]].append(key)
        return ret

    def put(self, key: int, value: int) -> None:
        if key in self.kmap or self.at<self.cap:
            if key not in self.kmap:
                self.at+=1
            self.freq[key]+=1
            if self.freq[key]>1:
                self.infreq[self.freq[key]-1].remove(key)
                if not self.infreq[self.freq[key]-1]:
                    del self.infreq[self.freq[key]-1]
            self.infreq[self.freq[key]].append(key)
            self.kmap[key]=value
        else:
            print(key,value)
            minused = min(self.infreq.keys())
            minkey = self.infreq[minused].pop(0)
            del self.freq[minkey]
            del self.kmap[minkey]
            self.freq[key]+=1
            if self.freq[key]>1:
                self.infreq[self.freq[key]-1].remove(key)
                if not self.infreq[self.freq[key]-1]:
                    del self.infreq[self.freq[key]-1]
            self.infreq[self.freq[key]].append(key)
            self.kmap[key]=value


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)