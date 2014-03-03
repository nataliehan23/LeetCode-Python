# Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

# For example,
# Given n = 3, there are a total of 5 unique BST's.

#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3

class Solution:
    # @return an integer
    def numTrees(self, n):
        num = [0]*(n+1)
        if n == 0:
            return 1
        if n == 1:
            return 1
        num[0] = 1
        num[1] = 1
        for i in range(2,n+1):
            for j in range(0,i):
                num[i] += num[j] * num[i-j-1]
        return num[-1]
            