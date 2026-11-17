class Solution:

    def encode(self, strs: List[str]) -> str:
        
        

        return "\x1f".join(strs)



    def decode(self, s: str) -> List[str]:
        
        return s.split("\x1f")
