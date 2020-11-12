import networkx as nx
import matplotlib.pyplot as plt


class CSPSolution:
    def __init__(self, countries, timestamp, all_colors):
        self.__countries = countries
        self.__timestamp = timestamp
        self.__all_colors = all_colors

    def get_countries(self):
        return self.__countries

    def get_timestamp(self):
        return self.__timestamp

    def plot_countries(self):
        graph = nx.Graph()
        colors = []
        for c in self.__countries:
            graph.add_node(c.get_name())

        for c in self.__countries:
            for n in c.get_neighbours():
                if not graph.has_edge(c.get_name(), n.get_name()):
                    graph.add_edge(c.get_name(), n.get_name())
            if c.get_color_index() is None:
                colors.append("white")
            else:
                colors.append(self.__all_colors[c.get_color()])

        nx.draw(graph, node_color=colors, with_labels=True)
        plt.show()