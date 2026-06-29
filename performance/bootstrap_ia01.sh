#!/usr/bin/env bash
set -e

PROJECT="$HOME/InspectAfricaAerospace/IA-01"

echo "Creating IA-01 project..."

mkdir -p \
"$PROJECT/docs" \
"$PROJECT/cad" \
"$PROJECT/cfd" \
"$PROJECT/airfoils" \
"$PROJECT/simulations" \
"$PROJECT/flight_mechanics" \
"$PROJECT/structures" \
"$PROJECT/performance" \
"$PROJECT/propulsion" \
"$PROJECT/avionics" \
"$PROJECT/digital_twin" \
"$PROJECT/optimization" \
"$PROJECT/weights" \
"$PROJECT/stability" \
"$PROJECT/controls" \
"$PROJECT/systems" \
"$PROJECT/landing_gear" \
"$PROJECT/materials" \
"$PROJECT/engines" \
"$PROJECT/reports" \
"$PROJECT/figures" \
"$PROJECT/scripts" \
"$PROJECT/tests" \
"$PROJECT/configs" \
"$PROJECT/data"

cat > "$PROJECT/README.md" <<'README'
# IA-01

Inspect Africa Aircraft 01

Open-source aircraft design platform.
README

cat > "$PROJECT/performance/aircraft_math.py" <<'PY'
import math

g = 9.81
rho = 1.225

MTOW = 900
Vs = 60 / 3.6
CLmax = 1.6
AR = 8.5

W = MTOW * g

S = (2 * W) / (rho * Vs**2 * CLmax)

b = math.sqrt(AR * S)

c = S / b

WS = W / S

print("=" * 50)
print("IA-01 INITIAL DESIGN")
print("=" * 50)
print(f"Weight       : {W:.2f} N")
print(f"Wing Area    : {S:.2f} m²")
print(f"Wing Span    : {b:.2f} m")
print(f"Mean Chord   : {c:.2f} m")
print(f"Wing Loading : {WS:.2f} N/m²")
PY

echo
echo "Project created."
echo

tree "$PROJECT" -L 2

echo
python3 "$PROJECT/performance/aircraft_math.py"
