class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        # Build adjacency list using wildcards (e.g., "c*t" -> ["cat"])
        wordList.append(beginWord)
        neighbors = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                neighbors[pattern].append(word)
        
        # BFS traversal
        visit = set([beginWord])
        q = deque([beginWord])
        res = 1
        
        while q:
            for _ in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return res
                
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neighbor in neighbors[pattern]:
                        if neighbor not in visit:
                            visit.add(neighbor)
                            q.append(neighbor)
                            
            res += 1
            
        return 0