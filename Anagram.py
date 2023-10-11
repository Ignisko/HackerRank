if len(s) % 2 != 0:
        return -1

    # Split the input string into two equal parts
    mid = len(s) // 2
    s1, s2 = s[:mid], s[mid:]

    # Create dictionaries to count the frequency of characters in both substrings
    freq1 = {}
    freq2 = {}
    for char in s1:
        freq1[char] = freq1.get(char, 0) + 1
    for char in s2:
        freq2[char] = freq2.get(char, 0) + 1

    # Calculate the number of characters to change to make s1 an anagram of s2
    changes_needed = 0
    for char, count in freq2.items():
        if char not in freq1:
            changes_needed += count
        else:
            changes_needed += max(0, count - freq1[char])

    return changes_needed