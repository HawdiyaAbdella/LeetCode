# Note: these codes are a python version of this youtube video
# https://www.youtube.com/watch?v=qBbZ3tS0McI

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def backtrack(ans, curr, openp, closep, maxp):
            if len(curr) == 2*maxp:
                ans.append(curr)
            if openp < maxp:
                backtrack(ans, curr+'(', openp+1, closep, maxp)
            if closep < openp:
                backtrack(ans, curr+')', openp, closep+1, maxp)
        
        ans = []
        openp, closep = 0, 0
        curr = ''
        backtrack(ans, curr, openp, closep, n)
        return ans