class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:

        arr = sorted(arr)
        ones = {}

        for i in arr :
            c = 0
            for j in str(bin(i))[2:]:
                if j == "1" :
                    c += 1
            if i not in list(ones) :
                ones[i] = [c,1]
            else :
                ones[i] = [c,ones[i][-1]+1]

        new_arr = []

        for  i in (sorted(ones.items(), key=lambda x: (x[1][0],x[0]))):
            for _ in range(i[-1][-1]):
                new_arr.append(i[0])

        return new_arr
