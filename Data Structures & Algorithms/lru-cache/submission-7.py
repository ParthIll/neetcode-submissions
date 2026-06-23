class LRUCache:

    def __init__(self, capacity: int):
        self.Cached = {}
        self.cachedList=[]
        self.left = capacity

    def get(self, key: int) -> int:
        if key in self.Cached:
            
            self.cachedList.remove(key)
            self.cachedList.append(key)
            return self.Cached[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.Cached:
            self.Cached[key] =value
            self.cachedList.remove(key)
            self.cachedList.append(key)
            return
        self.left-=1
        if self.left<0:
            del self.Cached[self.cachedList.pop(0)]
            self.left=0
        self.Cached[key]=value
        self.cachedList.append(key)
        print(self.Cached)
        print(self.cachedList)
