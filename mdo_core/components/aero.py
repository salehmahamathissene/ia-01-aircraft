from mdo_core.components.base import Component

class Aero(Component):
    def compute(self, state):
        span = state.get("span", 16.5)
        area = state.get("wing_area", 28.0)

        AR = span**2 / area
        LD = 0.82 * AR

        return {"LD": LD}
