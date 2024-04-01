from typing import List, Counter
import math

class Solution:

    def minStickersDP(self, stickers: List[str], target: str) -> int:
        # Convert stickers and target into character frequency maps
        sticker_maps = [Counter(sticker) for sticker in stickers]
        target_map = Counter(target)

        # Initialize dp array to store the minimum number of stickers required to spell each prefix of target
        n = len(target)
        dp = [float('inf')] * (1 << n)  # Initialize dp with infinity values
        dp[0] = 0  # Base case: no stickers needed for empty string

        # Iterate through each state of target word (represented as a bitmask)
        for state in range(1 << n):
            if dp[state] == float('inf'):  # Skip if current state is unreachable
                continue
            for sticker in sticker_maps:
                next_state = state
                for char, freq in sticker.items():
                    for i in range(n):
                        # If current character in sticker can be used to cover character at index i in target
                        if (state >> i) & 1 == 0 and target[i] == char:
                            next_state |= 1 << i  # Update next state
                            freq -= 1  # Decrement frequency of character in sticker
                            if freq == 0:
                                break
                # Update dp[next_state] with minimum number of stickers
                dp[next_state] = min(dp[next_state], dp[state] + 1)

        # Return the minimum number of stickers required to spell the entire target word
        return dp[(1 << n) - 1] if dp[(1 << n) - 1] != float('inf') else -1

    def minStickersBT(self, stickers: List[str], target: str) -> int:
        # Convert stickers and target into character frequency maps
        sticker_maps = [Counter(sticker) for sticker in stickers]
        target_map = Counter(target)

        # Memoization dictionary to store minimum stickers required for each prefix of target
        memo = {}

        # Helper function for backtracking
        def backtrack(freq_map):
            # Base case: If all characters in target are satisfied, return 0
            if all(freq == 0 for freq in freq_map.values()):
                return 0

            # If the current frequency map is memoized, return the result
            if tuple(freq_map.items()) in memo:
                return memo[tuple(freq_map.items())]

            # Prune the search space by considering only stickers with characters present in the target
            possible_stickers = [sticker for sticker in sticker_maps if any(freq_map[char] > 0 for char in sticker)]

            # Try using each possible sticker and recurse
            min_stickers = float('inf')
            for sticker in possible_stickers:
                next_freq_map = freq_map.copy()
                for char, freq in sticker.items():
                    next_freq_map[char] -= min(freq, next_freq_map[char])
                min_stickers = min(min_stickers, 1 + backtrack(next_freq_map))

            # Memoize the result and return
            memo[tuple(freq_map.items())] = min_stickers
            return min_stickers

        # Start backtracking from the initial target word frequency map
        min_stickers_needed = backtrack(target_map)

        # If the minimum number of stickers needed is infinity, target cannot be spelled
        return min_stickers_needed if min_stickers_needed != float('inf') else -1

    def minStickers(self, stickers: List[str], target: str) -> int:

        def count(word):
            result = {}
            for char in word:
                result[char] = result.get(char, 0) + 1
            return result
        
        def countSticker(sticker):
            result = {}
            for char in sticker:
                if char in targetCounts:
                    result[char] = result.get(char, 0) + 1
            return result
        
        def cover(cur, prev):
            if len(cur) < len(prev):
                return False
            for prevK, prevV in prev.items():
                if prevK not in cur or prevV > cur[prevK]:
                    return False
            return True

        def countStickers():
            result = []
            for sticker in stickers:
                count = countSticker(sticker)
                if count:
                    result.append(count)
            return result
            # if not result:
            #     return result
            # result.sort()
            # finalResult = [result[0]]
            # for i in range(1, len(result)):
            #     curCount = result[i]
            #     while finalResult and cover(curCount, finalResult[-1]):
            #         finalResult.pop()
            #     finalResult.append(curCount)
            # return finalResult
        
        def addCoverage(coverage, stickerCount):
            addCount = 0
            # Add 1 sticker if it improves coverage
            for char in stickerCount:
                if char not in coverage or coverage[char] < targetCounts[char]:
                    addCount = 1
                    break

            # Greedily adding multiple current sticker to meet target doesn't work
            #
            # for stickerK, stickerV in stickerCount.items():
            #     charAddCount = 0
            #     missingCount = targetCounts[stickerK] if stickerK not in coverage else (targetCounts[stickerK] - coverage[stickerK])
            #     if missingCount > 0:
            #         temp = missingCount % stickerV
            #         charAddCount = missingCount // stickerV if temp == 0 else (missingCount // stickerV + 1)
            #     addCount = max(addCount, charAddCount)
            if addCount > 0:
                for char in stickerCount:
                    coverage[char] = coverage.get(char, 0) + (addCount * stickerCount[char])
            return addCount

        def removeCoverage(coverage, stickerCount, addCount):
            if addCount > 0:
                for char in coverage:
                    if char in stickerCount:
                        coverage[char] -= (stickerCount[char] * addCount)
                        if coverage[char] < 0:
                            coverage[char] = 0

        def backtrack(startIndex, count, coverage):
            nonlocal result
            if cover(coverage, targetCounts):
                result = min(result, count)
                return
            for i in range(startIndex, len(stickerCounts)):
                if count < result:
                    addCount = addCoverage(coverage, stickerCounts[i])
                    count += addCount
                    backtrack(i + 1, count, coverage)
                    count -= addCount
                    removeCoverage(coverage, stickerCounts[i], addCount)

        if not stickers or not target:
            return 0
        targetCounts = count(target)
        stickerCounts = countStickers()
        result = math.inf
        backtrack(startIndex = 0, count = 0, coverage = {})
        return result if result < math.inf else -1


import unittest

class TestSolution(unittest.TestCase):
    def testMinStickers(self):
        s = Solution()
        self.assertEqual(s.minStickers(stickers = ["travel","quotient","nose","wrote","any"], target = "lastwest"), 4)
        self.assertEqual(s.minStickers(stickers = ["with","example","science"], target = "thehat"), 3)
        self.assertEqual(s.minStickers(stickers = ["notice","possible"], target = "basicbasic"), -1)



if __name__ == '__main__':
    unittest.main()