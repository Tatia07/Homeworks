from io import StringIO
from practice import Vehicle, ElectricVehicle
import unittest
import sys

class TestPractice(unittest.TestCase):
    def test_init(self):
        test_vehicle = Vehicle(brand="Mercedes", model="GLA", type="SUV")

    def test_fuel_up(self):
        test_vehicle = Vehicle(brand="Mercedes", model="GLA", type="SUV")
        result = test_vehicle.fuel_up()
        self.assertEqual(result, 'Gas tank is now full.')
        self.assertEqual(test_vehicle.fuel_level, test_vehicle.gas_tank_size)

    def test_drive(self):
        test_vehicle = Vehicle(brand="Mercedes", model="GLA", type="SUV")
        result = test_vehicle.drive()
        self.assertEqual(result, 'The GLA is now driving.')

class TestPractice2(unittest.TestCase):
    def test_charge_electric_vehicle(self):
        test_ev = ElectricVehicle(brand="Tesla", model="Model S", type="Sedan")

        result = test_ev.charge()
        self.assertEqual(result, 'The vehicle is now charged.')
        self.assertEqual(test_ev.charge_level, 100)

    def test_fuel_up_electric_vehicle(self):
        test_ev = ElectricVehicle(brand="Tesla", model="Model S", type="Sedan")

        captured_output = StringIO()
        sys.stdout = captured_output
        
        try:
            result = test_ev.fuel_up()
            self.assertRegex(captured_output.getvalue().strip(), 'This vehicle has no fuel tank.')
            self.assertEqual(result, 'This vehicle has no fuel tank!')
        finally:
            sys.stdout = sys.__stdout__ 

if __name__ == '__main__':
    unittest.main()