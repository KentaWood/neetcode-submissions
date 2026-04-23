class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        counts = {}

        for word in strs:

            freq = [0] * 26

            for let in word:
                freq[ord(let) - ord('a')] += 1 
            
            count = tuple(freq)

            if count in counts:
                counts[count].append(word)
            else:
                counts[count] = [word]
        
        return counts.values()