graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C'],
    'C': ['A', 'B']
}

colors = ['Red', 'Green', 'Blue']
assigned = {}

for region in graph:
    for color in colors:
        safe = True

        for neighbour in graph[region]:
            if assigned.get(neighbour) == color:
                safe = False
                break

        if safe:
            assigned[region] = color
            break

print(assigned)