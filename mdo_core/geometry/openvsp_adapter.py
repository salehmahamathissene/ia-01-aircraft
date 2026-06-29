def build_wing(state):
    span = state.get("span", 16.5)
    area = state.get("wing_area", 28.0)

    return {
        "span": span,
        "area": area,
        "mean_chord": area / span,
        "sweep": state.get("sweep", 5)
    }
