import pytest

from .models import Car, Truck, RaceCar


@pytest.fixture
def car():
    car_obj = Car(color="Red", max_speed=30, acceleration=10, tyre_friction=3)
    return car_obj

@pytest.fixture
def truck():
    truck_obj = Truck(color="Red", max_speed=30, acceleration=10, tyre_friction=3,max_cargo_weight=100)
    return truck_obj

@pytest.fixture
def racecar():
    racecar_obj=RaceCar(color="Red", max_speed=30, acceleration=10, tyre_friction=3)
    return racecar_obj

