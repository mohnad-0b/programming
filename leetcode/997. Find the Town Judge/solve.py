class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        persons = []
        
        if n == 1 : return 1

        sum_of_n = sum([i for i in range(1,n+1)])

        for person in trust : 
            if person[0] not in persons :
                persons.append(person[0])
        
        trust_no_one = sum_of_n - sum(persons)
        if not trust_no_one : return -1

        scor_trust = 0
     
        for person in trust : 
            if person[1] == trust_no_one :
                scor_trust += 1 
                if scor_trust == n -1:
                    return trust_no_one

        return -1
