from wire import Wire

def test_valid_wire():
    wire = Wire("W1001", 0.35)

    assert wire.is_valid() is True

def test_missing_wire():
    wire = Wire("", 0.35)

    assert wire.is_valid() is False

def test_missing_section():
    wire = Wire("W1001", None)

    assert wire.is_valid() is False

def test_small_cross_section():
    wire = Wire("W1001", 0.35)

    assert wire.check_cross_section() == "Kleiner Leitungsquerschnitt"

def test_normal_cross_section():
    wire = Wire("W1001", 1.5)

    assert wire.check_cross_section() == "OK"