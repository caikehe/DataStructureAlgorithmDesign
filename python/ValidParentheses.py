class Solution:
    # @return a boolean
    def isValid(self, s):
        stack = []
        left = "([{"
        for item in s:
            if item in left:
                stack.append(item)
            else:
                if len(stack) == 0 or not self.match(stack.pop(),item):
                    return False
        return len(stack) == 0
            
    def match(self, s1, s2):
        left = "([{"
        right = ")]}"
        return left.find(s1) == right.find(s2)

s = "()[]{}"
so = Solution()
print so.isValid(s)
