
"""
QUESTION:
Given two strings needle and haystack, return the index of the first 
occurrence of needle in haystack. If needle is not found, return -1.
Example:
haystack = "sadbutsad", needle = "sad" → output: 0
haystack = "leetcode", needle = "leeto" → output: -1
SOLUTION:
"""
def strStr(haystack, needle):
    if needle == "":
        return 0

    h_len = len(haystack)
    n_len = len(needle)

    for i in range(h_len - n_len + 1):
        if haystack[i:i+n_len] == needle:
            return i
    return -1

haystack = "sadbutsad"
needle = "sad"
result = strStr(haystack, needle)
print("Output:", result)