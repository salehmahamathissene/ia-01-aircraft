def estimate_range(LD, fuel_fraction, speed=70):
    """
    Breguet-like simplified range model (concept level)
    """
    g = 9.81
    specific_fuel_consumption = 0.6  # simplified

    range_km = (LD / specific_fuel_consumption) * fuel_fraction * speed
    return range_km
