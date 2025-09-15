#!/usr/bin/env python3
"""
TKT4150 - Exercise 3, Task 1.1.a)
Principal stress calculation for femur bone stress analysis

This script calculates the principal stresses for a 2D plane stress state
and determines the principal directions with angles relative to the coordinate system.

Given stress matrix:
T = [[-50, 35, 0],
     [35, -70, 0],
     [0, 0, 0]] MPa

This is a 2D plane stress problem where σ₃₃ = 0.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Given stress matrix (MPa)
T = np.array([
    [-50, 35, 0],
    [35, -70, 0],
    [0, 0, 0]
])

print("=== Exercise 3, Task 1.1.a) - Principal Stress Analysis ===")
print(f"Given stress matrix T (MPa):")
print(T)
print()

# =============================================================================
# TASK 1.1.a: Calculate principal stresses and directions
# =============================================================================

# For 2D plane stress, we work with the 2x2 in-plane stress matrix
T_2D = T[:2, :2]  # Extract the 2D stress matrix
print(f"2D plane stress matrix (MPa):")
print(T_2D)
print()

# Calculate eigenvalues (principal stresses) and eigenvectors (principal directions)
eigenvalues, eigenvectors = np.linalg.eig(T_2D)

# Sort eigenvalues and eigenvectors in descending order
sorted_indices = np.argsort(eigenvalues)[::-1]
principal_stresses = eigenvalues[sorted_indices]
principal_directions = eigenvectors[:, sorted_indices]

print("Principal Stresses (MPa):")
sigma1, sigma2 = principal_stresses
print(f"σ₁ = {sigma1:.2f} MPa")
print(f"σ₂ = {sigma2:.2f} MPa")
print(f"σ₃ = 0.00 MPa (plane stress condition)")
print()

# Calculate angles of principal directions relative to x₁-axis
angles_rad = []
angles_deg = []

for i, direction in enumerate(principal_directions.T):
    # Calculate angle with respect to x₁-axis (horizontal)
    angle_rad = np.arctan2(direction[1], direction[0])
    angle_deg = np.degrees(angle_rad)
    
    # Ensure angle is in [0, 180) range for principal directions
    if angle_deg < 0:
        angle_deg += 180
    
    angles_rad.append(angle_rad)
    angles_deg.append(angle_deg)
    
    print(f"Principal direction {i+1}: [{direction[0]:.4f}, {direction[1]:.4f}]")
    print(f"Angle with x₁-axis: {angle_deg:.2f}°")

print()

# Calculate maximum shear stress
tau_max = (sigma1 - sigma2) / 2
print(f"Maximum shear stress: τ_max = {tau_max:.2f} MPa")
print()

# =============================================================================
# Verification using analytical formulas for 2D principal stress
# =============================================================================

print("=== Verification using analytical formulas ===")

# Extract stress components
sigma_xx = T_2D[0, 0]  # σ₁₁
sigma_yy = T_2D[1, 1]  # σ₂₂
tau_xy = T_2D[0, 1]    # τ₁₂

print(f"Stress components:")
print(f"σ₁₁ = {sigma_xx:.1f} MPa")
print(f"σ₂₂ = {sigma_yy:.1f} MPa")
print(f"τ₁₂ = {tau_xy:.1f} MPa")
print()

# Calculate principal stresses using analytical formula
sigma_avg = (sigma_xx + sigma_yy) / 2
R = np.sqrt(((sigma_xx - sigma_yy) / 2)**2 + tau_xy**2)

sigma1_analytical = sigma_avg + R
sigma2_analytical = sigma_avg - R

print(f"Analytical principal stresses:")
print(f"σ₁ = {sigma1_analytical:.2f} MPa")
print(f"σ₂ = {sigma2_analytical:.2f} MPa")
print()

# Calculate principal angle using analytical formula
theta_p = 0.5 * np.arctan(2 * tau_xy / (sigma_xx - sigma_yy))
theta_p_deg = np.degrees(theta_p)

print(f"Principal angle from analytical formula: {theta_p_deg:.2f}°")
print()

# =============================================================================
# Visualization
# =============================================================================

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(15, 12))

# 1. Original stress state visualization
ax1.set_aspect('equal')
ax1.grid(True, alpha=0.3)
ax1.set_xlim(-2, 2)
ax1.set_ylim(-2, 2)

# Draw coordinate system
ax1.arrow(0, 0, 1.5, 0, head_width=0.1, head_length=0.1, fc='black', ec='black')
ax1.arrow(0, 0, 0, 1.5, head_width=0.1, head_length=0.1, fc='black', ec='black')
ax1.text(1.6, -0.2, 'x₁', fontsize=12, ha='center')
ax1.text(-0.2, 1.6, 'x₂', fontsize=12, ha='center')

# Show stress components as text
ax1.text(0.5, 0.5, f'σ₁₁ = {sigma_xx:.0f} MPa', fontsize=10, 
         bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue"))
ax1.text(0.5, -0.5, f'σ₂₂ = {sigma_yy:.0f} MPa', fontsize=10,
         bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgreen"))
ax1.text(-0.5, 0.5, f'τ₁₂ = {tau_xy:.0f} MPa', fontsize=10,
         bbox=dict(boxstyle="round,pad=0.3", facecolor="lightyellow"))

ax1.set_title('Original Stress State', fontsize=14, fontweight='bold')
ax1.set_xlabel('x₁')
ax1.set_ylabel('x₂')

# 2. Principal directions visualization
ax2.set_aspect('equal')
ax2.grid(True, alpha=0.3)
ax2.set_xlim(-2, 2)
ax2.set_ylim(-2, 2)

# Draw original coordinate system
ax2.arrow(0, 0, 1.2, 0, head_width=0.08, head_length=0.08, fc='gray', ec='gray', alpha=0.7)
ax2.arrow(0, 0, 0, 1.2, head_width=0.08, head_length=0.08, fc='gray', ec='gray', alpha=0.7)
ax2.text(1.3, -0.15, 'x₁', fontsize=10, ha='center', color='gray')
ax2.text(-0.15, 1.3, 'x₂', fontsize=10, ha='center', color='gray')

# Draw principal directions
colors = ['red', 'blue']
labels = ['σ₁', 'σ₂']
for i, (direction, color, label) in enumerate(zip(principal_directions.T, colors, labels)):
    # Draw principal direction vector
    ax2.arrow(0, 0, 1.5*direction[0], 1.5*direction[1], 
              head_width=0.1, head_length=0.1, fc=color, ec=color, linewidth=2)
    
    # Add angle arc
    angle = angles_deg[i]
    if angle < 90:
        arc_angles = np.linspace(0, np.radians(angle), 100)
    else:
        arc_angles = np.linspace(0, np.radians(angle), 100)
    
    arc_x = 0.8 * np.cos(arc_angles)
    arc_y = 0.8 * np.sin(arc_angles)
    ax2.plot(arc_x, arc_y, color=color, linewidth=1, alpha=0.7)
    
    # Label the direction
    label_x = 1.7 * direction[0]
    label_y = 1.7 * direction[1]
    ax2.text(label_x, label_y, f'{label}\n{angle:.1f}°', fontsize=10, ha='center', va='center',
             bbox=dict(boxstyle="round,pad=0.2", facecolor=color, alpha=0.3))

ax2.set_title('Principal Directions', fontsize=14, fontweight='bold')
ax2.set_xlabel('x₁')
ax2.set_ylabel('x₂')

# 3. Mohr's circle
ax3.set_aspect('equal')
ax3.grid(True, alpha=0.3)

# Calculate center and radius of Mohr's circle
center_sigma = (sigma_xx + sigma_yy) / 2
radius = np.sqrt(((sigma_xx - sigma_yy) / 2)**2 + tau_xy**2)

# Draw Mohr's circle
theta_circle = np.linspace(0, 2*np.pi, 1000)
sigma_circle = center_sigma + radius * np.cos(theta_circle)
tau_circle = radius * np.sin(theta_circle)

ax3.plot(sigma_circle, tau_circle, 'b-', linewidth=2, label="Mohr's Circle")

# Mark principal stresses
ax3.plot([sigma1, sigma2], [0, 0], 'ro', markersize=8, label='Principal Stresses')
ax3.text(sigma1, 5, f'σ₁ = {sigma1:.1f}', ha='center', fontweight='bold')
ax3.text(sigma2, 5, f'σ₂ = {sigma2:.1f}', ha='center', fontweight='bold')

# Mark original stress state
ax3.plot(sigma_xx, tau_xy, 'gs', markersize=8, label='Original State (x₁,x₂)')
ax3.plot(sigma_yy, -tau_xy, 'gs', markersize=8)

# Mark maximum shear stress
ax3.plot(center_sigma, radius, 'mo', markersize=8, label=f'τ_max = {radius:.1f}')
ax3.plot(center_sigma, -radius, 'mo', markersize=8)

ax3.axhline(y=0, color='k', linestyle='-', alpha=0.3)
ax3.axvline(x=0, color='k', linestyle='-', alpha=0.3)
ax3.set_xlabel('Normal Stress σ (MPa)', fontsize=12)
ax3.set_ylabel('Shear Stress τ (MPa)', fontsize=12)
ax3.set_title("Mohr's Circle", fontsize=14, fontweight='bold')
ax3.legend()

# 4. Summary table
ax4.axis('off')
summary_text = f"""
PRINCIPAL STRESS ANALYSIS SUMMARY

