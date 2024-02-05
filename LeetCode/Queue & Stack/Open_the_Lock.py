from collections import deque
class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        deadends = set(deadends)

        # Check if the initial state "0000" is a deadend
        if "0000" in deadends:
            return -1

        # Initialize the BFS queue with the initial state and level
        queue = deque([("0000", 0)])

        # Set to keep track of visited states
        visited = set("0000")

        while queue:
            current_state, level = queue.popleft()

            # Check if we have reached the target
            if current_state == target:
                return level

            # Generate the next possible states by turning each wheel
            next_states = []
            for i in range(4):
                digit = int(current_state[i])
                for diff in [-1, 1]:
                    new_digit = (digit + diff) % 10
                    new_state = current_state[:i] + str(new_digit) + current_state[i + 1:]
                    if new_state not in visited and new_state not in deadends:
                        next_states.append(new_state)
                        visited.add(new_state)

            # Add the next states to the queue
            if next_states:
                queue.extend([(state, level + 1) for state in next_states])

        # If we exhaust all possibilities and cannot reach the target
        return -1


deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
res = Solution()
sol = res.openLock(deadends, target)
print(sol)
