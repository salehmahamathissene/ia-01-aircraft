"""
IA-01 → OpenVSP Interface (Prototype)
Connects aircraft sizing to parametric geometry
"""

def generate_wing(span, area, sweep=5):
    """
    Placeholder interface for OpenVSP geometry generation
    Later this will call real OpenVSP API
    """

    chord = area / span

    geometry = {
        "span": span,
        "area": area,
        "mean_chord": chord,
        "sweep_deg": sweep
    }

    print("Generated OpenVSP Wing Geometry:", geometry)

    return geometry
