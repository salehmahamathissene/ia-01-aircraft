def couple(aero, struct):
    """
    Safe coupling layer (NASA-style defensive design)
    """

    if aero is None or struct is None:
        raise ValueError("Coupler received invalid subsystem outputs")

    return {
        "LD": aero.get("LD", 1.0),
        "mass": struct.get("mass", 900.0)
    }
