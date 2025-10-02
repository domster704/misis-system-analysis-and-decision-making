from pprint import pprint


def main(csv_graph: str) -> list[list[list[int]]]:
    """
    csv_graph: строка с CSV-графом:
        1,2
        1,3
        3,4
        3,5

    Возвращает список из 5 матриц n×n:
      [ out_matrix, in_matrix, successors_matrix, predecessors_matrix, brothers_matrix ]
    """
    lines = csv_graph.strip().splitlines()
    edges: list[tuple[int, int]] = []
    vertices: set[int] = set()

    for line in lines:
        v1, v2 = map(int, line.strip().split(","))
        edges.append((v1, v2))
        vertices.update([v1, v2])

    sorted_vertices = sorted(vertices)
    index_map = {v: i for i, v in enumerate(sorted_vertices)}
    n = len(sorted_vertices)

    arr: list[list[int]] = [[0] * n for _ in range(n)]
    for v1, v2 in edges:
        i, j = index_map[v1], index_map[v2]
        arr[i][j] = 1
        arr[j][i] = -1

    out_matrix = [[0] * n for _ in range(n)]
    in_matrix = [[0] * n for _ in range(n)]
    successors_matrix = [[0] * n for _ in range(n)]
    predecessors_matrix = [[0] * n for _ in range(n)]
    brothers_matrix = [[0] * n for _ in range(n)]

    def dfs_successors(root: int, v: int, visited: set[int]):
        for u in range(n):
            if arr[v][u] == 1 and u not in visited:
                successors_matrix[root][u] = 1
                visited.add(u)
                dfs_successors(root, u, visited)

    def dfs_predecessors(root: int, v: int, visited: set[int]):
        for u in range(n):
            if arr[v][u] == -1 and u not in visited:
                predecessors_matrix[root][u] = 1
                visited.add(u)
                dfs_predecessors(root, u, visited)

    def mark_brothers(root: int, v: int):
        for u in range(n):
            if arr[v][u] == 1 and u != root:
                brothers_matrix[root][u] = 1

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                out_matrix[i][j] = 1
                dfs_successors(i, j, {j})
            elif arr[i][j] == -1:
                in_matrix[i][j] = 1
                dfs_predecessors(i, j, {j})
                mark_brothers(i, j)

    return [out_matrix, in_matrix, successors_matrix, predecessors_matrix, brothers_matrix]


if __name__ == "__main__":
    csv: str = open('graph.csv', 'r', encoding='utf-8').read()
    result = main(csv)

    names = ["out", "in", "successors", "predecessors", "brothers"]
    for name, matrix in zip(names, result):
        print(f"\n{name} matrix:")
        pprint(matrix)
