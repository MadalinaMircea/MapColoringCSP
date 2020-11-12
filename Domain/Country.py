class Country:
    def __init__(self, name):
        self.__name = name
        self.__neighbours = []
        self.__color_index = None
        self.__domain = []

    def get_name(self):
        return self.__name

    def has_next_value(self):
        return self.__color_index is None or self.__color_index < len(self.__domain) - 1

    def increase_index(self):
        if self.__color_index is None:
            self.__color_index = -1
        self.__color_index += 1
        return True

    def set_color_index(self, index):
        self.__color_index = index

    def add_neighbour(self, neighbour):
        self.__neighbours.append(neighbour)

    def get_neighbours(self):
        return self.__neighbours

    def get_color(self):
        return self.__domain[self.__color_index]

    def get_color_index(self):
        return self.__color_index

    def set_domain(self, domain):
        self.__domain = domain

    def get_domain(self):
        return self.__domain

    def is_assigned(self):
        return self.__color_index is not None
