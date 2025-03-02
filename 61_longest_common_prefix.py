def solve(strs):
    if not strs:
        return ""
    if len(strs) == 1:
        return strs[0]
    longest = strs[0]

    def longest_prefix(s1, s2):
        shortest_len = min(len(s1), len(s2))
        pref = ""
        for i in range(shortest_len):
            if s1[i] == s2[i]:
                pref += s1[i]
                continue
            break
        return pref

    for s in strs[1:]:
        longest = longest_prefix(s, longest)
    return longest


def solve2(strs):
    shortest = min(strs, key=len)
    for idx, char in enumerate(shortest):
        for other in strs:
            if other[idx] != char:
                shortest = shortest[:idx]

    return shortest


print(solve2(["flower", "flow", "flight"]))
