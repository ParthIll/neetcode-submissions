class MyHashSet:

    def __init__(self):
        self.nums={}

    def add(self, key: int) -> None:
        self.nums[key]=1

    def remove(self, key: int) -> None:
        self.nums[key]=0

    def contains(self, key: int) -> bool:
        return key in self.nums and self.nums[key]==1


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)