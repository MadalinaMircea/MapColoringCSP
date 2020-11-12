from copy import deepcopy


class CountryReduceNeighbours:
    def __init__(self, name):
        self.__name = name
        self.__neighbours = []
        self.__color_index = None
        self.__domain = []
        self.__domain_dict = {}

    def get_name(self):
        return self.__name

    def has_next_value(self):
        return self.__color_index is None or self.__color_index < len(self.__domain) - 1

    def increase_index(self):
        prev = self.__color_index
        if self.__color_index is None:
            self.__color_index = 0
        else:
            self.__color_index += 1

        for n in self.__neighbours:
            if prev is not None:
                n.add_to_domain(self.__domain[prev], self.__name)
            if not n.remove_from_domain(self.__domain[self.__color_index], self.__name):
                return False
        return True

    def remove_from_domain(self, value, sender):
        if self.__color_index is None:
            try:
                index = self.__domain.index(value)
                self.__domain.pop(index)
                self.__domain_dict[value].append(sender)
                # if index <= self.__color_index:
                #     self.__color_index -= 1
            except:
                pass

        if len(self.__domain) == 0:
            return False

        return True

    def add_to_domain(self, index, sender):
        if self.__color_index is None:
            try:
                self.__domain_dict[index].remove(sender)
            except ValueError:
                pass

            if len(self.__domain_dict[index]) == 0 and index not in self.__domain:
                self.__domain.append(index)

        # self.__color_index = -1

    def reset_color_index(self):
        for n in self.__neighbours:
            n.add_to_domain(self.__domain[self.__color_index], self.__name)

        self.__color_index = None

    def add_neighbour(self, neighbour):
        self.__neighbours.append(neighbour)

    def get_neighbours(self):
        return self.__neighbours

    def get_color(self):
        return self.__domain[self.__color_index]

    def get_color_index(self):
        return self.__color_index

    def set_domain(self, domain):
        self.__domain = deepcopy(domain)
        for c in self.__domain:
            self.__domain_dict[c] = []

    def get_domain(self):
        return self.__domain

    def is_assigned(self):
        return self.__color_index is not None
