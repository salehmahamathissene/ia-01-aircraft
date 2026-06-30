from mdo_core.components.base import Component

class Structure(Component):
    def compute(self, state):
        return {
            "mass": state.get("mtow", 900) * 1.02
        }
