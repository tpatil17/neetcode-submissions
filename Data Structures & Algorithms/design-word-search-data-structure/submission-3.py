class WordDictionary:

    def __init__(self):
        self.char = ""
        self.children = {}
        self.isEnd = False
        

    def addWord(self, word: str) -> None:

        if len(word) < 1:
            self.isEnd = True
            return

        else:
            c = word[0]
            nxt = "" if len(word) <= 1 else word[1:]

            if c in self.children:
                self.children[c].addWord(nxt)
            else:
                new = WordDictionary()
                new.char = c
                self.children[c] = new
                self.children[c].addWord(nxt)

        

    def search(self, word: str) -> bool:

        if word == "":

            return self.isEnd
        else:
            c = word[0]
            nxt = "" if len(word) <= 1 else word[1:]

            if c == ".":
                for char in self.children:
                    val  = self.children[char].search(nxt)
                    if val != True:
                        continue
                    else:
                        return True
                
                return False
            else:
                if c not in self.children:
                    return False
                else:
                    return self.children[c].search(nxt)
            



    