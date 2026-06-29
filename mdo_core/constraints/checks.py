def check_constraints(state):

    constraints = {}

    constraints["range_ok"] = state.range_km > 200
    constraints["ld_ok"] = state.ld_ratio > 8
    constraints["thrust_ok"] = state.engine_thrust > 2000

    state.feasible = all(constraints.values())

    return constraints
