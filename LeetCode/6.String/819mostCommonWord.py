class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub('[^\w]', ' ', paragraph).lower().split() if word not in banned]
        words_cnter = collections.Counter(words);
        return words_cnter.most_common(1)[0][0]