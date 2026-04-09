from typing import List

class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        def dfs(i, a_sum, b_sum, a_streak, b_streak):
            if i == n:
                if a_sum > b_sum:
                    return "Alice"
                elif b_sum > a_sum:
                    return "Bob"
                return "Tie"

            results = []

            if a_streak == 0 and b_streak == 0:
                # Start of Alice's turn — she must take at least 1 stone
                results.append(dfs(i + 1, a_sum + stoneValue[i], b_sum, 1, 0))

            elif a_streak > 0:
                # Alice is mid-turn: take another stone OR stop and let Bob start
                if a_streak < 3:
                    results.append(dfs(i + 1, a_sum + stoneValue[i], b_sum, a_streak + 1, 0))
                # Alice stops — Bob must take this stone to begin his turn
                results.append(dfs(i + 1, a_sum, b_sum + stoneValue[i], 0, 1))

            else:  # b_streak > 0
                # Bob is mid-turn: take another stone OR stop and let Alice start
                if b_streak < 3:
                    results.append(dfs(i + 1, a_sum, b_sum + stoneValue[i], 0, b_streak + 1))
                # Bob stops — Alice must take this stone to begin her turn
                results.append(dfs(i + 1, a_sum + stoneValue[i], b_sum, 1, 0))

            # Aggregate: current player picks optimally for themselves
            alice_turn = a_streak > 0 or (a_streak == 0 and b_streak == 0)

            if alice_turn:
                if "Alice" in results: return "Alice"
                if "Tie" in results: return "Tie"
                return "Bob"
            else:
                if "Bob" in results: return "Bob"
                if "Tie" in results: return "Tie"
                return "Alice"

        return dfs(0, 0, 0, 0, 0)