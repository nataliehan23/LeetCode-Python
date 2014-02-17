class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        seen = {}
        for i in range(len(num)):
            res = target -num[i]
            if res not in seen:
                seen[num[i]] = i+1
            else:
                return seen[res], i+1
                
                
        