class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        result = []
        p = [i for i in range(1, m + 1)]
        
        for i in queries:
            idx = p.index(i)
            result.append(idx)
            num = p.pop(idx)
            p = [num] + p
            
        return result
