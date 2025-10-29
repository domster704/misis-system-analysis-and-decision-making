from math import log2, log, e


def main(s: str, root_id: str) -> tuple[float, float]:
    edges = [line.strip().split(",") for line in s.strip().splitlines()]
    edges = [(int(a), int(b)) for a, b in edges]

    # Определяем множество узлов
    nodes = sorted(set([x for a, b in edges for x in (a, b)]))
    n = len(nodes)
    root = int(root_id)

    # Формируем матрицу смежности
    adj = {i: set() for i in nodes}
    for a, b in edges:
        adj[a].add(b)

    # Типы отношений
    r1 = set(edges)
    r2 = set((b, a) for a, b in edges)
    r3 = set()
    for a in nodes:
        for mid in adj[a]:
            for b in adj.get(mid, []):
                if b != a:
                    r3.add((a, b))
    r3 -= r1
    r4 = set((b, a) for a, b in r3)

    # Сотрудничество
    from collections import deque
    level = {root: 0}
    q = deque([root])
    while q:
        v = q.popleft()
        for u in adj.get(v, []):
            level[u] = level[v] + 1
            q.append(u)
    r5 = set()
    for a in nodes:
        for b in nodes:
            if a != b and level.get(a) == level.get(b):
                r5.add((a, b))

    relations = [r1, r2, r3, r4, r5]

    # Считаем lij
    L = {m: [] for m in nodes}
    for m in nodes:
        for r in relations:
            L[m].append(sum(1 for (a, b) in r if a == m))

    # Энтропия
    H_total = 0.0
    for m in nodes:
        for lij in L[m]:
            if lij > 0:
                P = lij / (n - 1)
                H_total += -P * log2(P)

    H_total = round(H_total, 1)

    # Нормализация
    c = 1 / (e * log(2))
    k = 5
    H_ref = c * n * k
    h_norm = round(H_total / H_ref, 2)

    return H_total, h_norm


if __name__ == "__main__":
    csv: str = open('graph.csv', 'r', encoding='utf-8').read()
    print(main(csv, "1"))