Given Stress Matrix (MPa):
σ₁₁ = {sigma_xx:.0f},  τ₁₂ = {tau_xy:.0f}
τ₂₁ = {tau_xy:.0f},  σ₂₂ = {sigma_yy:.0f}

Principal Stresses:
σ₁ = {sigma1:.2f} MPa
σ₂ = {sigma2:.2f} MPa  
σ₃ = 0.00 MPa (plane stress)

Principal Directions (angles with x₁-axis):
Direction 1: {angles_deg[0]:.2f}°
Direction 2: {angles_deg[1]:.2f}°

Maximum Shear Stress:
τ_max = {tau_max:.2f} MPa

This occurs at 45° to the principal directions.
The femur bone experiences maximum tensile stress
of {sigma1:.1f} MPa and maximum compressive stress
of {abs(sigma2):.1f} MPa.
"""

ax4.text(0.05, 0.95, summary_text, transform=ax4.transAxes, fontsize=11,
         verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle="round,pad=0.5", facecolor="lightgray", alpha=0.8))

plt.tight_layout()
plt.savefig('/Users/jan-oivindlima/Documents/arbeid/skole/9. semester/TKT4150 - Biomekanikk/Øvinger/images/ex3.1.1a-analysis.png', 
            dpi=300, bbox_inches='tight')
plt.show()

# =============================================================================
# 3D Visualization of principal directions
# =============================================================================

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Create 3D principal direction vectors (extending the 2D directions to 3D)
origin = np.array([0, 0, 0])

# Principal directions in 3D (z-component is 0 for plane stress)
dir1_3d = np.array([principal_directions[0, 0], principal_directions[1, 0], 0])
dir2_3d = np.array([principal_directions[0, 1], principal_directions[1, 1], 0])
dir3_3d = np.array([0, 0, 1])  # z-direction (σ₃ = 0)

# Plot coordinate system
ax.quiver(0, 0, 0, 1.5, 0, 0, color='gray', alpha=0.7, arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, 0, 1.5, 0, color='gray', alpha=0.7, arrow_length_ratio=0.1)
ax.quiver(0, 0, 0, 0, 0, 1.5, color='gray', alpha=0.7, arrow_length_ratio=0.1)

# Labels for coordinate system
ax.text(1.7, 0, 0, 'x₁', fontsize=12)
ax.text(0, 1.7, 0, 'x₂', fontsize=12)
ax.text(0, 0, 1.7, 'x₃', fontsize=12)

# Plot principal directions
colors = ['red', 'blue', 'green']
stresses = [sigma1, sigma2, 0]
for i, (direction, color, stress) in enumerate(zip([dir1_3d, dir2_3d, dir3_3d], colors, stresses)):
    # Scale vector length by stress magnitude (with minimum length for visibility)
    length = max(abs(stress)/50, 0.5) if stress != 0 else 1.0
    
    ax.quiver(0, 0, 0, 
              length * direction[0], 
              length * direction[1], 
              length * direction[2],
              color=color, linewidth=3, arrow_length_ratio=0.15)
    
    # Add labels
    label_pos = 1.3 * length * direction
    ax.text(label_pos[0], label_pos[1], label_pos[2], 
            f'σ{i+1} = {stress:.1f} MPa', fontsize=10, color=color, fontweight='bold')

ax.set_xlabel('x₁')
ax.set_ylabel('x₂')
ax.set_zlabel('x₃')
ax.set_title('3D Principal Stress Directions for Femur Bone', fontsize=14, fontweight='bold')

# Set equal aspect ratio
max_range = 2
ax.set_xlim([-max_range, max_range])
ax.set_ylim([-max_range, max_range])
ax.set_zlim([-max_range, max_range])

plt.savefig('/Users/jan-oivindlima/Documents/arbeid/skole/9. semester/TKT4150 - Biomekanikk/Øvinger/images/ex3.1.1a-3d.png', 
            dpi=300, bbox_inches='tight')
plt.show()

print("=== ANALYSIS COMPLETE ===")
print(f"Results saved to images/ex3.1.1a-analysis.png and images/ex3.1.1a-3d.png")
