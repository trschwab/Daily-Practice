
# Naive casting approach
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        i = 0
        while i < len(x) // 2:
            if x[i] != x[len(x) - 1 - i]:
                return False
            i += 1
        return True


# Great solution but can be refined more
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True

        divisor = 10
        check = x // divisor
        calculate = x

        while check >= 10:
            check = calculate // divisor
            if check >=10:
                divisor *= 10

        while True:
            if x < 10 and x >= 0:
                return True
            if x < 0:
                return False
            right_digit = x % 10

            left_digit = x // divisor

            if left_digit != right_digit:
                return False
            
            # Remove left digit from number
            x -= left_digit * divisor

            # Remove right digit from number
            x -= right_digit
            x = x / 10

            divisor = divisor // 10 // 10

            # In cases when we see a discrepancy
            # of the divisor and number we know that there
            # were leading 0's
            if x < 10 and divisor >= 10 and x != 0:
                return False

