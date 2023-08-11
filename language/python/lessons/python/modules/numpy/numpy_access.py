import numpy as np

# ------------------------------------------------------------------
# Iterate


L = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 6],
    [1, 2, 3, 4, 7],
    [1, 2, 3, 4, 8],
]

N = np.array(L)


for x in N:
    for y in x:
        print(y, end=" - ")
# 1 - 2 - 3 - 4 - 5 - 1 - 2 - 3 - 4 - 6 - 1 - 2 - 3 - 4 - 7 - 1 - 2 - 3 - 4 - 8 -


print()


for x in N.reshape(-1):
    print(x, end=" * ")
# 1 * 2 * 3 * 4 * 5 * 1 * 2 * 3 * 4 * 6 * 1 * 2 * 3 * 4 * 7 * 1 * 2 * 3 * 4 * 8 *


print()


for x in np.nditer(N):
    print(x, end=" ^ ")
# 1 ^ 2 ^ 3 ^ 4 ^ 5 ^ 1 ^ 2 ^ 3 ^ 4 ^ 6 ^ 1 ^ 2 ^ 3 ^ 4 ^ 7 ^ 1 ^ 2 ^ 3 ^ 4 ^ 8 ^


for index, item in np.ndenumerate(N):
    print(index, item)
"""
(0, 1) 2
(0, 2) 3
(0, 3) 4
(0, 4) 5
(1, 0) 1
(1, 1) 2
(1, 2) 3
(1, 3) 4
(1, 4) 6
(2, 0) 1
(2, 1) 2
(2, 2) 3
(2, 3) 4
(2, 4) 7
(3, 0) 1
(3, 1) 2
(3, 2) 3
(3, 3) 4
(3, 4) 8
"""