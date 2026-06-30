from mdo_core.registry import Registry
from mdo_core.orchestrator.engine import Orchestrator

# --- mock integrations (replace later with SUAVE/OpenFOAM/JSBSim) ---

def aero(state):
    AR = state["span"]**2 / state["wing_area"]
    return {"LD": 0.85 * AR}

def perf(state, aero):
    return {"range": aero["LD"] * 320}

def struct(state):
    return {"mass": state["mtow"] * 1.02}

state = {
    "mtow": 900,
    "span": 16.5,
    "wing_area": 28.0
}

registry = Registry()
registry.register("aero", aero)
registry.register("performance", perf)
registry.register("structure", struct)

engine = Orchestrator(registry)

print("===== LEVEL 5 NASA STACK START =====")

for i in range(10):
    print(f"\nITER {i+1}")
    state = engine.run(state)

    print("LD:", state["LD"])
    print("Range:", state["range"])
    print("Mass:", state["mass"])

print("\n===== FINAL DESIGN =====")
print(state)
