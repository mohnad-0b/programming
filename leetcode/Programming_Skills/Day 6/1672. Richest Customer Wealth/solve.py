class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max = 0
        for account in accounts:
            wealth = 0
            for n in account :
                wealth += n
            if wealth > max :
                max = wealth
        return max