class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        count_to_word = defaultdict(list)
        # n 
        for word in strs:
            
            # let count
            count = [0] * 26
            
            # len(word)
            for let in word:
            
                count[ord(let) - ord('a')] += 1

            count_to_word[tuple(count)].append(word)
        
        return list(count_to_word.values())




        