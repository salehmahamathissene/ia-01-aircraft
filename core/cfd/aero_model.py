def compute_aero(geometry):
    """
    Replace later with OpenFOAM / Navier-Stokes solver
    """

    span = geometry["span"]
    area = geometry["area"]

    AR = span**2 / area

    # crude aerodynamic estimation (will be replaced later)
    LD = 0.5 * AR + 4.0

    return {
        "aspect_ratio": AR,
        "LD": LD,
        "CL": 0.9,
        "CD": 0.05
    }
