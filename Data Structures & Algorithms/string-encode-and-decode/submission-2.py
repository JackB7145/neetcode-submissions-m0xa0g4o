class Solution:

    def encode(self, strs: List[str]) -> str:
        return './.'.join(strs) if strs else "MotherFucker"
    def decode(self, s: str) -> List[str]:
        return [] if s == "MotherFucker" else s.split('./.')

        return res
