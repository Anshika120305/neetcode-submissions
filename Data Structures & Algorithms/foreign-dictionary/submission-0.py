class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
       
        # Build adjacency list for all unique characters
        adj = {char: set() for word in words for char in word}

        # Find directed edges by comparing adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i + 1]
            min_len = min(len(w1), len(w2))

            # Invalid case: prefix word comes after longer word (e.g., "abc", "ab")
            if len(w1) > len(w2) and w1[:min_len] == w2[:min_len]:
                return ""

            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        # Topological Sort using DFS
        # visit status: False = visited in current path (cycle detection), True = fully processed & visited
        visit = {}  
        res = []

        def dfs(c):
            if c in visit:
                return visit[c]  # Returns True if cycle detected (False in visit map)

            visit[c] = True  # Mark character as currently visiting in path

            for neighbor in adj[c]:
                if dfs(neighbor):
                    return True

            visit[c] = False  # Mark character as fully processed
            res.append(c)
            return False

        for char in adj:
            if dfs(char):
                return ""  # Cycle detected

        res.reverse()
        return "".join(res)