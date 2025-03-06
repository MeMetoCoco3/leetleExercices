"""
64. Group Anagrams

Write a function solve that groups anagrams together.

Example:
Input: ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
"""


def solve(strs):
    def isanagram(a, b):
        if len(a) != len(b):
            return False
        return sorted(a) == sorted(b)

    if not strs:
        return []
    anags = []
    anags.append([strs[0]])
    if len(strs) == 1:
        return anags
    breakpoint()
    for i in strs[1:]:
        is_anag = False
        for j in range(len(anags)):
            if isanagram(i, anags[j][0]):
                anags[j].append(i)
                is_anag = True
                continue
        if not is_anag:
            anags.append([i])
    return anags


print(solve(["eat", "tea", "tan", "ate", "nat", "bat"]))
