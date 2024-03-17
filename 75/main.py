"""
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
"""

def reverseWords(self, s: str) -> str:
        s = self.trim_spaces(s)
        return self.reverse_string(s)

    def trim_spaces(self, s:str) -> str:
        final_list = []
        s_list = s.split(" ")
        for phrase in s_list:
            if phrase:
                final_list.append(phrase)
        print(final_list)
        return ' '.join(final_list)
    
    def reverse_string(self, s:str) -> str:
        reversed_str = []
        s_list = s.split(" ")
        for idx in range(len(s_list), 0,  -1):
            reversed_str.append(s_list[idx - 1])
        return ' '.join(reversed_str)

#runtime 43-s
#The runtime can be better using the builtin functions.