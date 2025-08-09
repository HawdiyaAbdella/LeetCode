class Solution:
    def isPalindrome(self, x: int) -> bool:
       x= str(x)
       x = list(x)
       if x== list(reversed(x)):
          return True
       else:
          return False