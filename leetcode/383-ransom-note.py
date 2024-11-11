
# First look
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        h = {}
        for element in magazine:
            if element in h.keys():
                h[element] += 1
            else:
                h[element] = 1
        
        for r in ransomNote:
            if r in h.keys():
                if h[r] > 0:
                    h[r] -= 1
                else:
                    return False
            else:
                return False
        return True

# Noteable boost in efficiency from using collections.Counter(magazine):
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        lookup = collections.Counter(magazine)

        for element in ransomNote:
            if element in lookup.keys():
                if lookup[element] > 0:
                    lookup[element] -= 1
                else:
                    return False
            else:
                return False

        return True
