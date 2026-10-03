from collections import deque

start = (3,3,0)
goal = (0,0,1)

queue = deque([start])
visited = set()

moves = [
    (1,0),(2,0),(0,1),(0,2),(1,1)
]

def safe(m,c):
    return (m==0 or m>=c) and (3-m ==0 or 3-m >= 3-c)

while queue:
    state = queue.popleft()
    if state not in visited:
        visited.add(state)
        print(state)

        if goal == state:
            print('\nGoal Found')
            break

        m, c, boat = state

        for dm, dc in moves:
            if boat == 0:
                new = (m-dm, c-dc,1)
            else:
                new = (m+dm, c+dc,0)

            if 0 <= new[0] <= 3 and 0 <= new[1] <= 3:
                if safe(new[0],new[1]) and new not in visited:
                    queue.append(new)
                    
        