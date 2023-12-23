from src.item import Item


class Phone(Item):
    def __init__(self, name: str, price: float, quantity: int, number_of_sim):
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    @property
    def number_of_sim(self):
        return self.__number_of_sim

    @number_of_sim.setter
    def number_of_sim(self, zero_sim):
        if not isinstance(zero_sim, int):
            raise ValueError('SIM-карты должны быть целым числом')
        if zero_sim <= 0:
             self.__number_of_sim = ValueError('Количество физических SIM-карт должно быть больше нуля.')
        else:
            self.__number_of_sim = zero_sim

    def __repr__(self):
        return f"Phone('{self.name}', {self.price}, {self.quantity}, {self.number_of_sim})"
