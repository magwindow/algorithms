# the graph table
graph = {
    "start": {"a": 6, "b": 2},
    "a": {"fin": 1},
    "b": {"a": 3, "fin": 5},
    "fin": {}
}

# the costs table
infinity = float("inf")
costs = {
    "a": 6,
    "b": 2,
    "fin": infinity
}

# the parents table
parents = {
    "a": "start",
    "b": "start",
    "fin": None
}

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = float("inf")
    lowest_cost_node = None
    # Перебрать все узлы.
    for node in costs:
        cost = costs[node]
        # Если этот узел с наименьшей стоимостью из уже
        # виденных и он еще не был обработан...
        if cost < lowest_cost and node not in processed:
            # ... он назначается новым узлом с наименьшей стоимостью.
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node


# Найти узел с наименьшей стоимостью среди необрабатанных.
node = find_lowest_cost_node(costs)
# Если обработаны все узлы, цикл while останавливается.
while node is not None:
    cost = costs[node]
    neighbors = graph[node]
    # Перебрать всех соседей текущего узла.
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        # Если к соседу можно быстрее добраться через текущий  узел...
        if costs[n] > new_cost:
            # ... обновить стоимость для этого узла.
            costs[n] = new_cost
            # Этот узел становится новым родителем для соседа.
            parents[n] = node
    # Узел помечается как обработанный.
    processed.append(node)
    # Найти следующий узел для обработки и повторить цикл.
    node = find_lowest_cost_node(costs)

print("Стоимость от начала до каждого узла:")
print(costs)