import pytest
from practice import Vehicle, ElectricVehicle 

def test_vehicle_fuel_up():
    vehicle = Vehicle("Toyota", "Camry", "Sedan")
    assert vehicle.fuel_up() == 'Gas tank is now full.'
    assert vehicle.fuel_level == 14

def test_vehicle_drive():
    vehicle = Vehicle("Toyota", "Camry", "Sedan")
    assert vehicle.drive() == 'The Camry is now driving.'

def test_electric_vehicle_charge():
    ev = ElectricVehicle("Tesla", "Model S", "Sedan")
    assert ev.charge() == 'The vehicle is now charged.'
    assert ev.charge_level == 100

def test_electric_vehicle_fuel_up(capsys):
    ev = ElectricVehicle("Tesla", "Model S", "Sedan")
    ev.fuel_up()

    captured = capsys.readouterr().out.strip()
    assert 'This vehicle has no fuel tank.' in captured
    assert ev.fuel_level == 0