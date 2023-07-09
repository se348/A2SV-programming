from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = defaultdict(str)
        emailOwner, rank = defaultdict(str), defaultdict(lambda: 1)
        for account in accounts:
            owner, emails = account[0], account[1:]
            for email in emails:
                emailOwner[email] = owner
                parent[email] = email
        
        def find(email):
            p = parent[email]
            while p != parent[p]:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(e1, e2):
            p1, p2 = find(e1), find(e2)
            if p1 == p2: return
            if rank[p1] > rank[p2]:
                parent[p2] = p1
                rank[p1] += rank[p2]
            else:
                parent[p1] = p2
                rank[p2] += rank[p1]
        
        for account in accounts:
            for i in range(1, len(account) - 1):
                union(account[i], account[i + 1])

        merged = defaultdict(list)
        for child, par in parent.items():
            merged[find(par)].append(child)

        res = []
        for emails in merged.values():
            curr = [emailOwner[emails[0]]]
            curr.extend(sorted(emails))
            res.append(curr)

        return res