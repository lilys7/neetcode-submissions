class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    #addword is just adding the characters of the word, each as a child of the prev
    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True
    def search(self, word: str) -> bool:
        def dfs(j,root):
            cur = root
            for i in range(j, len(word)):
                c = word[i]
                if c == '.':
                    #we wanna do dfs on every possible trie tree under all the letters in the children to see if we can finish the word
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.endOfWord
        return dfs(0, self.root)

