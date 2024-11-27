def test_my_truck(truck):
    # Sample assert
    assert truck.max_speed == 30
def test_truck_load(truck):
      load_value=10
      check=truck.load(load_value)
      assert "Cannot load cargo during motion"==check

def test_truck_unload(truck):
    load_value=10
    check=truck.unload(load_value)
    assert "Cannot load cargo during motion"==check

def test_truck_sound_horn(truck):
    check=truck.sound_horn()
    assert check=="Honk Honk"