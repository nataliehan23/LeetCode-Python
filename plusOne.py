# Given a non-negative number represented as an array of digits, plus one to the number.

# The digits are stored such that the most significant digit is at the head of the list.


class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        carry = 0
        i = len(digits)-1
        if digits[-1]==9:
            carry = 1
        while i > 0:
            if digits[i]+carry <= 9:
                digits[i] += 1
                carry = 0
                break
            else:
                digits[i] = 0
                carry = 1
                i -= 1
        if i == 0:
            if digits[i] < 9:
                digits[i] += 1
            else:
                digits[i] = 0
                digits.insert(0,1)
        return digits
      