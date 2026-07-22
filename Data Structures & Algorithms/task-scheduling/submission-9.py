class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        cCount = Counter(tasks)
        fCount = Counter(cCount.values())
        maxf = max(fCount.keys())
        maxCount = fCount[maxf]

        time = (maxf - 1) * (n + 1) + maxCount
        return max(len(tasks), time)