class GradientFreeOptimizer:
    def step(self, state):
        state["span"] *= 1.01
        state["wing_area"] *= 0.999
        return state
