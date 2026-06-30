class Orchestrator:
    def __init__(self, registry):
        self.registry = registry

    def run(self, state):
        aero = self.registry.get("aero")(state)
        perf = self.registry.get("performance")(state, aero)
        struct = self.registry.get("structure")(state)

        state.update({
            **aero,
            **perf,
            **struct
        })

        return state
