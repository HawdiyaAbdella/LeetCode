class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer =""
        strs.sort()
        for i in range(len(strs[0])):
            if strs[0][i]!=strs[-1][i]:
                return answer
            else:
                answer +=strs[0][i]
        return answer
          
