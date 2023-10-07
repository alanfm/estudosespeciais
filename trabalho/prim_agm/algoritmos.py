import numpy as np

# ARVORE BINARIA
class BinaryTreeNode:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight
        self.left = None
        self.right = None
        
# Nó da árvore
class BinaryTree:
    # inicializa uma árvore vazia
    def __init__(self):
        self.root = None

    # inserir um nó
    def insert(self, root, vertex, weight):
        if not root:
            return BinaryTreeNode(vertex, weight)

        # verifica se existe um nó, caso não exista, insere na esquerda ou direita
        if vertex < root.vertex:
            root.left = self.insert(root.left, vertex, weight)
        elif vertex > root.vertex:
            root.right = self.insert(root.right, vertex, weight)
        else:
            # Duplicatas não são permitidas em uma AGM
            return root

        return root

    # Insere um novo vértice na árvore
    def insert_vertex(self, vertex, weight):
        self.root = self.insert(self.root, vertex, weight)
        
    # Percorre a árvore de na sequênciaÇ esquerda, raiz e depois na direita, então imprime os vértices e pesos dos nós.
    def print_inorder(self, root):
        if root:
            self.print_inorder(root.left)
            print(f"({root.vertex}, {root.weight})", end=" ")
            self.print_inorder(root.right)

    # Exclui um nó da árvore
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

    # Encontra o nó com o valor mínimo na árvore
    def find_min(self, root):
        while root.left:
            root = root.left
        return root

# Classe do Grafo

# construtor inicializa o grafo
class GraphBin:
    def __init__(self, edges):
        self.vertices_set = set()
        for edge in edges:
            self.vertices_set.add(edge[0])
            self.vertices_set.add(edge[1])

        self.V = len(self.vertices_set)
        self.adj = [[] for _ in range(self.V)]

        for edge in edges:
            src, dest, weight = edge
            src = round(src)
            dest = round(dest)
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

    #  Imprime as arestas da AGM encontrada
    def print_mst_edges(self, parent):
        for vertex, par in parent.items():
            if par is not None:
                print(f"Edge: ({par}, {vertex})")


#################################################################################

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
class GraphAVL:
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

#######################################################################

# HEAP FIBONACCI
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
class GraphHeapFibonacci:
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

