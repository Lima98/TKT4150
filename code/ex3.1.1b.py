#!/usr/bin/env python3
"""
Exercise 3.1.1b - Von Mises Equivalent Stress
Concise calculation for femur bone stress analysis
"""

import numpy as np

# Principal stresses from 1.1.a
sigma1 = -23.60  # MPa
sigma2 = -96.40  # MPa
sigma3 = 0.0     # MPa (plane stress condition)
yield_strength = 130  # MPa

# Von Mises equivalent stress
sigma_vm = np.sqrt(((sigma1-sigma2)**2 + (sigma2-sigma3)**2 +
                   (sigma3-sigma1)**2)/2)

print(f"Von Mises equivalent stress: σ_vm = {sigma_vm:.2f} MPa")
print(f"Yield strength: {yield_strength} MPa")
print(f"Safety factor: {yield_strength/sigma_vm:.2f}")
print(f"Safe operation: {'✓' if sigma_vm < yield_strength else '✗'}")
