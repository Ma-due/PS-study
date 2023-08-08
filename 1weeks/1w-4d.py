class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        def union(a, b):
            a = find(a)
            b = find(b)

            if a < b:
                parents[b] = a
            else:
                parents[a] = b
            
        def find(x):
            if x not in parents:
                parents[x] = x
            
            if parents[x] != x:
                parents[x] = find(parents[x])
            
            return parents[x]

        parents = {}
        for c1, c2 in zip(s1, s2):
            union(c1, c2)
            print(c1, c2, parents)


        return ''.join([find(c) for c in baseStr])
