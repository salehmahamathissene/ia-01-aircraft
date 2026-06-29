class MDOWorkflow:
    def __init__(self, aero, perf, struct, geom, optimizer):
        self.aero = aero
        self.perf = perf
        self.struct = struct
        self.geom = geom
        self.optimizer = optimizer

    def run(self, state, iterations=10):

        print("\n===== IA-MDO ENGINE START =====")

        for i in range(iterations):
            print(f"\nITER {i+1}")

            geom = self.geom(state)
            aero = self.aero(geom, state)
            perf = self.perf(state, aero)
            struct = self.struct(state)

            state.update({
                "LD": aero.get("LD", 0),
                "range": perf.get("range", 0),
                "mass": struct.get("mass", state.get("mtow", 900))
            })

            state = self.optimizer.step(state)

            print("LD:", state["LD"])
            print("Range:", state["range"])
            print("Mass:", state["mass"])

        print("\n===== FINAL DESIGN =====")
        print(state)

        return state
