class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        Long  = str1 if len(str1) > len(str2) else str2
        Short = str1 if len(str1) <= len(str2) else str2
        ans = ""
        anss=[ans]


        if Short*(len(Long)//len(Short)) == Long:
            return Short

        for i in Short:
            ans += i
            if ans*(len(Long)//len(ans)) == Long and ans*(len(Short)//len(ans)) == Short: 
                anss.append(ans)
            
        return anss[-1]
