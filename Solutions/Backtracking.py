import random
import networkx as nx
import matplotlib.pyplot as plt
import datetime as dt

all_colors = ["red", "green", "blue"]#, "yellow"]#, "pink", "purple"]


class Backtracking:
    def __init__(self):
        self.create_graph()
        self.create_color_mapping()

    """
    Create an undirected graph with a random number of nodes and edges
    """
    def create_graph(self):
        # number of nodes
        self.n = random.randint(5, 5)

        print(str(self.n) + " VERTICES")

        # number of edges
        self.e = random.randint(5, 8)

        print(str(self.e) + " EDGES")

        # create graph
        self.graph = nx.Graph()

        # add nodes
        for i in range(1, self.n + 1):
            self.graph.add_node(i)

        maxNr = (self.n * (self.n - 1)) / 2

        print(str(maxNr) + " MAX NUMBER OF EDGES")

        # add edges
        for i in range(self.e):
            start = random.randint(1, self.n)
            end = random.randint(1, self.n)
            while (start == end or self.graph.has_edge(start, end)) and self.graph.number_of_edges() < maxNr:
                if self.graph.number_of_edges(start) == self.n - 1:
                    start = random.randint(1, self.n)
                end = random.randint(1, self.n)

            self.graph.add_edge(start, end)

        print(str(self.graph.number_of_edges()) + " TOTAL EDGES")

    def create_color_mapping(self):
        # self.available_colors = []
        # for color in all_colors:
        #     if random.randint(0, 1) == 0:
        #         self.available_colors.append(color)
        #
        # if len(self.available_colors) <= 1:
        #     self.available_colors = all_colors

        # self.available_colors = all_colors

        self.available_colors = all_colors


    """
    Plot the graph
    """
    def plot_graph(self, colors):
        nx.draw(self.graph, node_color=colors, with_labels=True)
        plt.savefig("graph_" + str(self.n) + "_" + str(self.e) + ".png")
        plt.show()

    def get_colors(self, candidate):
        colors = []
        for c in candidate:
            colors.append(self.available_colors[c])
        return colors

    def is_valid(self, candidate):
        if len(candidate) > self.n:
            return False

        for neighbour in self.graph[len(candidate)]:
            if len(candidate) > neighbour and candidate[neighbour - 1] == candidate[-1]:
                return False
        # for x in candidate[:-1]:
        #     if x == candidate[-1]:
        #         return False
        return True

    def is_solution(self, candidate):
        return len(candidate) == self.n

    def back(self):
        candidate = [-1]
        start = dt.datetime.now()
        solutions = []

        while len(candidate) > 0:
            chosen = False
            while not chosen and candidate[-1] < len(self.available_colors) - 1:
                candidate[-1] += 1
                chosen = self.is_valid(candidate)
            if chosen:
                if self.is_solution(candidate):
                    # self.plot_graph(self.get_colors(candidate))
                    print((dt.datetime.now() - start).total_seconds())
                    solutions.append(self.get_colors(candidate))
                    if len(solutions) == 10:
                        return solutions
                candidate.append(-1)
            else:
                candidate = candidate[:-1]

        return solutions
