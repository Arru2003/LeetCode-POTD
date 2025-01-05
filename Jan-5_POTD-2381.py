from typing import List

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift_effects = [0] * (n + 1)
        
        # Record the shift effects using a prefix sum approach
        for start, end, direction in shifts:
            if direction == 1:
                shift_effects[start] += 1
                shift_effects[end + 1] -= 1
            else:
                shift_effects[start] -= 1
                shift_effects[end + 1] += 1
        
        # Compute the net shifts for each character
        net_shifts = [0] * n
        current_shift = 0
        for i in range(n):
            current_shift += shift_effects[i]
            net_shifts[i] = current_shift
        
        # Apply the shifts to the string
        result = []
        for i, char in enumerate(s):
            # Calculate new character
            new_char = chr((ord(char) - ord('a') + net_shifts[i]) % 26 + ord('a'))
            result.append(new_char)
        
        return ''.join(result)
