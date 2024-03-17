"""
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
"""

def reverseVowels(self, s: str) -> str:
        s_list = []
        found_vowels = []
        vowels = ['a','A','e','E','i','I','o','O','u','U']
        for letter in list(s):
            if letter in vowels:
                found_vowels.append(letter)
        for letter in list(s):
            if letter in vowels:
                s_list.append(found_vowels.pop(-1))
                continue
            s_list.append(letter)
        return ''.join(s_list)

#runtime - 48ms
#We define a vowel list, a list of all vowels found in the string and a list to be returned.
#We simply add all vowels found to a list, then we iterate the string again
#but this time, at each vowel found, we replace it with the vowels found in the reverse order.