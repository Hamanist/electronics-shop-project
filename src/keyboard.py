from src.item import Item


class MixinLanguage:
    LANGUAGE = ["RU", "EN"]

    def __init__(self):
        self.language = "EN"

    def get_language(self):
        return self.language


class Keyboard(Item, MixinLanguage):
    def __init__(self, name: str, price: float, quantity: int):
        super().__init__(name, price, quantity)
        self.mixin = MixinLanguage().get_language()
        self.__language = self.mixin

    def change_lang(self):
        if self.__language == MixinLanguage().LANGUAGE[1]:
            self.__language = MixinLanguage().LANGUAGE[0]
        else:
            self.__language = MixinLanguage().LANGUAGE[1]

    @property
    def language(self):
        return self.__language
