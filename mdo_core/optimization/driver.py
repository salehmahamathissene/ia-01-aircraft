class Driver:
    def __init__(self):
        self.step_size = 0.02

    def run_step(self, state):
        # gradient-free heuristic optimization
        state["span"] *= 1.01
        state["wing_area"] *= 0.998
        return state
