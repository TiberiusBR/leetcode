"""

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1.
 If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

"""


def merge_alternately(self, word1: str, word2: str) -> str:
    f_list = []
    i = 0
    iterator = max(len(word1), len(word2))
    while i < iterator:
        if i < len(word1):
            f_list.append(word1[i])
        if i < len(word2):
            f_list.append(word2[i])
        i += 1
    return "".join(f_list)


# Runtime - 32ms
# Get the biggest word lenght for iterating purposes.
# Starting with the first word, append one by one.
# If the iterator surpasses the lesser word length (or both if they have the same one), it won't append.
