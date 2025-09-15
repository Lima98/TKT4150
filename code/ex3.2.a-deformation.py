"""
Exercise 3, Task 2.a: Homogeneous Deformation Analysis
TKT4150 - Biomechanics

Analyzes homogeneous deformation: x1 = X1 + aX2, x2 = (1+a)X2 with a=0.1
Including visualization, stretch calculations, and strain analysis.
"""

import numpy as np
import matplotlib.pyplot as plt


def homogeneous_deformation_analysis():
    """
    Complete analysis of homogeneous deformation problem
    """
    print("="*70)
    print("EXERCISE 3, TASK 2.a: HOMOGENEOUS DEFORMATION ANALYSIS")
    print("="*70)
    
    # Given deformation parameters
    a = 0.1
    print(f"Given deformation parameter: a = {a}")
    print("Deformation mapping:")
    print("x₁ = X₁ + aX₂")
    print("x₂ = (1 + a)X₂")
    print()
    
    # Part 1: Original and deformed square
    print("PART 1: Square Deformation")
    print("-" * 40)
    
    # Original square corners
    original_corners = np.array([
        [0., 0.],  # A
        [1., 0.],  # B
        [1., 1.],  # C
        [0., 1.]   # D
    ])

    # Apply deformation mapping: x1 = X1 + a*X2, x2 = (1+a)*X2
    deformed_corners = np.zeros_like(original_corners)
    for i, (X1, X2) in enumerate(original_corners):
        x1 = X1 + a * X2
        x2 = (1 + a) * X2
        deformed_corners[i] = [x1, x2]
    
    corner_labels = ['A', 'B', 'C', 'D']
    print("Original → Deformed corners:")
    for i, label in enumerate(corner_labels):
        orig = original_corners[i]
        deform = deformed_corners[i]
        print(f"  {label}: ({orig[0]}, {orig[1]}) → "
              f"({deform[0]:.1f}, {deform[1]:.1f})")
    print()
    
    # Part 2: Stretch calculations
    print("PART 2: Stretch Calculations from Geometry")
    print("-" * 50)
    
    # Stretch along AC (diagonal)
    A_orig, C_orig = original_corners[0], original_corners[2]
    A_def, C_def = deformed_corners[0], deformed_corners[2]
    
    AC_orig_length = np.linalg.norm(C_orig - A_orig)
    AC_def_length = np.linalg.norm(C_def - A_def)
    stretch_AC = AC_def_length / AC_orig_length
    
    print("Stretch along AC:")
    print(f"  Original length: {AC_orig_length:.3f}")
    print(f"  Deformed length: {AC_def_length:.3f}")
    print(f"  Stretch ratio λ_AC = {stretch_AC:.3f}")
    print()
    
    # Stretch along BD (diagonal)
    B_orig, D_orig = original_corners[1], original_corners[3]
    B_def, D_def = deformed_corners[1], deformed_corners[3]
    
    BD_orig_length = np.linalg.norm(D_orig - B_orig)
    BD_def_length = np.linalg.norm(D_def - B_def)
    stretch_BD = BD_def_length / BD_orig_length
    
    print("Stretch along BD:")
    print(f"  Original length: {BD_orig_length:.3f}")
    print(f"  Deformed length: {BD_def_length:.3f}")
    print(f"  Stretch ratio λ_BD = {stretch_BD:.3f}")
    print()
    
    # Part 3: Shear strain calculation
    print("PART 3: Shear Strain Calculation")
    print("-" * 40)
    
    # Deformed basis vectors
    e1_def = np.array([1, 0])  # e1 unchanged
    e2_def = np.array([a, 1 + a])  # e2 becomes (a, 1+a)
    
    # Calculate angle between deformed vectors
    cos_alpha = (np.dot(e1_def, e2_def) /
                 (np.linalg.norm(e1_def) * np.linalg.norm(e2_def)))
    alpha = np.arccos(cos_alpha)
    gamma = np.pi/2 - alpha

    print(f"Original angle between e₁ and e₂: π/2 = {np.pi/2:.3f} rad")
    print(f"Deformed angle α: {alpha:.3f} rad")
    print(f"Shear strain γ = π/2 - α = {gamma:.3f} rad "
          f"({np.degrees(gamma):.1f}°)")
    print()

    # Part 4: Deformation gradient and Green strain
    print("PART 4: Deformation Gradient F and Green Strain E")
    print("-" * 55)

    # Deformation gradient tensor
    F = np.array([
        [1, a],
        [0, 1 + a]
    ])

    print("Deformation gradient tensor F:")
    print(F)
    print()

    # Green-Lagrange strain tensor
    identity = np.eye(2)
    E = 0.5 * (F.T @ F - identity)
    
    print("Green-Lagrange strain tensor E:")
    print(E)
    print()
    
    # Part 5: Stretch ratio for arbitrary direction
    print("PART 5: Stretch Ratio for Arbitrary Direction")
    print("-" * 50)
    
    def stretch_ratio(theta):
        """Calculate stretch ratio for direction at angle theta"""
        n0 = np.array([np.cos(theta), np.sin(theta)])
        n = F @ n0
        return np.linalg.norm(n) / np.linalg.norm(n0)
    
    def longitudinal_strain_green(theta):
        """Calculate longitudinal strain using Green tensor"""
        n0 = np.array([np.cos(theta), np.sin(theta)])
        return n0.T @ E @ n0
    
    # Test for specific angles
    test_angles = [0, np.pi/4, np.pi/2, 3*np.pi/4]
    angle_names = ['0°', '45°', '90°', '135°']
    
    print("Stretch ratios for test directions:")
    for angle, name in zip(test_angles, angle_names):
        lambda_val = stretch_ratio(angle)
        epsilon_direct = lambda_val - 1
        epsilon_green = longitudinal_strain_green(angle)
        print(f"  θ = {name}: λ = {lambda_val:.3f}, "
              f"ε_dir = {epsilon_direct:.3f}, ε_Green = {epsilon_green:.3f}")
    print()

    # Part 6: Find maximum and minimum stretch directions
    print("PART 6: Maximum and Minimum Stretch Directions")
    print("-" * 50)

    # Calculate stretch for many angles
    theta_range = np.linspace(0, 2*np.pi, 1000)
    stretch_values = [stretch_ratio(theta) for theta in theta_range]

    # Find extrema
    max_idx = np.argmax(stretch_values)
    min_idx = np.argmin(stretch_values)

    theta_max = theta_range[max_idx]
    theta_min = theta_range[min_idx]
    lambda_max = stretch_values[max_idx]
    lambda_min = stretch_values[min_idx]

    print("Maximum stretch:")
    print(f"  Direction: θ = {theta_max:.3f} rad "
          f"({np.degrees(theta_max):.1f}°)")
    print(f"  Stretch ratio: λ_max = {lambda_max:.3f}")
    print()

    print("Minimum stretch:")
    print(f"  Direction: θ = {theta_min:.3f} rad "
          f"({np.degrees(theta_min):.1f}°)")
    print(f"  Stretch ratio: λ_min = {lambda_min:.3f}")
    print()
    
    # Part 7: Principal strain analysis
    print("PART 7: Principal Strain Analysis")
    print("-" * 40)
    
    # Calculate eigenvalues and eigenvectors of E
    eigenvalues, eigenvectors = np.linalg.eigh(E)
    
    print("Principal strains (eigenvalues of E):")
    for i, eval in enumerate(eigenvalues):
        print(f"  E_{i+1} = {eval:.6f}")
    print()
    
    print("Principal strain directions (eigenvectors):")
    for i, evec in enumerate(eigenvectors.T):
        angle = np.arctan2(evec[1], evec[0])
        print(f"  Direction {i+1}: [{evec[0]:.3f}, {evec[1]:.3f}] "
              f"(θ = {np.degrees(angle):.1f}°)")
    print()
    
    # Relationship between principal strains and stretches
    print("Relationship between principal strains and stretches:")
    principal_stretches = np.sqrt(2 * eigenvalues + 1)
    for i, (strain, stretch) in enumerate(
            zip(eigenvalues, principal_stretches)):
        print(f"  E_{i+1} = {strain:.6f} → λ_{i+1} = "
              f"√(2E_{i+1} + 1) = {stretch:.3f}")
    print()

    # Visualization
    create_visualization(original_corners, deformed_corners, corner_labels,
                         theta_range, stretch_values, F, E, a)
    
    return {
        'deformation_parameter': a,
        'deformation_gradient': F,
        'green_strain': E,
        'stretch_AC': stretch_AC,
        'stretch_BD': stretch_BD,
        'shear_strain': gamma,
        'max_stretch': lambda_max,
        'min_stretch': lambda_min,
        'principal_strains': eigenvalues,
        'principal_directions': eigenvectors
    }


