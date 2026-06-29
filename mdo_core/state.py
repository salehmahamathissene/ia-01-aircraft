class AircraftState:
    """
    Central state of the aircraft design.
    Everything flows through this object (MDO style).
    """

    def __init__(self):
        # Design variables
        self.span = 16.0
        self.wing_area = 28.0
        self.sweep = 5.0
        self.thickness_ratio = 0.12
        self.engine_thrust = 3000

        # Performance outputs
        self.lift = 0.0
        self.drag = 0.0
        self.ld_ratio = 0.0
        self.range_km = 0.0

        # Constraints
        self.stall_speed = 0.0
        self.thrust_margin = 0.0
        self.feasible = True

        # Mass properties
        self.mtow = 900.0
        self.fuel_mass = 0.0
