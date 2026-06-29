from core.sizing.ia01_sizing import IA01Sizing
from core.cfd.interface import run_cfd_simulation
from core.geometry.openvsp_interface import generate_wing

def main():
    print("===== IA-01 FULL AIRCRAFT PIPELINE =====")

    # 1. Sizing
    sizing = IA01Sizing()
    report = sizing.summary()

    print("\n--- SIZING ---")
    for k, v in report.items():
        print(k, ":", v)

    # 2. Geometry (OpenVSP layer)
    print("\n--- GEOMETRY ---")
    geom = generate_wing(
        span=16.5,
        area=report["Wing_Area_m2"]
    )

    # 3. CFD
    print("\n--- CFD ---")
    aero = run_cfd_simulation(geom)

    print(aero)

if __name__ == "__main__":
    main()
