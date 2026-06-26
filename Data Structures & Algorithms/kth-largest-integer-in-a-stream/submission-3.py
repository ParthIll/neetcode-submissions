class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.kval = k
        self.numList = [0]*k
        for i in range(k):
            try:
                self.numList[i] = nums.pop(nums.index(max(nums)))
            except:
                self.numList[i] = -9000

    def add(self, val: int) -> int:
        if val>=self.numList[-1]:
            self.numList.append(val)
            self.numList.sort(reverse=True)
            self.numList.pop()
            print(self.numList)
            return self.numList[-1]
            
        else:
            return self.numList[-1]   
