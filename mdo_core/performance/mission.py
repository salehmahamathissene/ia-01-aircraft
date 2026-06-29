def compute_mission(state, aero, propulsion):

    ld = aero["LD"]

    # Breguet-style simplified range
    range_km = 300 * ld

    state.ld_ratio = ld
    state.range_km = range_km

    return state
