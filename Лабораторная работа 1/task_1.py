import doctest


class Car:
    def __init__(self, brand: str, model: str, max_speed: int):
        """
        Создание и подготовка к работе объекта "Автомобиль".

        :param brand: Марка автомобиля (например, BMW, Tesla).
        :param model: Модель автомобиля (например, X5, Model S).
        :param max_speed: Максимальная скорость автомобиля в км/ч.

        Пример:
        >>> car = Car("BMW", "X5", 300) # инициализация экземпляра класса
        """

        if not isinstance(brand, str):
            raise TypeError("Название марки должно быть типа str")
        self.brand = brand

        if not isinstance(model, str):
            raise TypeError("Название модели должно быть типа str")
        self.model = model

        if not isinstance(max_speed, (int, float)):
            raise TypeError("Максимальная скорость должна быть типа int или float")
        if max_speed <= 0:
            raise ValueError("Максимальная скорость должна быть больше 0")
        self.max_speed = max_speed

    def start_engine(self) -> None:
        """
        Запускает двигатель автомобиля.
        :return: None
        Примеры:
        >>> car = Car("Tesla", "Model 3", 200)
        >>> car.start_engine()
        """
        ...

    def drive(self, speed: float) -> None:
        """
        Управление автомобилем на определённой скорости.

        :param speed: Скорость движения

        :raises ValueError: Не должна превышать max_speed. Если speed > max_speed

        :return: None
        Примеры:
        >>> car = Car("Tesla", "Model 3", 200)
        >>> car.drive(120)
        """
        if not isinstance(speed, (float, int)):
            raise TypeError("Скорость движения должна быть типа float или int")
        if speed < 0:
            raise ValueError("Скорость движения должна быть положительным числом")
        ...

    def stop(self) -> None:
        """
        Останавливает автомобиль.
        :return: None
        Примеры:
        >>> car = Car("Tesla", "Model 3", 200)
        >>> car.stop()
        """
        ...


class BankAccount:
    def __init__(self, account_number: str, balance: float, owner_name: str):
        """
         Создание и подготовка к работе объекта "Банковский счёт".

        :param account_number: Номер счёта (например, 123srj234l14j).
        :param balance: Текущий баланс на счёте.
        :param owner_name: Имя владельца счёта.

        Пример:
        >>> account = BankAccount("111ois23", 300.05, "Ivan Ivanov") # инициализация экземпляра класса
        """

        if not isinstance(account_number, str):
            raise TypeError("Номер счёта должен быть типа str")
        self.account_number = account_number

        if not isinstance(balance, (int, float)):
            raise TypeError("Текущий баланс на счете должен быть типа int или float")
        if balance < 0:
            raise ValueError("Текущий баланс не может быть отрицательным.")
        self.balance = balance

        if not isinstance(owner_name, str):
            raise TypeError("Имя владельца должен быть типа str")
        self.owner_name = owner_name

    def deposit(self, amount: float) -> None:
        """
        Внесение денег на счёт.

        :param amount: Сумма для внесения. Должна быть > 0.

        :return: None

        Примеры:
        >>> account = BankAccount("111ois23", 300.05, "Ivan Ivanov")
        >>> account.deposit(200.0)
        """
        if not isinstance(amount, (float, int)):
            raise TypeError("Сумма для внесения должна быть типа float или int")
        if amount <= 0:
            raise ValueError("Сумма должна быть больше 0.")
        ...

    def withdraw(self, amount: float) -> None:
        """
        Снятие денег со счёта.

        :param amount: Сумма для снятия. Должна быть > 0 и <= balance.

        :raises ValueError: Если amount <= 0 или amount > balance.

        :return: None

        Примеры:
        >>> account = BankAccount("111ois23", 300.05, "Ivan Ivanov")
        >>> account.withdraw(100.0)
        """

        if not isinstance(amount, (float, int)):
            raise TypeError("Сумма для снятия должна быть типа float или int")
        if amount <= 0:
            raise ValueError("Сумма должна быть больше 0.")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счёте.")
        ...

    def check_balance(self) -> float:
        """
        Проверяет текущий баланс.

        :return: Текущий баланс.
        Примеры:
        >>> account = BankAccount("12345678", 500.0, "John Doe")
        >>> account.check_balance()
        500.0
        """
        return self.balance


class House:
    def __init__(self, address: str, floors: int, area: float):
        """
        Создание и подготовка к работе объекта "Дом".

        :param address: Адрес дома.
        :param floors: Количество этажей.
        :param area: Площадь дома в квадратных метрах.

        :raises ValueError: Если floors < 1 или area <= 0

        Пример:
        >>> house = House("Wisteria Lane 5", 2, 115.3)
        """

        if not isinstance(address, str):
            raise TypeError("Адрес должен быть типа str")
        self.address = address

        if not isinstance(floors, int):
            raise TypeError("Количество этажей должен быть типа int")
        if floors < 1:
            raise ValueError("Количество этажей должно быть >= 1.")
        self.floors = floors

        if not isinstance(area, float):
            raise TypeError("Площадь дома должен быть типа float")
        if area <= 0:
            raise ValueError("Площадь дома должна быть больше 0")
        self.area = area

    def renovate(self, new_area: float) -> None:
        """
        Ремонт дома, изменение его площади.

        :param new_area: Новая площадь дома. Должна быть больше текущей площади.
        :raises ValueError: Если new_area <= текущей площади.
        :return: None
        Примеры:
        >>> house = House("Wisteria Lane 5", 2, 115.3)
        >>> house.renovate(150.0)
        """
        if not isinstance(new_area, float):
            raise TypeError("Новая площадь должна быть типа float")
        if new_area <= self.area:
            raise ValueError("Новая площадь должна быть больше текущей.")
        ...

    def add_floor(self, new_floor: int) -> None:
        """
        Добавление этажа/этажей.

        :param new_floor: Новое количество этажей. Должно быть больше текущему количеству этажей

        :raises ValueError: Если new_floor <= текущему количеству этажей.

        :return: None
        Примеры:
        >>> house = House("Wisteria Lane 5", 2, 115.3)
        >>> house.add_floor(3)
        """
        if not isinstance(new_floor, int):
            raise TypeError("Новое количество этажей должно быть типа int")
        if new_floor <= self.floors:
            raise ValueError("Новое количество этажей должно быть больше текущего количества этажей")
        ...

    def sell(self, buyer_name: str) -> None:
        """
        Продажа дома новому владельцу.

        :param buyer_name: Имя покупателя.

        :return: None
        Примеры:
        >>> house = House("Wisteria Lane 5", 2, 115.3)
        >>> house.sell("Alice Smith")
        """

        if not isinstance(buyer_name, str):
            raise TypeError("Имя покупателя должно быть типа str")
        ...


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
