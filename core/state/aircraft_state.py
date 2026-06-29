class AircraftState:
    """
    Central aircraft state for iterative design loop
    """

    def __init__(self):
        self.MTOW = 900.0  # kg
        self.fuel_fraction = 0.25

        self.span = 16.5
        self.wing_area = 29.0

        self.LD = 12.0

        self.converged = False
        self.iteration = 0

    def update_weight(self, new_mtow):
        self.MTOW = new_mtow

    def summary(self):
        return {
            "MTOW": self.MTOW,
            "Span": self.span,
            "WingArea": self.wing_area,
            "L/D": self.LD,
            "Iteration": self.iteration
        }
