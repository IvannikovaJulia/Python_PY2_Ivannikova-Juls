class Animal:
    """
    Базовый класс для всех животных.
    """

    def __init__(self, name: str, age: int):
        """
        Инициализация объекта Animal.

        :param name: Имя животного
        :param age: Возраст животного
        """
        self._name = name  # Инкапсуляция: имя не должно изменяться напрямую
        self.age = age

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта для пользователя.
        """
        return f"Животное: {self._name}, возраст: {self.age} лет"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для отладки.
        """
        return f"Animal(name={self._name!r}, age={self.age})"

    def make_sound(self) -> str:
        """
        Метод, который должны переопределить дочерние классы для указания звука животного.
        """
        return "Неизвестный звук"


class Dog(Animal):
    """
    Дочерний класс, представляющий собаку.
    """

    def __init__(self, name: str, age: int, breed: str):
        """
        Инициализация объекта Dog.

        :param name: Имя собаки
        :param age: Возраст собаки
        :param breed: Порода собаки
        """
        super().__init__(name, age)
        self.breed = breed

    def __str__(self) -> str:
        """
        Переопределение метода __str__ для более информативного вывода.
        """
        return f"Собака: {self._name}, порода: {self.breed}, возраст: {self.age} лет"

    def make_sound(self) -> str:
        """
        Переопределенный метод из базового класса.

        Собака издает лай, в отличие от базового животного, у которого звук неизвестен.
        """
        return "Гав-гав!"

    def fetch(self) -> str:
        """
        Метод, уникальный для собаки: приносит брошенный предмет.
        """
        return f"{self._name} приносит предмет."


if __name__ == "__main__":
    dog = Dog("Бобик", 3, "Лабрадор")
    print(dog)               # Выводит информацию о собаке
    print(repr(dog))         # Отладочное представление
    print(dog.make_sound())  # Выводит "Гав-гав!"
    print(dog.fetch())       # Выводит "Бобик приносит предмет."
