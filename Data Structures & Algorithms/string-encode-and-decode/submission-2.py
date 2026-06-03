class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs ==[]:
            return "AbsolutelyNothing"
        megastring = ""
        for string in strs:
            megastring+=string+"`"
        return megastring[0:len(megastring)-1]
    def decode(self, s: str) -> List[str]:
        if s =="AbsolutelyNothing":
            return []
        ret =s.split("`")
        return ret
