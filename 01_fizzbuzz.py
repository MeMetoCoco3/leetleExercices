def solve(n):
    result = []
    for i in range(n + 1):
        j = ""
        if i % 3 == 0:
            j += "Fizz"
        if i % 5 == 0:
            j += "Buzz"
        if j == "":
            result.append(i)
            continue
        result.append(j)
    return result
