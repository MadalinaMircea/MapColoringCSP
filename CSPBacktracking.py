from Country import Country
from Color import Color
from CSPSolution import CSPSolution
import datetime as dt
import copy

"""
Variables = Countries
Variable Domains = Colors
Constraints = No two neighbours should have the same color
"""
class CSPBacktracking:
    def __init__(self):
        self.__countries = []
        self.__n = 0
        self.__domain = []
        self.create_domain()
        self.create_countries()

    def create_countries(self):
        self.__n = 4

        w = Country("w")
        x = Country("x")
        y = Country("y")
        z = Country("z")

        w.add_neighbour(x)
        w.add_neighbour(y)

        x.add_neighbour(w)
        x.add_neighbour(y)
        x.add_neighbour(z)

        y.add_neighbour(w)
        y.add_neighbour(x)
        y.add_neighbour(z)

        z.add_neighbour(y)
        z.add_neighbour(x)

        for c in [w, x, y,z]:
            c.set_domain(self.__domain)
            self.__countries.append(c)

    def create_domain(self):
        for c in ["red", "green", "blue"]:
            self.__domain.append(Color(c))

    def is_valid(self, currentPos):
        if currentPos >= len(self.__countries):
            return False

        for neighbour in self.__countries[currentPos].get_neighbours():
            if neighbour.get_color_index() != -1 and \
                    neighbour.get_color().get_color_name() == self.__countries[currentPos].get_color().get_color_name():
                return False
        # for x in candidate[:-1]:
        #     if x == candidate[-1]:
        #         return False
        return True

    def is_solution(self, currentPos):
        return currentPos == len(self.__countries) - 1

    def back(self, maxSolutions):
        currentPos = 0
        start = dt.datetime.now()
        solutions = []

        while currentPos > -1:
            chosen = False
            while not chosen and currentPos < len(self.__countries) and \
                    self.__countries[currentPos].get_color_index() < \
                    len(self.__countries[currentPos].get_domain()) - 1:
                self.__countries[currentPos].set_color_index(self.__countries[currentPos].get_color_index() + 1)
                chosen = self.is_valid(currentPos)
            if chosen:
                if self.is_solution(currentPos):
                    solutions.append(CSPSolution(copy.deepcopy(self.__countries),
                                                 (dt.datetime.now() - start).total_seconds()))
                    if len(solutions) == maxSolutions:
                        return solutions
                currentPos += 1
            else:
                if currentPos < len(self.__countries):
                    self.__countries[currentPos].set_color_index(-1)
                currentPos -= 1

        return solutions
