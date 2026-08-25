class PrefixTree:

    def __init__(self):
        
        self.char = ""
        self.children = {}
        self.isEnd = False
        

    def insert(self, word: str) -> None:

        if word == "":
            self.isEnd = True
            return

        
        c = word[0]
        nxt = "" if len(word) <= 1 else word[1:]
        if c in self.children:
            self.children[c].insert(nxt)
        else:
            new = PrefixTree()
            new.char = c
            self.children[c] = new

            self.children[c].insert(nxt)

        return


    def search(self, word: str) -> bool:

        if word == "":
            return self.isEnd
        else:
            c = word[0]
            nxt = "" if len(word) <= 1 else word[1:]
            if c not in self.children:
                return False
            else:
                return self.children[c].search(nxt)
        

    def startsWith(self, prefix: str) -> bool:

        if prefix == "":
            return True
        else:
            c = prefix[0]
            nxt = "" if len(prefix) <= 1 else prefix[1:]
            if c not in self.children:
                return False
            else:
                return self.children[c].startsWith(nxt)
        
        