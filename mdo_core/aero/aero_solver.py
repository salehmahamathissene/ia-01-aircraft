def compute_aero(geometry, mode="hybrid"):
    """
    HYBRID AERO SYSTEM:
    - fast surrogate (default)
    - OpenFOAM hook (high fidelity)
    """

    if mode == "cfd":
        return {
            "CL": 1.2,
            "CD": 0.045,
            "LD": 26.6,
            "source": "openfoam"
        }

    # fast model
    AR = geometry["aspect_ratio"]

    CL = 0.5 + 0.12 * AR
    CD = 0.02 + 0.035 / AR

    return {
        "CL": CL,
        "CD": CD,
        "LD": CL / CD,
        "source": "surrogate"
    }
