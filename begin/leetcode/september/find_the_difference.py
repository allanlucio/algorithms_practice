class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        temp=t
        for char in s:
            temp=temp.replace(char,"",1)
        return temp
