import logging


def setup_logger():
    logging.basicConfig(
        filename="wire_validator.log",
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s",
    )

    return logging.getLogger(__name__)