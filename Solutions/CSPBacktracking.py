from Domain.Country import Country
# from Color import Color
from Utils.CSPSolution import CSPSolution
import datetime as dt
import copy
import networkx as nx
import matplotlib.pyplot as plt

"""
Variables = Countries
Variable Domains = Colors
Constraints = No two neighbours should have the same color
"""
class CSPBacktracking:
    def __init__(self, graph_file):
        self.__all_colors = {1: "red", 2: "blue", 3: "yellow", 4: "green", 5: "pink"}
        self.__countries = []
        self.__n = 0
        self.__domain = []
        self.create_domain()
        self.create_countries(graph_file)

    def create_countries(self, graph_file):
        f = open(graph_file, "r")
        lines = f.readlines()
        self.__n = int(lines[0].strip())
        countries = {}
        for c in range(0, self.__n):
            countries[c] = Country(str(c))

        for i in range(1, len(lines)):
            split_line = lines[i].split(",")
            x = int(split_line[0].strip())
            y = int(split_line[1].strip())
            countries[x].add_neighbour(countries[y])
            countries[y].add_neighbour(countries[x])

        for c in countries:
            countries[c].set_domain(self.__domain)
            self.__countries.append(countries[c])
        # self.__n = 4
        #
        # w = Country("w")
        # x = Country("x")
        # y = Country("y")
        # z = Country("z")
        #
        # w.add_neighbour(x)
        # w.add_neighbour(y)
        #
        # x.add_neighbour(w)
        # x.add_neighbour(y)
        # x.add_neighbour(z)
        #
        # y.add_neighbour(w)
        # y.add_neighbour(x)
        # y.add_neighbour(z)
        #
        # z.add_neighbour(y)
        # z.add_neighbour(x)
        #
        # for c in [w, x, y, z]:
        #     c.set_domain(self.__domain)
        #     self.__countries.append(c)

    def create_domain(self):
        for c in self.__all_colors:
            self.__domain.append(c)
        self.__domain.sort()

    def choose_value(self, currentPos):
        return self.__countries[currentPos].increase_index()

    def is_valid(self, currentPos):
        # if currentPos >= len(self.__countries):
        #     return False

        for neighbour in self.__countries[currentPos].get_neighbours():
            if neighbour.get_color_index() is not None and \
                    neighbour.get_color() == self.__countries[currentPos].get_color():
                return False
        # for x in candidate[:-1]:
        #     if x == candidate[-1]:
        #         return False
        return True

    def is_solution(self, currentPos):
        return currentPos == len(self.__countries) - 1

    def pretty_print(self):
        result = ""
        for c in self.__countries:
            if c.is_assigned():
                result = result + self.__all_colors[c.get_color()][0] + " "
            else:
                result = result + "-1 "
        return result

    def back(self, maxSolutions):
        currentPos = 0
        start = dt.datetime.now()
        solutions = []
        graph = nx.Graph()
        nodes = ["0"]
        prev_node = 0
        graph.add_node("0")

        while currentPos > -1:
            chosen = False
            while not chosen and currentPos < len(self.__countries) and \
                    self.__countries[currentPos].has_next_value():
                chosen = self.choose_value(currentPos) and self.is_valid(currentPos)
            if chosen:
                current_node = self.pretty_print()
                if not graph.has_node(current_node):
                    graph.add_node(current_node)
                graph.add_edge(nodes[prev_node], current_node)
                nodes.append(current_node)
                prev_node += 1
                if self.is_solution(currentPos):
                    solutions.append(CSPSolution(copy.deepcopy(self.__countries),
                                                 (dt.datetime.now() - start).total_seconds(),
                                                 copy.deepcopy(self.__all_colors)))
                    if len(solutions) == maxSolutions:
                        return solutions, graph
                currentPos += 1
            else:
                if currentPos < len(self.__countries):
                    self.__countries[currentPos].set_color_index(None)
                currentPos -= 1
                if prev_node != 0:
                    prev_node -= 1

        return solutions, graph
