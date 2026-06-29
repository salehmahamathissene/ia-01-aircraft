class Aircraft:

    def __init__(self):

        self.name = "IA-01"

        self.mtow = 900

        self.payload = 250

        self.range = 1000

        self.cruise = 200

        self.service_ceiling = 4500

        self.stall_speed = 60

        self.engine = "Single Piston"

        self.configuration = "High Wing"

aircraft = Aircraft()

print(vars(aircraft))
