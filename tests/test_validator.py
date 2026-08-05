from wire import Wire
from validator import validate


def test_duplicate_wire_detected():
    wires = [
        Wire("W1001", 0.35),
        Wire("W1001", 0.75),
    ]

    errors = validate(wires)

    assert any("doppelt" in error for error in errors)