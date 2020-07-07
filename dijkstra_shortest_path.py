class Node:

    def __init__(self, data, indexLoc = None):
        self.data = data
        self.index = indexLoc


class Graph:

    @classmethod
    def create_from_node(self, nodes):
        return Graph(len(nodes), len(nodes), nodes)


    def __init__(self, row, column, nodes = None):

        self.adj_mat = [[0] * column for _ in range(row)]
        self.nodes = nodes
        for i in range(len(self.nodes)):
            self.nodes[i].index = i


    def get_index_from_node(self, node):

        if not isinstance(node, Node) and not isinstance(node, int):
            raise ValueError('Error. Must be a node or an integer.')

        if isinstance(node, int):
            return node
        else:
            return node.index            
            
        
    def connect_node(self, node1, node2, weight = 1):
        node1, node2 = self.get_index_from_node(node1), self.get_index_from_node(node2)
        self.adj_mat[node1][node2] = weight
        
    
    def connect(self, node1, node2, weight = 1):
        self.connect_node(node1, node2, weight)
        self.connect_node(node2, node1, weight)
        

    def print_adj_matrix(self):
        for row in self.adj_mat:
            print(row)

    
    def get_adj_matrix(self):
        return self.adj_mat

    
    def connection_from(self, node):
        node = self.get_index_from_node(node)
        return [(self.nodes[col_num], self.adj_mat[node][col_num]) for col_num in range(len(self.adj_mat[node])) if self.adj_mat[node][col_num] != 0]
        

    def dijkstra_shortest_path(self, node):
        node_num = self.get_index_from_node(node)
        distance = [None] * len(self.nodes)
        for i in range(len(distance)):
            distance[i] = [float("inf")]
            distance[i].append([self.nodes[node_num]])

        distance[node_num][0] = 0

        queue = [i for i in range(len(self.nodes))]
        seen = set()
        
        while len(queue) > 0:
            min_distance = float("inf")
            min_node = None

            for n in queue:
                if distance[n][0] < min_distance and n not in seen:
                    min_distance = distance[n][0]
                    min_node = n
                    
            queue.remove(min_node)
            seen.add(min_node)

            connections = self.connection_from(min_node)

            for (node, weight) in connections:
                total_distance = weight + min_distance
                
                if total_distance < distance[node.index][0]:
                    distance[node.index][0] = total_distance
                    distance[node.index][1] = list(distance[min_node][1])
                    distance[node.index][1].append(node)
                    
        return distance
        
    