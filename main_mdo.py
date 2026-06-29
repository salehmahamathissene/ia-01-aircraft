from mdo_core.core.workflow import MDOWorkflow
from mdo_core.models.aero import aero_model
from mdo_core.models.performance import performance_model
from mdo_core.models.structure import structure_model
from mdo_core.geometry.openvsp_adapter import build_wing
from mdo_core.optimization.simple_optimizer import SimpleOptimizer

state = {
    "mtow": 900,
    "span": 16.5,
    "wing_area": 28.0,
    "sweep": 5
}

workflow = MDOWorkflow(
    aero=aero_model,
    perf=performance_model,
    struct=structure_model,
    geom=build_wing,
    optimizer=SimpleOptimizer()
)

workflow.run(state, iterations=10)
