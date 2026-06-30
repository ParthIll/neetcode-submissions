class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digiMap = {
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"}
        res =[]
        if not digits:
            return res
        def dfs(s,i):
            if i==len(digits):
                res.append(s)
                return
            for j in range(len(digiMap[int(digits[i])])):
                dfs(s+digiMap[int(digits[i])][j],i+1)
        dfs("",0)
        return res