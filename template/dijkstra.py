def dijkstra(graph, source):
  """Finds the shortest path from the source node to all other nodes in the graph.

  Args:
    graph: A dictionary of adjacency lists, where each key is a node and each value is a list of neighboring nodes.
    source: The source node.

  Returns:
    A dictionary of distances from the source node to all other nodes in the graph.
  """

  distances = {}
  for node in graph:
    distances[node] = float('inf')
  distances[source] = 0

  visited = set()
  unvisited = set(graph.keys())

  while unvisited:
    current_node = min(unvisited, key=distances.__getitem__)
    unvisited.remove(current_node)
    visited.add(current_node)

    for neighbor in graph[current_node]:
      new_distance = distances[current_node] + graph[current_node][neighbor]
      if new_distance < distances[neighbor]:
        distances[neighbor] = new_distance

  return distances


# Example usage:

graph = {
  'A': {'B': 5, 'C': 3},
  'B': {'C': 2, 'D': 4},
  'C': {'D': 1},
  'D': {}
}

distances = dijkstra(graph, 'A')

print(distances)