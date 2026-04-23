class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        groups = {}

        for word in strs:
            count = [0] * 26

            for l in word:
                count[ord(l) - ord('a')] += 1

            key = tuple(count)

            if key in groups:
                groups[key].append(word)
            else:
                groups[key] = [word]

        return list(groups.values())