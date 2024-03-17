"""
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
"""


def gcdOfStrings(self, str1: str, str2: str) -> str:
    if not str1 or not str2:
        return str1 if not str2 else str2

    if len(str2) > len(str1):
        return self.gcdOfStrings(str2, str1)

    if str1.startswith(str2):
        return self.gcdOfStrings(str1[len(str2) :], str2)

    return ""

#runtime - 33ms
#The idea is that the first string will always be the largest one.
#Using recursion we can reach the result.
#First we check if any of the strings are empty.
#Then we check if str2 is larger then str1. If it happens to be, we reverse the string call order.
#After, we check if str1 contains str2, and we split str1 by then length of str2.
#In the end, if one of the strings are empty, and the other isn't, it means the GCD was found.