# task0
#
# Условие:
# Дан ориентированный ациклический граф G = (V, E), где:
#   V -- множество вершин графа,
#   E -- множество рёбер графа.
#
# Каждое ребро ei принадлежит E и описывается парой (vj, vk), где:
#   vj, vk принадлежит V -- вершины графа.
#
# Граф задаётся в виде CSV-файла. Каждая строка файла соответствует одному ребру:
#   начальная вершина, конечная вершина
#
# Пример входных данных (graph.csv):
# 1,2
# 1,3
# 3,4
# 3,5
#
# Задача:
# 1. Написать функцию
#       def main(csv_graph: str) -> list[list[int]]]:
#          ...
#    где csv_graph -- строка (содержимое CSV-файла).
#
# 2. Функция должна возвращать матрицу смежности графа в виде списка списков list[list].
#    - Размер матрицы: n x n, где n = |V| (количество вершин графа).
#    - Элемент matrix[i][j] равен 1, если существует ребро из вершины i в вершину j, и 0, если ребра нет.
#
# Ожидаемый результат:
#  [[0, 1, 1, 0, 0],
#   [1, 0, 0, 0, 0],
#   [1, 0, 0, 1, 1],
#   [0, 0, 1, 0, 0],
#   [0, 0, 1, 0, 0]]

from pprint import pprint


def main(csv_graph: str) -> list[list[int]]:
    lines = csv_graph.strip().splitlines()
    edges: list[tuple[int, int]] = []
    vertices: set[int] = set()

    for line in lines:
        v1, v2 = line.strip().split(',')
        edges.append((int(v1), int(v2)))

        vertices.add(int(v1))
        vertices.add(int(v2))

    sorted_vertices = sorted(vertices)
    index_map = {v: i for i, v in enumerate(sorted_vertices)}

    matrix: list[list[int]] = [[0] * len(sorted_vertices) for _ in range(len(sorted_vertices))]

    for v1, v2 in edges:
        i, j = index_map[v1], index_map[v2]
        matrix[i][j] = 1
        matrix[j][i] = 1

    return matrix


if __name__ == '__main__':
    csv: str = open('graph.csv', 'r', encoding='utf-8').read()
    matrix = main(csv)
    pprint(matrix)
