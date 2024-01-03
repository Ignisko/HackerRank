def noPrefix(words):
    """Checks if a set of words has no prefixes of each other."""

    def insert(trie, word):
        """Inserts a word into a trie data structure."""
        for i, char in enumerate(word):
            if char in trie:
                if trie[char]['*'] or i == len(word) - 1:
                    return True  # Prefix or full word already exists
            else:
                trie[char] = {}  # Create a new nested dictionary for the character node
                trie[char]['*'] = i == len(word) - 1  # Mark as end if it's the full word
            trie = trie[char]  # Continue traversing the trie

        return False

    trie = {}  # Initialize empty trie
    for word in words:
        if insert(trie, word):
            print("BAD SET")
            print(word)
            return

    print("GOOD SET")



if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
