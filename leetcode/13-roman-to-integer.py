
# First look
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        conversion_vals = {
            "I": 1,
            "V": 5,
            "X": 10, 
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        sum = 0
        for index, numeral in enumerate(s):
            val = conversion_vals[numeral]
            if index < len(s)-1:
                next_val = conversion_vals[s[index+1]]
                if next_val > val:
                    sum -= val
                else:
                    sum += val
            else:
                sum += val

        return sum
