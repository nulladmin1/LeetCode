class Solution:
    def merge_alternately(self, word1: str, word2: str) -> str:
        merged_string = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                merged_string.append(word1[i])
            if i < len(word2):
                merged_string.append(word2[i])
            i += 1

        return "".join(merged_string)
def main():
    solution = Solution()
    word1 = "abc"
    word2 = "pqrs"
    print("Word 1: ", word1)
    print("Word 2: ", word2)
    print(solution.merge_alternately(word1, word2))
