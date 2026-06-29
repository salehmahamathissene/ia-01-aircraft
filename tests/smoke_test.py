from mdo_core.core.mda import run_mda

def test_mda():
    state = {
        "mtow": 900,
        "span": 16.5,
        "wing_area": 28.0
    }

    out = run_mda(state)

    assert "LD" in out
    assert out["LD"] > 0
