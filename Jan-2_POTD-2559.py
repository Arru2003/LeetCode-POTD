class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        
        # Helper function to check if a word starts and ends with a vowel
        def is_vowel_string(word):
            return word[0] in vowels and word[-1] in vowels
        
        # Precompute a prefix sum array for vowel string counts
        n = len(words)
        prefix = [0] * (n + 1)
        
        for i in range(n):
            prefix[i + 1] = prefix[i] + (1 if is_vowel_string(words[i]) else 0)
        
        # Process each query
        results = []
        for l, r in queries:
            results.append(prefix[r + 1] - prefix[l])
        
        return results
