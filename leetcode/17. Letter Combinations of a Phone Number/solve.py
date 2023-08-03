class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keys = {
            "2" : ["a","b","c"] ,
            "3" : ["d","e","f"] ,
            "4" : ["g","h","i"] ,
            "5" : ["j","k","l"] ,
            "6" : ["m","n","o"] ,
            "7" : ["p","q","r","s"] ,
            "8" : ["t","u","v"] ,
            "9" : ["w","x","y","z"]
            }
        ans = [""]

        def any(list1,list2):
            res = []
            for i in list1 :
                for j in list2 :
                    res.append(j+i)
            return res

        for i in digits:
            ans = any(keys[i],ans)

        if ans == [""] :
            return []
        return ans
