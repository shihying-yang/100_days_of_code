def add(*args):
    """[summary]

    :return: [description]
    :rtype: [type]
    """
    return sum(args)


def calculate(n, **kwargs):
    """[summary]

    :param n: [description]
    :type n: [type]
    """
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(f"{key} = {value}")
    # print(kwargs[key])
    n += kwargs["add"]
    print(n)
    n *= kwargs["multiply"]
    print(n)


class Car:
    """[summary]"""

    def __init__(self, **kwargs):
        """[summary]"""
        super().__init__()
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.color = kwargs.get("color")
        self.seats = kwargs.get("seats")


if __name__ == "__main__":
    # print(add(1, 2, 3))
    calculate(2, add=3, multiply=5)

    # my_car = Car(make="Nissan", model="GT-R")
    my_car = Car(seats=5)
    print(my_car.make)
    print(my_car.model)
    print(my_car.seats)
