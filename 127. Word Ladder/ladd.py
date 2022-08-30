from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        myset=set(wordList)
        if endWord not in myset:
            return 0
        q=[(beginWord, 1)]
        if beginWord in myset:
            myset.remove(beginWord)
        while q:
            r=len(q)
            while r>0:
                cur, depth =q.pop(0)
                if cur == endWord:
                    return depth
                for i in range(len(cur)):
                    for elem in range(ord('a'), ord('z')+1):
                        copy=cur[:i] +chr(elem) + cur[i+1:]
                        if copy==cur:
                            continue
                        if copy==endWord:
                            return depth+1
                        if copy in myset:
                            q.append((copy, depth+1))
                            myset.remove(copy)
                r-=1
        return 0
