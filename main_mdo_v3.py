from mdo_core.state import AircraftState
from mdo_core.geometry.openvsp_adapter import generate_geometry
from mdo_core.aero.aero_solver import compute_aero
from mdo_core.integrations.suave_mission import run_suave_mission
from mdo_core.integrations.jsbsim_fd import run_jsbsim_dynamics
from mdo_core.integrations.registry import verify_clones


def run():

    state = AircraftState()

    print("\n===== IA-MDO v3 CLONE CONNECTED ENGINE =====\n")

    print("Checking aerospace toolchain...\n")
    print(verify_clones())

    for i in range(8):

        print(f"\nITER {i+1}")

        geo = generate_geometry(state)
        aero = compute_aero(geo)

        mission = run_suave_mission(state)
        flight = run_jsbsim_dynamics(state)

        state.range_km = mission["range_km"]
        state.ld_ratio = aero["LD"]

        print("LD:", state.ld_ratio)
        print("Range:", state.range_km)
        print("Stability:", flight["stability"])

        # simple feedback loop
        state.span += 0.05 * state.ld_ratio / 10

    print("\n===== FINAL DESIGN =====")
    print(vars(state))


if __name__ == "__main__":
    run()
