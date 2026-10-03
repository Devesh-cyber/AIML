graph = {
    'A' : ['B','C'],
    'B' : [],
    'C' : ['G'],
    'G' : []
}

h = {
    'A': 6,
    'B': 5,
    'C': 3,
    'G': 0
}

current = 'A'
goal = 'G'

while current != goal:
    print(current, end=' ')
    neighbour = graph[current]

    if not neighbour:
        print('\nGoal Not Found')
        break

    values = [h[n] for n in neighbour]

    min_value = min(values)

    next_node = neighbour[values.index(min_value)]

    current = next_node

print(goal)

