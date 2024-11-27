def test_get_current_speed(car):
    initial=0
    check=car.get_current_speed()
    assert check==initial

def test_start_engine(car):
    car.start_engine()
    assert car.is_engine_started==True

def test_accelerate_car(car):
    car.start_engine()
    car.accelerate()

    assert car.current_speed == 10


def test_apply_break_when_car_current_speed_is_more_than_tyre_friction(car):
    car.start_engine()
    car.accelerate()
    car.apply_brakes()

    assert car.current_speed == 7


def test_accelerate_car_more_than_max_limit(car):

    car.start_engine()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()
    car.accelerate()

    assert car.current_speed == 50

def test_car_horn_sound(car):
    act=car.sound_horn()
    assert act=="Beep Beep"

def test_car_stop(car):
    car.stop_engine()
    assert car.is_engine_started==False

