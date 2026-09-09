class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parents = [i for i in range(len(accounts))]

        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]

        def union(u, v):
            a, b = find(u), find(v)

            if a != b:
                parents[b] = a

        seen = {}
        number_to_name = {}

        # Build Union-Find relationships
        for i in range(len(accounts)):
            number_to_name[i] = accounts[i][0]

            for j in range(1, len(accounts[i])):
                email = accounts[i][j]

                if email in seen:
                    union(seen[email], i)
                else:
                    seen[email] = i

        # Group emails by their root account
        name_to_email = defaultdict(list)

        for email, account in seen.items():
            parent = find(account)
            name_to_email[parent].append(email)

        # Build result
        res = []

        for parent in name_to_email:
            emails = sorted(name_to_email[parent])
            res.append([number_to_name[parent]] + emails)

        return res