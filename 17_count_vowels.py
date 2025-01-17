"""
17. Count Vowels


Write a function solve that counts the number of vowels (a,e,i,o,u) in a string, ignoring case.
"""


def solve(text):
    vowel = "aeiou"
    count = 0
    for i in text.lower():
        if i in vowel:
            count += 1

    return count
