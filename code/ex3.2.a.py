"""
Exercise 3, Task 2.a: Deformation Measures Analysis
TKT4150 - Biomechanics

Analyzes deformation measures including strain tensors, principal strains,
and strain invariants for a given displacement gradient tensor.
"""

import numpy as np
import matplotlib.pyplot as plt


def analyze_deformation_measures():
    """
    Comprehensive analysis of deformation measures from displacement
    gradient tensor
    """
    print("="*60)
    print("EXERCISE 3, TASK 2.a: DEFORMATION MEASURES ANALYSIS")
    print("="*60)

    # Given displacement gradient tensor H
    H = np.array([
        [0.02,  0.01,  0.005],
        [0.015, 0.03,  0.008],
        [0.003, 0.012, 0.025]
    ])

    print("Given displacement gradient tensor H:")
    print(H)
    print()

    # Step 1: Calculate Green-Lagrange strain tensor
    print("STEP 1: Green-Lagrange Strain Tensor")
    print("-" * 40)

    H_T = H.T
    print("H^T (transpose):")
    print(H_T)
    print()

    # Green-Lagrange strain: E = 1/2(H + H^T + H^T * H)
    E = 0.5 * (H + H_T + H_T @ H)

    print("Green-Lagrange strain tensor E:")
    print(E)
    print()

    # Step 2: Calculate Almansi strain tensor
    print("STEP 2: Almansi Strain Tensor")
    print("-" * 40)

    # Almansi strain: e = 1/2(H + H^T - H * H^T)
    e = 0.5 * (H + H_T - H @ H_T)

    print("Almansi strain tensor e:")
    print(e)
    print()

    # Step 3: Principal strain analysis (using Green-Lagrange tensor)
    print("STEP 3: Principal Strain Analysis")
    print("-" * 40)

    # Calculate eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eigh(E)

    # Sort eigenvalues and eigenvectors in descending order
    sorted_indices = np.argsort(eigenvalues)[::-1]
    principal_strains = eigenvalues[sorted_indices]
    principal_directions = eigenvectors[:, sorted_indices]

    print("Principal strains (sorted):")
    for i, strain in enumerate(principal_strains):
        print(f"  E_{i+1} = {strain:.6f} ({strain*100:.3f}%)")
    print()

    print("Principal strain directions:")
    for i, direction in enumerate(principal_directions.T):
        print(f"  v_{i+1} = [{direction[0]:.3f}, {direction[1]:.3f}, "
              f"{direction[2]:.3f}]")
    print()

    # Step 4: Strain invariants
    print("STEP 4: Strain Invariants")
    print("-" * 40)

    # First invariant (trace)
    I1 = np.trace(E)

    # Second invariant
    I2 = 0.5 * (I1**2 - np.trace(E @ E))

    # Third invariant (determinant)
    I3 = np.linalg.det(E)

    print(f"First invariant (I₁):  {I1:.6f}")
    print(f"Second invariant (I₂): {I2:.6f}")
    print(f"Third invariant (I₃):  {I3:.8f}")
    print()

    # Step 5: Engineering strains and additional measures
    print("STEP 5: Engineering Strains and Additional Measures")
    print("-" * 50)

    # Normal strains (diagonal elements of E)
    epsilon_x = E[0, 0]
    epsilon_y = E[1, 1]
    epsilon_z = E[2, 2]

    print(f"Normal strain εₓ: {epsilon_x:.6f} ({epsilon_x*100:.3f}%)")
    print(f"Normal strain εᵧ: {epsilon_y:.6f} ({epsilon_y*100:.3f}%)")
    print(f"Normal strain εᵧ: {epsilon_z:.6f} ({epsilon_z*100:.3f}%)")
    print()

    # Shear strains (off-diagonal elements)
    gamma_xy = 2 * E[0, 1]
    gamma_yz = 2 * E[1, 2]
    gamma_xz = 2 * E[0, 2]

    print(f"Shear strain γₓᵧ: {gamma_xy:.6f}")
    print(f"Shear strain γᵧᵧ: {gamma_yz:.6f}")
    print(f"Shear strain γₓᵧ: {gamma_xz:.6f}")
    print()

    # Maximum shear strain
    gamma_max = principal_strains[0] - principal_strains[2]
    print(f"Maximum shear strain γₘₐₓ: {gamma_max:.6f} "
          f"({gamma_max*100:.3f}%)")
    print()

    # Step 6: Visualization
    print("STEP 6: Creating Visualization")
    print("-" * 40)

    # Create visualization
    fig = plt.figure(figsize=(15, 10))

    # 3D visualization of principal strain directions
    ax1 = fig.add_subplot(221, projection='3d')

    # Origin
    origin = np.array([0, 0, 0])

    # Plot principal strain directions as vectors
    colors = ['red', 'green', 'blue']
    labels = ['E₁ (max)', 'E₂ (intermediate)', 'E₃ (min)']

    for i, (direction, strain, color, label) in enumerate(
            zip(principal_directions.T, principal_strains, colors, labels)):
        # Scale vectors by strain magnitude for visualization
        scaled_direction = direction * strain * 20  # Scale factor
        ax1.quiver(origin[0], origin[1], origin[2],
                   scaled_direction[0], scaled_direction[1],
                   scaled_direction[2], color=color, arrow_length_ratio=0.1,
                   linewidth=3, label=label)

    ax1.set_xlabel('X')
    ax1.set_ylabel('Y')
    ax1.set_zlabel('Z')
    ax1.set_title('Principal Strain Directions')
    ax1.legend()
    ax1.set_xlim([-0.001, 0.001])
    ax1.set_ylim([-0.001, 0.001])
    ax1.set_zlim([-0.001, 0.001])

    # Principal strains bar chart
    ax2 = fig.add_subplot(222)
    strain_labels = ['E₁', 'E₂', 'E₃']
    strain_values = principal_strains * 100  # Convert to percentage
    bars = ax2.bar(strain_labels, strain_values,
                   color=['red', 'green', 'blue'], alpha=0.7)
    ax2.set_ylabel('Principal Strain (%)')
    ax2.set_title('Principal Strains')
    ax2.grid(True, alpha=0.3)

    # Add value labels on bars
    for bar, value in zip(bars, strain_values):
        height = bar.get_height()
        ax2.text(bar.get_x() + bar.get_width()/2., height + 0.001,
                 f'{value:.3f}%', ha='center', va='bottom')

    # Strain tensor heatmap (Green-Lagrange)
    ax3 = fig.add_subplot(223)
    im = ax3.imshow(E, cmap='RdBu_r', aspect='equal')
    ax3.set_title('Green-Lagrange Strain Tensor E')
    ax3.set_xlabel('Column Index')
    ax3.set_ylabel('Row Index')

    # Add text annotations
    for i in range(3):
        for j in range(3):
            ax3.text(j, i, f'{E[i, j]:.4f}',
                     ha="center", va="center", color="black",
                     fontweight="bold")

    plt.colorbar(im, ax=ax3, fraction=0.046, pad=0.04)

    # Strain invariants
    ax4 = fig.add_subplot(224)
    invariant_labels = ['I₁', 'I₂', 'I₃']
    invariant_values = [I1, I2, I3]
    bars = ax4.bar(invariant_labels, invariant_values,
                   color=['orange', 'purple', 'brown'], alpha=0.7)
    ax4.set_ylabel('Invariant Value')
    ax4.set_title('Strain Invariants')
    ax4.grid(True, alpha=0.3)
    ax4.set_yscale('log')  # Log scale due to different orders of magnitude

    # Add value labels on bars
    for bar, value in zip(bars, invariant_values):
        height = bar.get_height()
        ax4.text(bar.get_x() + bar.get_width()/2., height * 1.1,
                 f'{value:.2e}', ha='center', va='bottom', rotation=45)

    plt.tight_layout()
    plt.savefig('/Users/jan-oivindlima/Documents/arbeid/skole/9. semester/'
                'TKT4150 - Biomekanikk/Øvinger/images/ex3.2.a-analysis.png',
                dpi=300, bbox_inches='tight')
    plt.show()

    # Summary
    print("SUMMARY")
    print("="*60)
    print(f"Maximum principal strain: {principal_strains[0]*100:.3f}%")
    print(f"Minimum principal strain: {principal_strains[2]*100:.3f}%")
    print(f"Maximum shear strain: {gamma_max*100:.3f}%")
    print(f"Volumetric strain (first invariant): {I1*100:.3f}%")
    print()
    print("Physical interpretation:")
    print("- All principal strains are positive → tensile deformation")
    print("- Largest deformation occurs along E₁ direction")
    print("- Material experiences moderate strains suitable for "
          "biomechanical analysis")
    print("="*60)

    return {
        'displacement_gradient': H,
        'green_lagrange_strain': E,
        'almansi_strain': e,
        'principal_strains': principal_strains,
        'principal_directions': principal_directions,
        'strain_invariants': [I1, I2, I3],
        'engineering_strains': {
            'normal': [epsilon_x, epsilon_y, epsilon_z],
            'shear': [gamma_xy, gamma_yz, gamma_xz],
            'max_shear': gamma_max
        }
    }


if __name__ == "__main__":
    results = analyze_deformation_measures()
