from csv_reader import load_wires
from validator import validate
from report import print_report


wires = load_wires("data/wires.csv")
errors=validate(wires)
print_report(errors)
