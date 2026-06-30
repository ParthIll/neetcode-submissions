class PrefixTree:

    def __init__(self):
        self.wordList = []

    def insert(self, word: str) -> None:
        self.wordList.append(word)

    def search(self, word: str) -> bool:
        if word in self.wordList:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        for word in self.wordList:
            if word[:len(prefix)]==prefix:
                return True
        return False
        