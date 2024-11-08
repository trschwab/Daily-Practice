
# First look
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # cast to lowercase
        s = s.lower()

        # cast to alphanumeric 
        alpha_s = ""
        for element in s:
            if (ord(element) >= ord("a") and ord(element) <= ord("z")) or (element in "1234567890"):
                alpha_s += element
        
        if alpha_s == "":
            return True
        
        i = 0
        j = len(alpha_s) - 1
        while i < j:
            if alpha_s[i] != alpha_s[j]:
                return False
            i += 1
            j -= 1
        return True


# Optimize 1
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        while i < j:
            left = self.isAlphanumeric(s[i])
            right = self.isAlphanumeric(s[j])
            if left == None:
                i += 1
            if right == None:
                j -= 1
            if left != None and right != None:
                if left != right:
                    return False
                i += 1
                j -= 1
        return True

    def isAlphanumeric(self, c):
        c = c.lower()
        if (ord(c) >= ord("a") and ord(c) <= ord("z")) or (c in "1234567890"):
            return c
        else:
            return None
