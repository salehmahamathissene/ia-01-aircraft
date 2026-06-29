from core.state.aircraft_state import AircraftState
from core.geometry.openvsp_interface import generate_wing
from core.cfd.aero_model import compute_aero
from core.performance.performance_model import estimate_range

def run_design_loop(max_iter=10):
    state = AircraftState()

    print("\n===== IA-01 DESIGN LOOP START =====")

    for i in range(max_iter):

        state.iteration = i + 1

        # 1. Geometry
        geometry = generate_wing(state.span, state.wing_area)

        # 2. Aero
        aero = compute_aero(geometry)
        state.LD = aero["LD"]

        # 3. Performance
        range_km = estimate_range(state.LD, state.fuel_fraction)

        # 4. Weight update (simple convergence rule)
        new_mtow = state.MTOW * (1 + 0.01 * (15 / state.LD))

        print(f"\nITER {i+1}")
        print("L/D:", state.LD)
        print("Range:", range_km)
        print("MTOW:", new_mtow)

        # convergence check
        if abs(new_mtow - state.MTOW) < 0.1:
            state.converged = True
            break

        state.update_weight(new_mtow)

    print("\n===== FINAL STATE =====")
    print(state.summary())

    return state