def create_visualization(original_corners, deformed_corners, corner_labels, 
                        theta_range, stretch_values, F, E, a):
    """Create comprehensive visualization of the deformation analysis"""
    
    fig = plt.figure(figsize=(16, 12))
    
    # Plot 1: Original vs Deformed square
    ax1 = fig.add_subplot(2, 3, 1)
    
    # Close the polygons
    orig_closed = np.vstack([original_corners, original_corners[0]])
    def_closed = np.vstack([deformed_corners, deformed_corners[0]])
    
    ax1.plot(orig_closed[:, 0], orig_closed[:, 1], 'b-', linewidth=2, 
             label='Original square')
    ax1.plot(def_closed[:, 0], def_closed[:, 1], 'r-', linewidth=2, 
             label='Deformed square')
    
    # Add corner labels
    for i, label in enumerate(corner_labels):
        ax1.plot(original_corners[i, 0], original_corners[i, 1], 'bo', markersize=8)
        ax1.plot(deformed_corners[i, 0], deformed_corners[i, 1], 'ro', markersize=8)
        ax1.text(original_corners[i, 0] - 0.1, original_corners[i, 1] - 0.1, 
                label, fontsize=12, color='blue')
        ax1.text(deformed_corners[i, 0] + 0.05, deformed_corners[i, 1] + 0.05, 
                label + "'", fontsize=12, color='red')
    
    ax1.set_xlim(-0.3, 1.3)
    ax1.set_ylim(-0.3, 1.3)
    ax1.set_aspect('equal')
    ax1.grid(True, alpha=0.3)
    ax1.legend()
    ax1.set_title('Square Deformation')
    ax1.set_xlabel('x₁')
    ax1.set_ylabel('x₂')
    
    # Plot 2: Stretch ratio vs direction
    ax2 = fig.add_subplot(2, 3, 2)
    ax2.plot(np.degrees(theta_range), stretch_values, 'g-', linewidth=2)
    ax2.axhline(y=1, color='k', linestyle='--', alpha=0.5, label='No stretch')
    ax2.set_xlabel('Direction θ (degrees)')
    ax2.set_ylabel('Stretch ratio λ')
    ax2.set_title('Stretch Ratio vs Direction')
    ax2.grid(True, alpha=0.3)
    ax2.legend()
    
    # Plot 3: Deformation gradient tensor heatmap
    ax3 = fig.add_subplot(2, 3, 3)
    im1 = ax3.imshow(F, cmap='RdBu_r', aspect='equal')
    ax3.set_title('Deformation Gradient F')
    ax3.set_xlabel('Column')
    ax3.set_ylabel('Row')
    
    # Add text annotations for F
    for i in range(2):
        for j in range(2):
            ax3.text(j, i, f'{F[i, j]:.2f}', ha="center", va="center", 
                    color="black", fontweight="bold", fontsize=14)
    
    plt.colorbar(im1, ax=ax3, fraction=0.046, pad=0.04)
    
    # Plot 4: Green strain tensor heatmap
    ax4 = fig.add_subplot(2, 3, 4)
    im2 = ax4.imshow(E, cmap='RdBu_r', aspect='equal')
    ax4.set_title('Green Strain Tensor E')
    ax4.set_xlabel('Column')
    ax4.set_ylabel('Row')
    
    # Add text annotations for E
    for i in range(2):
        for j in range(2):
            ax4.text(j, i, f'{E[i, j]:.3f}', ha="center", va="center", 
                    color="black", fontweight="bold", fontsize=12)
    
    plt.colorbar(im2, ax=ax4, fraction=0.046, pad=0.04)
    
    # Plot 5: Principal directions visualization
    ax5 = fig.add_subplot(2, 3, 5)
    
    # Calculate principal directions
    eigenvalues, eigenvectors = np.linalg.eigh(E)
    
    # Plot deformed square
    def_closed = np.vstack([deformed_corners, deformed_corners[0]])
    ax5.plot(def_closed[:, 0], def_closed[:, 1], 'r-', linewidth=2, 
             alpha=0.7, label='Deformed square')
    
    # Plot principal directions as arrows from center
    center = np.mean(deformed_corners, axis=0)
    colors = ['purple', 'orange']
    
    for i, (eigval, eigvec) in enumerate(zip(eigenvalues, eigenvectors.T)):
        # Scale arrow by eigenvalue magnitude
        arrow_scale = 0.3 * (1 + eigval * 5)
        arrow_end = center + arrow_scale * eigvec
        
        ax5.annotate('', xy=arrow_end, xytext=center,
                    arrowprops=dict(arrowstyle='->', color=colors[i], 
                                  linewidth=3))
        ax5.text(arrow_end[0] + 0.05, arrow_end[1] + 0.05, 
                f'E{i+1}={eigval:.3f}', color=colors[i], fontweight='bold')
    
    ax5.plot(center[0], center[1], 'ko', markersize=8)
    ax5.set_xlim(-0.1, 1.3)
    ax5.set_ylim(-0.1, 1.3)
    ax5.set_aspect('equal')
    ax5.grid(True, alpha=0.3)
    ax5.set_title('Principal Strain Directions')
    ax5.set_xlabel('x₁')
    ax5.set_ylabel('x₂')
    
    # Plot 6: Stretch vs angle (polar plot)
    ax6 = fig.add_subplot(2, 3, 6, projection='polar')
    ax6.plot(theta_range, stretch_values, 'b-', linewidth=2)
    ax6.set_title('Stretch Ratio (Polar Plot)')
    ax6.set_ylim(0, max(stretch_values) * 1.1)
    
    plt.tight_layout()
    plt.savefig('/Users/jan-oivindlima/Documents/arbeid/skole/9. semester/'
                'TKT4150 - Biomekanikk/Øvinger/images/ex3.2.a-deformation.png',
                dpi=300, bbox_inches='tight')
    plt.show()


if __name__ == "__main__":
    results = homogeneous_deformation_analysis()
