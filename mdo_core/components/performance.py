from mdo_core.components.base import Component

class Performance(Component):
    def compute(self, state):
        LD = state.get("LD", 1)
        return {
            "range": LD * 300
        }
