class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = False
        length = len(digits) - 1

        while length >= 0:
            if carry:
                digits[length] += 1
                carry = False

            if length == len(digits)-1:
                digits[length] += 1

            if digits[length] == 10:
                digits[length] = 0
                carry = True

            length -= 1

        if carry:
            digits.insert(0, 1)

        return digits
