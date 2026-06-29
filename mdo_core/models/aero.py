def aero(state):
    AR = state["span"]**2 / state["wing_area"]
    LD = 0.85 * AR
    return {"LD": LD}
