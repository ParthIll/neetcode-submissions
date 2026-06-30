class TrieNode:
    def __init__(self):
        self.children ={}
        self.endOfWord= False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur=cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        print(word)
        cur = self.root
        for i in range(len(word)):
            c=word[i]
            if c != "." and c not in cur.children:
                return False
            if c!=".":
                cur=cur.children[c]
            else:
                for child in cur.children:
                    newWord= list(word)
                    newWord[i] = child
                    finWord = "".join(newWord)
                    if self.search(finWord):
                        return True
                return False
         
        return cur.endOfWord
