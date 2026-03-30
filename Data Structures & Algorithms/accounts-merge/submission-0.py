from typing import List
from collections import defaultdict


class AccountManager:
    def __init__(self):
        # name -> list of email sets
        self.name_to_groups = defaultdict(list)

    def add_account(self, account: List[str]):
        name = account[0]
        emails = set(account[1:])

        groups = self.name_to_groups[name]
        merged_groups = []
        current = emails

        for group in groups:
            # If any overlap, merge
            if current & group:
                current |= group
            else:
                merged_groups.append(group)

        merged_groups.append(current)
        self.name_to_groups[name] = merged_groups

    def get_accounts(self) -> List[List[str]]:
        result = []
        for name, groups in self.name_to_groups.items():
            for group in groups:
                result.append([name] + sorted(group))
        return result


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        manager = AccountManager()

        for account in accounts:
            manager.add_account(account)

        return manager.get_accounts()