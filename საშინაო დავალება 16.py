# შექმენი ნებისმიერი კლასი შენი ფანტაზიით, რომელსაც ექნება __init__ კონსტრუქტორი და __repr__ მეთოდი,
# კლასის და ობიექტის ცვლადები, მინიმუმ 1 private პარამეტრი საკუთარი setter_ით , მინიმუმ ერთი კლასის და სტატიკური მეთოდი.
# მინიმუმ ერთი ობიექტის დამალული მეთოდი.

class Car:
    max_speed = 200

    def __init__(self, manufacturer, model, year, mileage=0):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self._mileage = mileage 

    def __repr__(self):
        return f"Car({self.manufacturer}, {self.model}, {self.year}, Mileage: {self._mileage} miles)"

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, value):
        if value >= 0:
            self._mileage = value
        else:
            print("Mileage must be a non-negative value.")

    def drive(self, distance):
        self._update_mileage(distance)
        print(f"The car has been driven for {distance} miles.")

    def _update_mileage(self, distance):
        self._mileage += distance

    @classmethod
    def calculate_distance(cls, time, speed):
        return time * speed

    @staticmethod
    def get_max_speed():
        return Car.max_speed


my_car = Car("BMW", "X5", 2023, mileage=5000)
print(my_car)

my_car.drive(50)
print(f"Current mileage: {my_car.mileage} miles")

hours = 4
speed = 80

estimated_distance = Car.calculate_distance(hours, speed)
print(f"Estimated distance for {hours} hours at {speed} mph: {estimated_distance} miles")

max_speed = Car.get_max_speed()
print(f"Max speed of any car: {max_speed} mph")