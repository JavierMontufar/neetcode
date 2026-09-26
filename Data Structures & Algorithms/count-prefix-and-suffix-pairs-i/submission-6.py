class Solution:
    def isPrefixAndSuffix(self, prefix_suffix: str, word: str) -> bool:
        # return word.startswith(prefix_suffix) and word.endswith(prefix_suffix)
        long = len(prefix_suffix)
        fist_nitems = word[:long]
        last_nitems = word[len(word)-long:]
        return (prefix_suffix == fist_nitems) and (prefix_suffix == last_nitems)

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for index, word in enumerate(words):
            compare_words = words[(index+1):]
            for compare_word in compare_words:
                if self.isPrefixAndSuffix(word, compare_word):
                    count += 1
        return count