"""
IA-01 Aircraft Sizing Core
Simple conceptual aircraft sizing loop
"""

import math

class IA01Sizing:

    def __init__(self):
        self.MTOW = 900  # kg (initial concept)
        self.g = 9.81

    def weight(self):
        return self.MTOW * self.g

    def wing_area(self, wing_loading=300):
        W = self.weight()
        return W / wing_loading

    def aspect_ratio(self, span=16.5):
        S = self.wing_area()
        return (span**2) / S

    def summary(self):
        return {
            "MTOW_kg": self.MTOW,
            "Weight_N": self.weight(),
            "Wing_Area_m2": self.wing_area(),
            "Aspect_Ratio": self.aspect_ratio()
        }

if __name__ == "__main__":
    ia = IA01Sizing()
    print("IA-01 SIZING REPORT")
    for k, v in ia.summary().items():
        print(k, ":", v)
