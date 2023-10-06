

# Binária funcionando

class BinaryTreeNode:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, root, vertex, weight):
        if not root:
            return BinaryTreeNode(vertex, weight)

        if vertex < root.vertex:
            root.left = self.insert(root.left, vertex, weight)
        elif vertex > root.vertex:
            root.right = self.insert(root.right, vertex, weight)
        else:
            # Duplicatas não são permitidas em uma AGM
            return root

        return root

    def insert_vertex(self, vertex, weight):
        self.root = self.insert(self.root, vertex, weight)

    def print_inorder(self, root):
        if root:
            self.print_inorder(root.left)
            print(f"({root.vertex}, {root.weight})", end=" ")
            self.print_inorder(root.right)

    def delete(self, root, vertex):
        if not root:
            return root

        if vertex < root.vertex:
            root.left = self.delete(root.left, vertex)
        elif vertex > root.vertex:
            root.right = self.delete(root.right, vertex)
        else:
            # Vértice encontrado, realizar a exclusão
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            # Caso com dois filhos: encontrar o sucessor in-order (menor nó na subárvore direita)
            successor = self.find_min(root.right)
            root.vertex, root.weight = successor.vertex, successor.weight
            root.right = self.delete(root.right, successor.vertex)

        return root

    def find_min(self, root):
        while root.left:
            root = root.left
        return root

class Graph:
    def __init__(self, edges):
        self.vertices_set = set()
        for edge in edges:
            self.vertices_set.add(edge[0])
            self.vertices_set.add(edge[1])

        self.V = len(self.vertices_set)
        self.adj = [[] for _ in range(self.V)]

        for edge in edges:
            src, dest, weight = edge
            self.add_edge(src, dest, weight)

    def add_edge(self, src, dest, weight):
        if 0 <= src < self.V and 0 <= dest < self.V:
            self.adj[src].append((dest, weight))
            self.adj[dest].append((src, weight))  # Gráfico não direcionado
        else:
            print(f"Erro: Vértices {src} ou {dest} fora do intervalo esperado.")

    def prim_mst(self):
        key = {vertex: float('inf') for vertex in self.vertices_set}
        mst_set = {vertex: False for vertex in self.vertices_set}
        parent = {vertex: None for vertex in self.vertices_set}
        min_heap = []

        # Começamos com um vértice arbitrário
        start_vertex = list(self.vertices_set)[0]
        key[start_vertex] = 0
        heapq.heappush(min_heap, (0, start_vertex))

        while min_heap:
            # Escolhemos o vértice com a chave mínima na fila de prioridade
            current_key, u = heapq.heappop(min_heap)
            if mst_set[u]:
                continue

            mst_set[u] = True

            for neighbor, weight in self.adj[u]:
                if not mst_set[neighbor] and weight < key[neighbor]:
                    key[neighbor] = weight
                    parent[neighbor] = u
                    heapq.heappush(min_heap, (key[neighbor], neighbor))

        return parent

    def print_mst_edges(self, parent):
        for vertex, par in parent.items():
            if par is not None:
                print(f"Edge: ({par}, {vertex})")

    def plot_mst(self, parent):
        G = nx.Graph()

        for vertex, par in parent.items():
            if par is not None and 0 <= par < self.V and 0 <= vertex < self.V:
                if par < len(self.adj) and vertex < len(self.adj[par]):
                    # Adicionando a aresta apenas se os índices estiverem dentro dos limites
                    if self.adj[par][vertex][0] != float('inf'):
                        G.add_edge(par, vertex, weight=self.adj[par][vertex][0])

        pos = nx.spring_layout(G)

        edge_labels = {(u, v): d['weight'] for u, v, d in G.edges(data=True)}

        nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

        plt.show()

edges = [
    [0, 1, 6],
    [0, 2, 7],
    [1, 2, 3],
    [1, 4, 1],
    [2, 3, 1],
    [1, 3, 1],
    [3, 4, 55],
    [3, 5, 10],
    [5, 4, 20],
    [5, 6, 3],
    [2, 6, 4],
    [6, 7, 4],
    [7, 8, 1],
    [7, 9, 10],
    [9, 8, 1],
]

g = Graph(edges)

parent = g.prim_mst()
print("Edges of MST:")
g.print_mst_edges(parent)
g.plot_mst(parent)