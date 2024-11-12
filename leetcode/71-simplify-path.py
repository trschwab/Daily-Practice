class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = []

        path_split = path.split("/")

        for element in path_split:
            if element != "":
                if element == "..":
                    if len(stack) > 0:
                        stack.pop()
                    else:
                        continue
                elif element == ".":
                    continue
                else:
                    stack.append(element)
        
        if len(stack) == 0:
            return "/"

        path = "/".join([""] + stack)
        return path
