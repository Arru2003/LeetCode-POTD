class Solution:
    def minOperations(self, boxes: str) -> list[int]:
        n = len(boxes)
        answer = [0] * n

        # First pass: calculate moves from left to right
        moves = 0
        count = 0  # Count of balls encountered so far
        for i in range(n):
            answer[i] += moves
            if boxes[i] == '1':
                count += 1
            moves += count

        # Second pass: calculate moves from right to left
        moves = 0
        count = 0  # Reset count of balls
        for i in range(n - 1, -1, -1):
            answer[i] += moves
            if boxes[i] == '1':
                count += 1
            moves += count

        return answer