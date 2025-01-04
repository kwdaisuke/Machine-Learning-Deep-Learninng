class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        mapping = {}
        counter = {}
        for word in strs:
            for num, letter in enumerate(word):
                if word == strs[0]:
                    mapping[num] = letter
                else:
                    if mapping[num] == letter:
                        counter[letter] += 1
                        continue
                    else:
                        break

        return counter

### Best Solution
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        v = sorted(v)
        first = v[0]
        last = v[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return ans
            ans += first[i]
        return ans



