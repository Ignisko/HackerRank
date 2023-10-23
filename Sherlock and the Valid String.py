from collections import Counter
#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#



def isValid(s):
    char_freq = Counter(s)
    
    freq_count = Counter(char_freq.values())
    
    if len(freq_count) == 1:
        return "YES"
        
    if len(freq_count) == 2:
        freq1, freq2 = freq_count.keys()
        if freq_count[freq1] == 1:
            if freq1 == 1 or freq1 - freq2 == 1:
                return "YES"
        if freq_count[freq2] == 1:
            if freq2 == 1 or freq2 - freq1 == 1:
                return "YES"
    
    return "NO"
    
    