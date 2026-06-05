class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        temp = [0] * 26
        count = 0
        maxcnt = 0
        maxfreq = 0

        for right in range(len(s)):
            idx = ord(s[right]) - ord('A')
            temp[idx] += 1
            count += 1

            maxfreq = max(maxfreq, temp[idx])

            while count - maxfreq > k:
                temp[ord(s[left]) - ord('A')] -= 1
                left += 1
                count -= 1

            maxcnt = max(maxcnt, count)

        return maxcnt