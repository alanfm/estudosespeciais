# import networkx as nx
# import matplotlib.pyplot as plt
# import heapq

class FibonacciNode:
    def __init__(self, vertex, key):
        self.vertex = vertex
        self.key = key
        self.degree = 0
        self.child = None
        self.marked = False
        self.parent = None
        self.next = self
        self.prev = self

# construtor inicializa uma heap vazia
class FibonacciHeap:
    def __init__(self):
        self.min_node = None
        self.vertex_to_node = {}

    # Insere um novo nó na heap com o vértice e chave fornecidos
    def insert(self, vertex, key):
        if vertex not in self.vertex_to_node:
            new_node = FibonacciNode(vertex, key)
            self.vertex_to_node[vertex] = new_node

            if self.min_node is None:
                self.min_node = new_node
            else:
                self._link(self.min_node, new_node)
                if key < self.min_node.key:
                    self.min_node = new_node
        else:
            print(f"Aviso: Vértice {vertex} já está na heap de Fibonacci.")

    #  Atualiza a chave de um nó na heap para um novo valor, mantendo as propriedades da heap
    def decrease_key(self, vertex, new_key):
        if vertex in self.vertex_to_node:
            node = self.vertex_to_node[vertex]
            if new_key < node.key:
                node.key = new_key
                parent = node.parent

                if parent is not None and node.key < parent.key:
                    self._cut(node, parent)
                    self._cascade_cut(parent)

                if node.key < self.min_node.key:
                    self.min_node = node
        else:
            print(f"Erro: Vértice {vertex} não encontrado na heap de Fibonacci.")

    # Conecta dois nós na heap durante as operações de união e inserção
    def _link(self, root1, root2):
        root1.next.prev = root2
        root2.next.prev = root1
        root1.next, root2.next = root2.next, root1.next
        root1.child = root2
        root2.parent = root1
        root1.degree += 1
        root2.marked = False

    # Remove um nó da lista de filhos de seu pai
    def _cut(self, child, parent):
        if child.next == child:
            parent.child = None
        else:
            child.prev.next = child.next
            child.next.prev = child.prev
            if parent.child == child:
                parent.child = child.next

        parent.degree -= 1
        self._add_to_root_list(child)

        child.parent = None
        child.marked = False

    # Executa operações de corte cascata para manter as propriedades da heap
    def _cascade_cut(self, node):
        parent = node.parent
        if parent is not None:
            if not node.marked:
                node.marked = True
            else:
                self._cut(node, parent)
                self._cascade_cut(parent)

    # Adiciona um nó à lista de raízes na heap
    def _add_to_root_list(self, node):
        node.prev = self.min_node.prev
        node.next = self.min_node
        self.min_node.prev.next = node
        self.min_node.prev = node
        node.parent = None

    # Extrai o nó com a menor chave da heap
    def extract_min(self):
        min_node = self.min_node
        if min_node is not None:
            if min_node.child is not None:
                child = min_node.child
                while True:
                    next_child = child.next
                    child.prev = min_node.prev
                    child.next = min_node.next
                    min_node.prev.next = child
                    min_node.next.prev = child
                    child.parent = None
                    if next_child == min_node.child:
                        break
                    child = next_child

            min_node.prev.next = min_node.next
            min_node.next.prev = min_node.prev

            if min_node == min_node.next:
                self.min_node = None
            else:
                self.min_node = min_node.next
                self._consolidate()

            del self.vertex_to_node[min_node.vertex]

        return min_node

    # Realiza a operação de consolidar para manter as propriedades da heap
    def _consolidate(self):
        max_degree = int(1.5 * (1 + len(self.vertex_to_node))**0.5)
        degree_table = [None] * max_degree

        current = self.min_node
        nodes = [current]

        while current.next != self.min_node:
            current = current.next
            nodes.append(current)

        for node in nodes:
            degree = node.degree
            while degree_table[degree] is not None:
                other = degree_table[degree]
                if node.key > other.key:
                    node, other = other, node
                self._link(node, other)
                degree_table[degree] = None
                degree += 1

            degree_table[degree] = node

        self.min_node = None
        for degree_node in degree_table:
            if degree_node is not None:
                if self.min_node is None:
                    self.min_node = degree_node
                elif degree_node.key < self.min_node.key:
                    self.min_node = degree_node

# construtor inicializa o grafo
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

    # Adiciona uma aresta ao grafo
    def add_edge(self, src, dest, weight):
        if 0 <= src < self.V and 0 <= dest < self.V:
            self.adj[src].append((dest, weight))
            self.adj[dest].append((src, weight))  # Gráfico não direcionado
        else:
            print(f"Erro: Vértices {src} ou {dest} fora do intervalo esperado.")

    # Implementa o algoritmo de Prim usando a Heap de Fibonacci para encontrar a Árvore Geradora Mínima no grafo
    def prim_mst_fibonacci_heap(self):
        key = {vertex: float('inf') for vertex in self.vertices_set}
        mst_set = {vertex: False for vertex in self.vertices_set}
        parent = {vertex: None for vertex in self.vertices_set}
        fib_heap = FibonacciHeap()

        # Começamos com um vértice arbitrário
        start_vertex = list(self.vertices_set)[0]
        key[start_vertex] = 0
        fib_heap.insert(start_vertex, key[start_vertex])

        while fib_heap.min_node is not None:
            # Escolhemos o vértice com a chave mínima na heap de Fibonacci
            min_node = fib_heap.extract_min()
            u = min_node.vertex
            mst_set[u] = True

            for neighbor, weight in self.adj[u]:
                if not mst_set[neighbor] and weight < key[neighbor]:
                    key[neighbor] = weight
                    parent[neighbor] = u
                    fib_heap.insert(neighbor, key[neighbor])

        return parent

    # Imprime as arestas da AGM encontrada
    def print_mst_edges(self, parent):
        for vertex, par in parent.items():
            if par is not None:
                print(f"Edge: ({par}, {vertex})")

    # Gera uma representação gráfica da AGM (ainda com um erro, mas nada que interfira no entendimento ou execução)
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

# Exemplo ###################################################
# 
# Usando a função de leitura de arquivo
# nome_arquivo = 'alue2105.stp'
# matriz_dados = ler_dados_arquivo(nome_arquivo)
# matriz_dados = np.round(matriz_dados).astype(int)
# 
# Se não for utilizar a função de leitura de arquivo, pode gerar manualmente a matriz [[vertice, vertice, peso], ...]
# matriz_dados = [
#     [0, 1, 6],
#     [0, 2, 7],
#     [1, 2, 3],
#     [1, 4, 1],
#     [2, 3, 1],
#     [1, 3, 1],
#     [3, 4, 55],
#     [3, 5, 10],
#     [5, 4, 20],
#     [5, 6, 3],
#     [2, 6, 4],
#     [6, 7, 4],
#     [7, 8, 1],
#     [7, 9, 10],
#     [9, 8, 1],
# ]
# 
# 
# g = Graph(matriz_dados)
# 
# Utilizando a Heap de Fibonacci
# parent_fib = g.prim_mst_fibonacci_heap()
# g.print_mst_edges(parent_fib)
# g.plot_mst(parent_fib)
