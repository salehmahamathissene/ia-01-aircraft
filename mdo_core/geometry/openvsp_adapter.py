def generate_geometry(state):
    """
    In real system: call OpenVSP API
    Here: parametric surrogate model
    """

    geometry = {
        "span": state.span,
        "area": state.wing_area,
        "aspect_ratio": state.span**2 / state.wing_area,
        "sweep": state.sweep,
        "taper_ratio": 0.35
    }

    return geometry
