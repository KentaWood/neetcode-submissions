class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        word_to_counts = defaultdict(list)

        for word in strs:
            count = [0] * 26
            # build counts using a tupe 
            for let in word:
                count[ord(let) - ord('a')] += 1


            word_to_counts[tuple(count)].append(word)
        # print(word_to_counts)
        return list(word_to_counts.values())
        