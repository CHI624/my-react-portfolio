import heapq
def dijkstra(graph, start):
# Number of vertices
    n = len(graph)
# Distance table to store shortest path estimates
    distances = [float('inf')] * n
    distances[start] = 0
# Priority queue for the next vertex to explore
    priority_queue = [(0, start)] # (distance, vertex)
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
# Skip processing if we found a better path already
        if current_distance > distances[current_vertex]:
            continue
# Explore neighbors
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
# If a shorter path is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances
city_graph = {
0: [(1, 213.1), (2, 230.5)],
1: [(0, 213.1), (2, 164.0), (5, 887.3)],
2: [(0, 230.5), (1, 164.0), (3, 107.5)],
3: [(2, 107.5), (4, 403.3)],
4: [(3, 403.3), (5, 733.8)],
5: [(1, 887.3), (4, 733.8)],
6: []
}
city_names = ["London", "Paris", "Brussels", "Amsterdam", "Berlin", "Rome", "Madrid"]
# Run Dijkstra's algorithm
n=len(city_names)
distance_matrix =[[0.0 if i == j else float('inf') for j in range(n)] for i in range(n)] 
for start in range(n):
        distances = dijkstra(city_graph, start)
        distances = [dist if dist < float('inf') else 0.0 for dist in distances]
        distance_matrix[start] = distances

print("Shortest distances between cities:")
header = " " *12
for city in city_names:
    header += f"{city:>12}"
print(header)

for i in range(n):
    row = f"{city_names[i]:<12}"
    for j in range(n):
        row += f"{distance_matrix[i][j]:>12.1f}"
    print(row)
