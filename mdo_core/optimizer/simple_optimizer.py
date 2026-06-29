import random

def optimize(state):

    # tiny perturbation search (CMA-ES will replace later)

    state.span += random.uniform(-0.2, 0.2)
    state.wing_area += random.uniform(-0.3, 0.3)
    state.engine_thrust += random.uniform(-50, 50)

    return state
