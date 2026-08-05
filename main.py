from logger_config import setup_logger
from csv_reader import load_wires
from validator import validate
from report import print_report


logger = setup_logger()


logger.info("Application started")

wires = load_wires("data/sample_wires.csv")
logger.info(f"{len(wires)} wires loaded")

errors = validate(wires)
logger.info(f"Validation finished with {len(errors)} errors")

print_report(errors)

logger.info("Application finished")