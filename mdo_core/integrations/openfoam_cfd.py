import subprocess

def run_openfoam_case(case_dir):
    """
    Hook to real OpenFOAM simulation
    (later you replace with actual solver run)
    """

    try:
        result = subprocess.run(
            ["bash", "-c", f"cd {case_dir} && ./Allrun"],
            capture_output=True,
            text=True
        )

        return {
            "status": "ok",
            "output": result.stdout[-500:]
        }

    except Exception as e:
        return {
            "status": "failed",
            "error": str(e)
        }
