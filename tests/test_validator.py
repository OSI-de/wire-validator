from wire import Wire
from validator import validate


def test_duplicate_wire_detected():
    wires = [
        Wire("W1001", 0.35),
        Wire("W1001", 0.75),
    ]

    errors = validate(wires)

    assert any("doppelt" in error for error in errors)


def test_missing_wire_detected():
    wires = [
        Wire("", 0.35),
    ]

    errors = validate(wires)

    assert any("fehlt" in error for error in errors)


def test_missing_section_detected():
    wires = [
        Wire("W1001", None),
    ]

    errors = validate(wires)

    assert any("keinen Querschnitt" in error for error in errors)


def test_small_cross_section_detected():
    wires = [
        Wire("W1001", 0.35),
    ]

    errors = validate(wires)

    assert any("kleinen Leitungsquerschnitt" in error for error in errors)


def test_no_errors_for_valid_data():
    wires = [
        Wire("W1001", 0.75),
        Wire("W1002", 1.50),
    ]

    errors = validate(wires)

    assert errors == []