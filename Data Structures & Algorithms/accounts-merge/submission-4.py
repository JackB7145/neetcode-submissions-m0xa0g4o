class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parents = [i for i in range(len(accounts))]
        number_to_name = {}
        seen = {}

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]

        def union(u, v):
            u = find(u)
            v = find(v)

            if u != v:
                parents[v] = u

        # Map account number -> name
        # Union accounts that share an email
        for i, account in enumerate(accounts):
            number_to_name[i] = account[0]

            for email in account[1:]:
                if email in seen:
                    union(seen[email], i)
                else:
                    seen[email] = i

        # Root account -> emails
        name_map = defaultdict(list)

        for email, account in seen.items():
            root = find(account)
            name_map[root].append(email)

        # Build answer
        res = []

        for root, emails in name_map.items():
            res.append([number_to_name[root]] + sorted(emails))

        return res