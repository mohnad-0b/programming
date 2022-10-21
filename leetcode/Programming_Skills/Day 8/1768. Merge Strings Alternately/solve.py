class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        marg_word = ""
        
        if len(word1) == len(word2) :

            for i in range(len(word1)+len(word2)):
                if i%2 == 0:
                    marg_word += word1[i//2]
                else :
                    marg_word += word2[i//2]
        elif len(word1) > len(word2):

            for i in range(len(word2)+len(word2)):
                if i%2 == 0:
                    marg_word += word1[i//2]
                else :
                    marg_word += word2[i//2]
            marg_word += word1[len(word2):]
        elif len(word2) > len(word1):

            for i in range(len(word1)+len(word1)):
                if i%2 == 0:
                    marg_word += word1[i//2]
                else :
                    marg_word += word2[i//2]
            marg_word += word2[len(word1):]
        
        return "".join(marg_word)