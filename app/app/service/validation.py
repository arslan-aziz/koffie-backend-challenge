import re


def validate_vin(vin: str) -> bool:
    """Validate vin satisfies basic format checks.

    :param vin: Candiate vehicle identifier number.
    """
    return re.match(r"[A-Za-z0-9]{17}$", vin) is not None
