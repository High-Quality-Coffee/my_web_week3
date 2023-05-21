from collections import deque
import time

#N이 증가하면서 이동횟수는 임의로 변경

# Define the BFS algorithm
def bfs(initial_state, goal_state, n):
  visited = set()
  queue = deque([(0, initial_state)])  # (moves, state)
  while queue:
    moves, state = queue.popleft()
    if state == goal_state:
      return moves
    if tuple(state) not in visited:
      visited.add(tuple(state))
      blank_index = state.index(0)
      for move in [-n, -1, 1, n]:
        new_index = blank_index + move
        if 0 <= new_index < n**2 and (new_index // n == blank_index // n
                                      or new_index % n == blank_index % n):
          new_state = state.copy()
          new_state[blank_index], new_state[new_index] = new_state[
            new_index], new_state[blank_index]
          queue.append((moves + 1, new_state))

  return -1


n = 3
# Define the goal state and the initial state
goal_state = list(range(1, n**2)) + [0]

initial_state = [1, 2, 3, 4,5, 6, 7,0,8]

start = time.time()
print(bfs(initial_state, goal_state, n))
end = time.time()
print(end - start)

#print("{:.10f}".format(end - start))

