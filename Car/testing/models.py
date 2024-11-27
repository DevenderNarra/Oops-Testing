import math

class Car:
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        if max_speed <= 0:
            raise ValueError("Invalid value for max_speed")

        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.is_engine_started = False
        self.current_speed=0
    def get_current_speed(self):
        return self.current_speed

    def start(self):
        self.current_speed += self.acceleration

    def start_engine(self):
        self.is_engine_started = True

    def accelerate(self):
        if self.is_engine_started:
            self.current_speed += self.acceleration
        else:
            print("Start the engine to accelerate")

    def apply_brakes(self):
        self.current_speed -= self.tyre_friction

    def sound_horn(self):
        return "Beep Beep"

    def stop_engine(self):
        self.is_engine_started = False

    def __str__(self):
        return self.color

class Truck:
    def __init__(self, color, max_speed, acceleration, tyre_friction, max_cargo_weight):
            if max_speed <= 0:
                raise ValueError("Invalid value for max_speed")

            self.color = color
            self.max_speed = max_speed
            self.acceleration = acceleration
            self.tyre_friction = tyre_friction
            self.max_cargo_weight = max_cargo_weight

    def load(self,value):
            if value < 0:
                raise ValueError("Invalid value for max_cargo_weight")
            if value>=self.max_cargo_weight:
                return "Cannot load cargo more than max limit: 100"
            if value<100 and value>0:
                return "Cannot load cargo during motion"


    def unload(self,value):
            if value < 0:
                raise ValueError("Invalid value for max_cargo_weight")
            if value>=self.max_cargo_weight:
                return "Cannot load cargo more than max limit: 100"
            if value<100 and value>0:
                return "Cannot load cargo during motion"

    def sound_horn(self):
            return "Honk Honk"

class RaceCar:
    def __init__(self,color,max_speed,acceleration,tyre_friction):
        if max_speed <= 0:
            raise ValueError("Invalid value for max_speed")

        self.color = color
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.tyre_friction = tyre_friction
        self.nitro = 0
        self.is_engine_started=False
        self.current_speed=0

    def get_current_speed(self):
        return self.current_speed

    def start(self):
        self.is_engine_started=True

    def apply_breaks(self):
        if self.current_speed >= self.current_speed//2:
             self.nitro=10
        self.current_speed -= self.tyre_friction

    def accelerate(self):
        if self.is_engine_started:
            self.current_speed += self.acceleration
        if self.nitro >= 10:
            # Use nitro
            extra_speed = math.ceil(0.3 * self.acceleration)
            self.current_speed += extra_speed
            self.nitro -= 10
        else:
            return "Start the engine to accelerate"

    def sound_horn(self):
        return "Peep Peep\nBeep Beep"
