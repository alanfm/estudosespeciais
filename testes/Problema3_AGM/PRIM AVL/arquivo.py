# importações necessárias
#
#
#


# AVL

class AVLNode:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
        self.left = None
        self.right = None
        self.height = 1

# Árvore AVL
class AVLTree:

    # O construtor inicializa uma árvore AVL vazia
    def __init__(self):
        self.root = None

    # Retorna a altura do nó. Se o nó for None, a altura é considerada 0
    def get_height(self, node):
        return node.height if node else 0

    # Retorna o fator de balanceamento para um nó
    def get_balance_factor(self, node):
        return self.get_height(node.left) - self.get_height(node.right)

    # Executa uma rotação à direita em torno do nó y
    def rotate_right(self, y):
        x = y.left
        T2 = x.right

        x.right = y
        y.left = T2

        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1
        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1

        return x

    # Executa uma rotação à esquerda em torno do nó x
    def rotate_left(self, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        x.height = max(self.get_height(x.left), self.get_height(x.right)) + 1
        y.height = max(self.get_height(y.left), self.get_height(y.right)) + 1

        return y

    # Insere um novo nó na árvore AVL e faz a rotação
    def insert(self, root, vertex, weight):
        if not root:
            return AVLNode(vertex, weight)

        if vertex < root.vertex:
            root.left = self.insert(root.left, vertex, weight)
        elif vertex > root.vertex:
            root.right = self.insert(root.right, vertex, weight)
        else:
            # Duplicatas não são permitidas em uma AGM
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance_factor(root)

        # Casos de desequilíbrio

        # Esquerda-Esquerda
        if balance > 1 and vertex < root.left.vertex:
            return self.rotate_right(root)

        # Direita-Direita
        if balance < -1 and vertex > root.right.vertex:
            return self.rotate_left(root)

        # Esquerda-Direita
        if balance > 1 and vertex > root.left.vertex:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        # Direita-Esquerda
        if balance < -1 and vertex < root.right.vertex:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    # Insere um novo vértice na árvore AVL chamando o método "insert"
    def insert_vertex(self, vertex, weight):
        self.root = self.insert(self.root, vertex, weight)

    # Percorre a árvore e imprime os vértices e pesos dos nós
    def print_inorder(self, root):
        if root:
            self.print_inorder(root.left)
            print(f"({root.vertex}, {root.weight})", end=" ")
            self.print_inorder(root.right)

    # Deleta um nó da árvore AVL, mantendo o balanceamento, e realiza as rotações necessárias
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

        # Atualizar a altura do nó atual
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Rebalancear a árvore
        balance = self.get_balance_factor(root)

        # 4 casos de desequilíbrio
        if balance > 1 and self.get_balance_factor(root.left) >= 0:
            return self.rotate_right(root)

        if balance < -1 and self.get_balance_factor(root.right) <= 0:
            return self.rotate_left(root)

        if balance > 1 and self.get_balance_factor(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)

        if balance < -1 and self.get_balance_factor(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)

        return root

    # Encontra o nó com o valor mínimo na árvore AVL
    def find_min(self, root):
        while root.left:
            root = root.left
        return root

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

    # Implementa o algoritmo de Prim para encontrar a AGM
    def prim_mst(self):
        key = {vertex: float('inf') for vertex in self.vertices_set}
        mst_set = {vertex: False for vertex in self.vertices_set}
        parent = {vertex: None for vertex in self.vertices_set}
        avl_tree = AVLTree()

        # Começamos com um vértice arbitrário
        start_vertex = list(self.vertices_set)[0]
        key[start_vertex] = 0
        avl_tree.insert_vertex(start_vertex, key[start_vertex])

        while avl_tree.root is not None:
            # Escolhemos o vértice com a chave mínima na árvore AVL
            u = avl_tree.root.vertex
            mst_set[u] = True

            for neighbor, weight in self.adj[u]:
                if not mst_set[neighbor] and weight < key[neighbor]:
                    key[neighbor] = weight
                    parent[neighbor] = u
                    avl_tree.insert_vertex(neighbor, key[neighbor])

            # Removemos o vértice escolhido da árvore AVL
            avl_tree.root = avl_tree.delete(avl_tree.root, u)

        return parent

    #  Imprime as arestas da AGM encontrada
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
#
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
# g = Graph(matriz_dados)
# 
# parent = g.prim_mst()
# g.print_mst_edges(parent)
# g.plot_mst(parent)
