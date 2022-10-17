class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for i in "abcdefghijklmnopqrstuvwxyz" :
            if i not in sentence:
                return False
        return True
