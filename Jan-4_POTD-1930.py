class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
    # Record the first and last occurrence of each character
        first_occurrence = {}
        last_occurrence = {}
    
        for i, char in enumerate(s):
            if char not in first_occurrence:
                first_occurrence[char] = i
            last_occurrence[char] = i

        unique_palindromes = set()

        # Check for each character's contribution to palindromes
        for char in first_occurrence:
            if first_occurrence[char] < last_occurrence[char]:
                start = first_occurrence[char]
                end = last_occurrence[char]
                # Find unique middle characters
                middle_chars = set(s[start + 1:end])
                for middle in middle_chars:
                    unique_palindromes.add((char, middle, char))

        # The result is the count of unique palindromes
        return len(unique_palindromes)