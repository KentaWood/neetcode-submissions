class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        word_to_counts = defaultdict(list)

        for word in strs:
            word_to_counts[tuple(sorted(word))].append(word)
        # print(word_to_counts)
        return list(word_to_counts.values())
        