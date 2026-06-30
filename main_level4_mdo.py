from mdo_core.components.aero import Aero
from mdo_core.components.structure import Structure
from mdo_core.components.performance import Performance
from mdo_core.digital_twin.engine import DigitalTwin
from mdo_core.optim.optimizer import GradientFreeOptimizer

state = {
    "mtow": 900,
    "span": 16.5,
    "wing_area": 28.0
}

engine = DigitalTwin(
    components=[Aero(), Structure(), Performance()],
    optimizer=GradientFreeOptimizer()
)

print("===== LEVEL 4 NASA DIGITAL TWIN START =====")

for i in range(12):
    print(f"\nITER {i+1}")
    state = engine.step(state)

    print("LD:", state.get("LD"))
    print("Range:", state.get("range"))
    print("Mass:", state.get("mass"))

print("\n===== FINAL DESIGN =====")
print(state)
