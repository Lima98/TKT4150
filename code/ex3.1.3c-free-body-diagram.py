#!/usr/bin/env python3
"""
Exercise 3.1.3c: Free Body Diagram for Cylindrical Pressure Vessel
TKT4150 - Biomechanics

This script creates a free body diagram showing the forces acting on a 
cylindrical pressure vessel cut perpendicular to its axis, used to derive
the axial stress formula in Laplace's law.
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

def create_free_body_diagram():
    """Create free body diagram for cylindrical pressure vessel axial stress analysis"""
    
    # Create figure and axis
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8))
    fig.suptitle('Exercise 3.1.3c: Free Body Diagram - Cylindrical Pressure Vessel', 
                 fontsize=16, fontweight='bold')
    
    # === LEFT PLOT: 3D VIEW OF CYLINDER ===
    ax1.set_xlim(-3, 3)
    ax1.set_ylim(-2, 4)
    ax1.set_aspect('equal')
    ax1.set_title('3D View: Cylinder with Cut Plane', fontsize=14, fontweight='bold')
    
    # Draw cylinder body
    cylinder_rect = patches.Rectangle((-1, 0), 2, 3, linewidth=2, 
                                    edgecolor='black', facecolor='lightblue', alpha=0.7)
    ax1.add_patch(cylinder_rect)
    
    # Draw cylinder top (ellipse for 3D effect)
    ellipse_top = patches.Ellipse((0, 3), 2, 0.6, linewidth=2, 
                                edgecolor='black', facecolor='lightblue', alpha=0.8)
    ax1.add_patch(ellipse_top)
    
    # Draw cylinder bottom (ellipse)
    ellipse_bottom = patches.Ellipse((0, 0), 2, 0.6, linewidth=2, 
                                   edgecolor='black', facecolor='lightblue', alpha=0.8)
    ax1.add_patch(ellipse_bottom)
    
    # Draw cut plane
    cut_y = 1.5
    ax1.plot([-1.2, 1.2], [cut_y, cut_y], 'r--', linewidth=3, label='Cut Plane')
    
    # Add dimensions
    ax1.annotate('', xy=(1, -0.5), xytext=(-1, -0.5),
                arrowprops=dict(arrowstyle='<->', color='red', lw=2))
    ax1.text(0, -0.8, '2r', ha='center', fontsize=12, color='red', fontweight='bold')
    
    ax1.annotate('', xy=(1.5, 0), xytext=(1.5, 3),
                arrowprops=dict(arrowstyle='<->', color='blue', lw=2))
    ax1.text(1.8, 1.5, 'L', ha='center', va='center', fontsize=12, color='blue', fontweight='bold')
    
    # Wall thickness indication
    ax1.plot([1, 1.15], [1, 1], 'g-', linewidth=3)
    ax1.text(1.3, 1, 't', ha='left', va='center', fontsize=12, color='green', fontweight='bold')
    
    # Labels
    ax1.text(0, 3.5, 'Cylinder Axis', ha='center', fontsize=12, fontweight='bold')
    ax1.text(0, -1.5, 'Radius r, Wall thickness t', ha='center', fontsize=11)
    
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    
    # === RIGHT PLOT: FREE BODY DIAGRAM ===
    ax2.set_xlim(-3, 3)
    ax2.set_ylim(-2, 3)
    ax2.set_aspect('equal')
    ax2.set_title('Free Body Diagram: Forces on Cut Section', fontsize=14, fontweight='bold')
    
    # Draw free body (circular cross-section with wall)
    
    # Inner circle (pressure acts here)
    inner_circle = patches.Circle((0, 0), 1, linewidth=2, 
                                edgecolor='blue', facecolor='lightcyan', alpha=0.6)
    ax2.add_patch(inner_circle)
    
    # Wall ring
    outer_circle = patches.Circle((0, 0), 1.15, linewidth=3, 
                                edgecolor='black', facecolor='none')
    ax2.add_patch(outer_circle)
    
    # === PRESSURE FORCES (distributed, shown as arrows) ===
    # Create pressure arrows pointing outward
    n_arrows = 12
    angles = np.linspace(0, 2*np.pi, n_arrows, endpoint=False)
    
    for angle in angles:
        x_start = 0.8 * np.cos(angle)
        y_start = 0.8 * np.sin(angle)
        dx = 0.3 * np.cos(angle)
        dy = 0.3 * np.sin(angle)
        
        ax2.arrow(x_start, y_start, dx, dy, head_width=0.08, 
                 head_length=0.05, fc='red', ec='red', linewidth=1.5)
    
    # Pressure force resultant (axial)
    ax2.arrow(0, 0, 0, 1.8, head_width=0.15, head_length=0.1, 
             fc='red', ec='red', linewidth=3, alpha=0.8)
    ax2.text(0.3, 1.8, r'$F_{pressure} = p_i \cdot \pi r^2$', fontsize=12, 
             color='red', fontweight='bold', ha='left')
    
    # === AXIAL STRESS FORCES (around the ring) ===
    # Show stress arrows around the wall ring
    n_stress_arrows = 8
    stress_angles = np.linspace(0, 2*np.pi, n_stress_arrows, endpoint=False)
    
    for angle in stress_angles:
        x_pos = 1.3 * np.cos(angle)
        y_pos = 1.3 * np.sin(angle)
        dx = -0.25 * np.cos(angle)
        dy = -0.25 * np.sin(angle)
        
        ax2.arrow(x_pos, y_pos, dx, dy, head_width=0.06, 
                 head_length=0.04, fc='green', ec='green', linewidth=1.2)
    
    # Stress force resultant (axial, opposing pressure)
    ax2.arrow(0, -1.8, 0, 1.6, head_width=0.15, head_length=0.1, 
             fc='green', ec='green', linewidth=3, alpha=0.8)
    ax2.text(0.3, -1.8, r'$F_{axial} = \sigma_z \cdot 2\pi r t$', fontsize=12, 
             color='green', fontweight='bold', ha='left')
    
    # === ANNOTATIONS AND LABELS ===
    
    # Radius annotation
    ax2.plot([0, 1], [0, 0], 'k--', linewidth=1)
    ax2.text(0.5, -0.15, 'r', ha='center', fontsize=12, fontweight='bold')
    
    # Wall thickness
    ax2.plot([1, 1.15], [0.3, 0.3], 'k-', linewidth=2)
    ax2.text(1.08, 0.4, 't', ha='center', fontsize=10, fontweight='bold')
    
    # Pressure indication
    ax2.text(0, 0, r'$p_i$', ha='center', va='center', fontsize=14, 
             color='red', fontweight='bold')
    
    # Equilibrium equation
    ax2.text(0, -2.5, 'Equilibrium: $F_{axial} = F_{pressure}$', 
             ha='center', fontsize=12, fontweight='bold', 
             bbox=dict(boxstyle="round,pad=0.3", facecolor="yellow", alpha=0.7))
    
    # Legend
    ax2.plot([], [], 'r-', linewidth=3, label='Pressure Forces')
    ax2.plot([], [], 'g-', linewidth=3, label='Axial Stress Forces')
    ax2.legend(loc='upper right')
    
    ax2.grid(True, alpha=0.3)
    ax2.set_xlabel('Distance from center', fontsize=11)
    ax2.set_ylabel('Distance from center', fontsize=11)
    
    # Remove ticks for cleaner look
    ax1.set_xticks([])
    ax1.set_yticks([])
    ax2.set_xticks([])
    ax2.set_yticks([])
    
    plt.tight_layout()
    return fig

def create_force_analysis_diagram():
    """Create a detailed force analysis diagram"""
    
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    fig.suptitle('Force Analysis for Axial Stress Derivation', fontsize=16, fontweight='bold')
    
    ax.set_xlim(-4, 4)
    ax.set_ylim(-3, 4)
    ax.set_aspect('equal')
    
    # === MAIN DIAGRAM ===
    
    # Draw cross-section view
    outer_circle = patches.Circle((0, 0), 1.5, linewidth=3, 
                                edgecolor='black', facecolor='lightgray', alpha=0.3)
    ax.add_patch(outer_circle)
    
    inner_circle = patches.Circle((0, 0), 1.2, linewidth=2, 
                                edgecolor='blue', facecolor='lightblue', alpha=0.5)
    ax.add_patch(inner_circle)
    
    # Pressure distribution (arrows pointing outward from center)
    ax.arrow(0, 0, 0, 1.0, head_width=0.1, head_length=0.08, 
             fc='red', ec='red', linewidth=4)
    ax.text(0.2, 0.8, r'$p_i$', fontsize=14, color='red', fontweight='bold')
    
    # Wall stress (arrows around circumference)
    angles = np.linspace(0, 2*np.pi, 12, endpoint=False)
    for i, angle in enumerate(angles):
        if i % 3 == 0:  # Show every third arrow for clarity
            x_pos = 1.35 * np.cos(angle)
            y_pos = 1.35 * np.sin(angle)
            dx = -0.2 * np.cos(angle)
            dy = -0.2 * np.sin(angle)
            ax.arrow(x_pos, y_pos, dx, dy, head_width=0.05, 
                    head_length=0.04, fc='green', ec='green')
    
    # Dimensions
    ax.plot([0, 1.2], [0, 0], 'k--', linewidth=1)
    ax.text(0.6, -0.1, 'r', ha='center', fontsize=12, fontweight='bold')
    
    ax.plot([1.2, 1.5], [0.3, 0.3], 'k-', linewidth=3)
    ax.text(1.35, 0.4, 't', ha='center', fontsize=12, fontweight='bold')
    
    # === FORCE CALCULATIONS ===
    
    # Text box with calculations
    calc_text = (
        "Force Analysis:\n\n"
        "1. Pressure Force (acting on circular area):\n"
        r"   $F_{pressure} = p_i \times \pi r^2$" + "\n\n"
        "2. Axial Stress Force (acting on wall area):\n"
        r"   $A_{wall} = \pi(r+t)^2 - \pi r^2 \approx 2\pi rt$" + "\n"
        r"   $F_{axial} = \sigma_z \times 2\pi rt$" + "\n\n"
        "3. Equilibrium Condition:\n"
        r"   $F_{axial} = F_{pressure}$" + "\n"
        r"   $\sigma_z \times 2\pi rt = p_i \times \pi r^2$" + "\n\n"
        "4. Solving for axial stress:\n"
        r"   $\sigma_z = \frac{p_i r}{2t}$"
    )
    
    ax.text(2.2, 1, calc_text, fontsize=11, 
            bbox=dict(boxstyle="round,pad=0.5", facecolor="lightyellow", alpha=0.9),
            verticalalignment='top')
    
    # === RESULT BOX ===
    result_text = (
        "Result:\n"
        r"$\sigma_z = \frac{rp}{2t}$" + "\n\n"
        "Compare with hoop stress:\n"
        r"$\sigma_\theta = \frac{rp}{t} = 2\sigma_z$"
    )
    
    ax.text(2.2, -1.5, result_text, fontsize=12, fontweight='bold',
            bbox=dict(boxstyle="round,pad=0.5", facecolor="lightgreen", alpha=0.9),
            verticalalignment='top')
    
    # Labels and annotations
    ax.text(0, 1.8, 'Cross-section of Cylindrical Pressure Vessel', 
            ha='center', fontsize=14, fontweight='bold')
    
    ax.text(-1.8, 1.0, 'Wall', ha='center', fontsize=12, 
            bbox=dict(boxstyle="round,pad=0.2", facecolor="lightgray"))
    
    ax.text(0, -0.3, 'Internal\nPressure', ha='center', fontsize=10, color='red')
    
    ax.text(-1.8, 0, 'Axial Stress\n' + r'$\sigma_z$', ha='center', fontsize=10, 
            color='green', bbox=dict(boxstyle="round,pad=0.2", facecolor="lightgreen"))
    
    ax.grid(True, alpha=0.3)
    ax.set_xticks([])
    ax.set_yticks([])
    
    plt.tight_layout()
    return fig

def main():
    """Main function to create and save the diagrams"""
    
    print("Creating free body diagrams for Exercise 3.1.3c...")
    
    # Create the main free body diagram
    fig1 = create_free_body_diagram()
    
    # Create the detailed force analysis
    fig2 = create_force_analysis_diagram()
    
    # Save the figures
    fig1.savefig('/Users/jan-oivindlima/Documents/arbeid/skole/9. semester/TKT4150 - Biomekanikk/Øvinger/images/ex3.1.3c-free-body-diagram.png', 
                 dpi=300, bbox_inches='tight')
    
    fig2.savefig('/Users/jan-oivindlima/Documents/arbeid/skole/9. semester/TKT4150 - Biomekanikk/Øvinger/images/ex3.1.3c-force-analysis.png', 
                 dpi=300, bbox_inches='tight')
    
    print("✓ Free body diagram saved as: ex3.1.3c-free-body-diagram.png")
    print("✓ Force analysis diagram saved as: ex3.1.3c-force-analysis.png")
    
    # Show the plots
    plt.show()
    
    print("\nDiagram Features:")
    print("- Left panel: 3D view of cylinder showing cut plane")
    print("- Right panel: Free body diagram with force arrows")
    print("- Red arrows: Internal pressure forces")
    print("- Green arrows: Axial stress forces")
    print("- Mathematical derivation included")
    print("- Shows equilibrium condition leading to σz = rp/(2t)")

if __name__ == "__main__":
    main()
