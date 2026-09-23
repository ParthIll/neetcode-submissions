class Solution:
    def climbStairs(self, n: int) -> int:
        cache={}
        def foo(num):
            if num in cache:
                return cache[num]
            if num>n:
                return 0
            elif num==n:
                return 1
            else:
                save = foo(num+1)+foo(num+2)
                cache[num]=save
                return save
        return foo(0)     