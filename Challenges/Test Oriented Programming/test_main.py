import main

def get_temperature_helper_function(lat, lng):
    return 26

def test_get_temperature_by_lat_lng(monkeypatch):
    lat = -3.10719
    lng = -60.0261
    
    expected = 26

    monkeypatch.setattr(main, 'get_temperature', get_temperature_helper_function)
    
    assert main.get_temperature(lat, lng) == expected
