import math

# -----------------------------
# IA-01 Conceptual Design
# -----------------------------

g = 9.81
rho = 1.225

# Mission Requirements
MTOW = 900.0              # kg
stall_speed = 60 / 3.6    # m/s
CLmax = 1.6

# Aircraft assumptions
aspect_ratio = 8.5

# -----------------------------
# Calculations
# -----------------------------

weight = MTOW * g

wing_area = (2 * weight) / (rho * stall_speed**2 * CLmax)

wing_loading = weight / wing_area

wing_span = math.sqrt(aspect_ratio * wing_area)

mean_chord = wing_area / wing_span

print("=" * 60)
print(" IA-01 CONCEPTUAL DESIGN")
print("=" * 60)

print(f"MTOW                : {MTOW:.1f} kg")
print(f"Weight              : {weight:.1f} N")
print(f"Wing Area           : {wing_area:.2f} m²")
print(f"Wing Span           : {wing_span:.2f} m")
print(f"Mean Chord          : {mean_chord:.2f} m")
print(f"Wing Loading        : {wing_loading:.2f} N/m²")
print(f"Aspect Ratio        : {aspect_ratio:.1f}")
