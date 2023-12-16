# 1. დაწერეთ პითონის  Car (ატრიბუტები: brand, model, year) კლასი და მოახდინეთ ამ კლასისთვის __new__ და __init__ მეთოდის გადაფარვა.

class Car:
    def _new(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

    def _init(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def __str__(self):
        return f"{self.year} {self.brand} {self.model}"

car = Car._new(Car)
car._init(brand="Toyota", model="Camry", year=2022)
print(car)

# 2. შექმენით დეკორატორი, რომელიც დაითვლის და დაგვიბეჭდავს დროს, თუ რა დრო დასჭირდა ობიექტის მეთოდის შესრულებას და დაგვიწერს რა ატრიბუტები აქვს გადმოცემული ობიექტს

import time

class Timer:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = self._get_current_time()
        result = self.func(*args, **kwargs)

        end_time = self._get_current_time()
        elapsed_time = end_time - start_time

        print(f"Method '{self.func.__name__}' took {elapsed_time} seconds to execute.")
        print(f"Arguments passed to '{self.func.__name__}':")
        print(f"Positional arguments: {args}")
        print(f"Keyword arguments: {kwargs}")

        return result

    def _get_current_time(self):
        return time.time()

@Timer
def example(arg1, arg2, kwarg1=None, kwarg2=None):
    return f"Result from example_function: {arg1}, {arg2}, {kwarg1}, {kwarg2}"

result = example("Value1", "Value2", kwarg1="KeywordValue1", kwarg2="KeywordValue2")
print(result)

# 3. Car კლასს დაუმატეთ  თითეული ატრიბუტისთვის set და get ფუნქტორი მათი ცვლილებებისთვის და დაამატეთ ვალიდაციები თითოეული ატრიბუტისთვის.

class Car:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

    def __init__(self, brand, model, year):
        self._brand = None
        self._model = None
        self._year = None

        self.set_brand(brand)
        self.set_model(model)
        self.set_year(year)

    def __str__(self):
        return f"{self._year} {self._brand} {self._model}"

    def get_brand(self):
        return self._brand

    def set_brand(self, brand):
        if isinstance(brand, str) and brand.strip():
            self._brand = brand
        else:
            raise ValueError("Brand must be a non-empty string")

    def get_model(self):
        return self._model

    def set_model(self, model):
        if isinstance(model, str) and model.strip():
            self._model = model
        else:
            raise ValueError("Model must be a non-empty string")

    def get_year(self):
        return self._year

    def set_year(self, year):
        if isinstance(year, int):
            self._year = year
        else:
            raise ValueError("Year must be an integer")

car = Car(brand="Toyota", model="Camry", year=2022)
print(car)

car.set_brand("Honda")
car.set_model("Accord")
car.set_year(2023)

print(f"Brand: {car.get_brand()}")
print(f"Model: {car.get_model()}")
print(f"Year: {car.get_year()}")
print(car)