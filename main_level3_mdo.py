from mdo_core.core.mda import run_mda
from mdo_core.optimization.driver import Driver

state = {
    "mtow": 900,
    "span": 16.5,
    "wing_area": 28.0,
    "sweep": 5
}

driver = Driver()

print("===== LEVEL 3 NASA MDO START =====")

for i in range(12):
    print(f"\nITER {i+1}")

    results = run_mda(state)

    state.update(results)

    print("LD:", results["LD"])
    print("Range:", results["range"])
    print("Mass:", results["mass"])

    state = driver.run_step(state)

print("\n===== FINAL DESIGN =====")
print(state)
