from mdo_core.state import AircraftState
from mdo_core.geometry.openvsp_adapter import generate_geometry
from mdo_core.aero.aero_solver import compute_aero
from mdo_core.integrations.suave_mission import run_suave_mission
from mdo_core.integrations.jsbsim_fd import run_jsbsim_dynamics
from mdo_core.constraints.checks import check_constraints
from mdo_core.optimizer.simple_optimizer import optimize


def run_mdo(iterations=10):

    state = AircraftState()

    print("\n===== IA-MDO v2 (CLONE-COUPLED ENGINE) START =====\n")

    for i in range(iterations):

        print(f"\nITER {i+1}")

        geometry = generate_geometry(state)

        aero = compute_aero(geometry, mode="surrogate")

        mission = run_suave_mission(state)

        flight = run_jsbsim_dynamics(state)

        state.range_km = mission["range_km"]
        state.ld_ratio = aero["LD"]

        constraints = check_constraints(state)

        print("LD:", state.ld_ratio)
        print("Range:", state.range_km)
        print("Stability:", flight["stability"])
        print("Feasible:", state.feasible)

        state = optimize(state)

    print("\n===== FINAL DESIGN (CLONE-COUPLED) =====")
    print(vars(state))


if __name__ == "__main__":
    run_mdo(12)
