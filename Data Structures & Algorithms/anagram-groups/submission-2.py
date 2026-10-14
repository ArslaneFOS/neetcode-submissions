class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams = defaultdict(list)

        for s in strs:
            key = 26 * [0]
            for c in s:
                key[ord(c) - ord('a')] += 1
            anagrams[tuple(key)].append(s)

        return list(anagrams.values())