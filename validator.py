import logging

logger = logging.getLogger(__name__)

def validate(wires):
    existing_wire = set()
    error_messages = []
    for item in wires:
        wire= item.wire
        section= item.section
        if not wire:
            error_messages.append("Wire-Nummer fehlt.")
        else:
            if wire in existing_wire:
                error_messages.append(f'{wire} ist doppelt.')
                logger.warning(f"Duplicate wire: {wire.wire}")
            existing_wire.add(wire)
        if section is None:
            error_messages.append(f'{wire} hat keinen Querschnitt.')
        if item.check_cross_section() == "Kleiner Leitungsquerschnitt":
            error_messages.append(f'{wire} hat einen kleinen Leitungsquerschnitt.')

    return error_messages