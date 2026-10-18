class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        nei = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                key = word[:i] + '*' + word[i + 1:]
                nei[key].append(word)

        q = collections.deque([beginWord])
        count = 1
        visited = {beginWord}

        while q:
            for _ in range(len(q)):
                curWord = q.popleft()

                if curWord == endWord:
                    return count

                for i in range(len(curWord)):
                    key = curWord[:i] + '*' + curWord[i + 1:]
                    for neighbor in nei[key]:
                        if neighbor in visited:
                            continue
                        q.append(neighbor)
                        visited.add(neighbor)

            count += 1

        return 0
