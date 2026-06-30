class DigitalTwin:
    def __init__(self, components, optimizer):
        self.components = components
        self.optimizer = optimizer

    def step(self, state):

        # run all components
        for comp in self.components:
            result = comp.compute(state)
            state.update(result)

        # optimization step
        state = self.optimizer.step(state)

        return state
