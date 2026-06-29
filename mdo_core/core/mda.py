from mdo_core.models.aero import aero
from mdo_core.models.structure import structure
from mdo_core.models.performance import performance
from mdo_core.core.coupler import couple

def run_mda(state):

    aero_res = aero(state)
    struct_res = structure(state)

    coupled = couple(aero_res, struct_res)

    perf_res = performance(state, coupled)

    return {
        **aero_res,
        **struct_res,
        **perf_res
    }
