# Есть граф ориентированный, взвешенный и ациклический.
# G = (V, E) - граф: упорядоченное множество пар, элементы которого - вершины графа и ребра
# V = {v1, v2, v3, vi, vn} - неупорядоченное множество вершин
# E = {e1, e2, e3, ei, en} - неупорядоченное множество ребер
# ei = (vj, vk, mi) принадлежит E - ребро
# vj, vk принадлежит V - вершины
# mi принадлежит R - вес ребра
#
# Задача: считать CSV файл, описывающий граф, и нарисовать граф в виде матрицы смежности.
# Написать функцию, которая на вход получает строку (именно как строчка, то есть считываем CSV, а потом преобразовываем это в строку) и возвращает list[list]
# Это task0. Это функция потом пойдёт в task1
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
