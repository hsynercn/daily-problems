
def staircase(n):
    FibArray = [0, 1, 2]

    while len(FibArray) < n + 2:
        FibArray.append(0)

    if n <= 2:
        return n
    else:
        if FibArray[n - 1] == 0:
            FibArray[n - 1] = staircase(n - 1)

        if FibArray[n - 2] == 0:
            FibArray[n - 2] = staircase(n - 2)
    FibArray[n] = FibArray[n - 2] + FibArray[n - 1]
    return FibArray[n]

# Fill this in.

print staircase(4)
# 5
print staircase(5)
# 8