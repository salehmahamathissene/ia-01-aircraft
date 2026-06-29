def compute_thrust(state):
    """
    Simple turbofan-like scaling model
    """

    thrust = state.engine_thrust

    # mass penalty
    efficiency = 0.85

    return {
        "thrust": thrust * efficiency
    }
