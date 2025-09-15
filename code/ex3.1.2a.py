"""
TKT4150 Biomechanics - Exercise 3, Task 1.2.a)
Deformation Measures Analysis

This script analyzes deformation measures including:
- Strain tensor calculation
- Principal strains
- Engineering strains
- Strain invariants

Author: Generated for TKT4150 course
"""

import numpy as np
import matplotlib.pyplot as plt


def displacement_gradient_to_strain(displacement_gradient):
    """
    Convert displacement gradient tensor to strain tensor
    
    For small deformations: ε = 0.5 * (∇u + (∇u)^T)
    
    Parameters:
    displacement_gradient: 3x3 numpy array - gradient tensor ∇u
    
    Returns:
    strain_tensor: 3x3 numpy array - strain tensor
    """
    # Small strain assumption (most biomechanics applications)
    grad_u = np.array(displacement_gradient)
    strain_tensor = 0.5 * (grad_u + grad_u.T)
    return strain_tensor


def analyze_strain_tensor(strain_tensor):
    """
    Comprehensive analysis of strain tensor
    
    Parameters:
    strain_tensor: 3x3 numpy array
    
    Returns:
    Dictionary with strain analysis results
    """
    # Calculate principal strains and directions
    eigenvalues, eigenvectors = np.linalg.eigh(strain_tensor)
    
    # Sort by magnitude (largest first)
    idx = np.argsort(eigenvalues)[::-1]
    principal_strains = eigenvalues[idx]
    principal_directions = eigenvectors[:, idx]
    
    # Strain invariants
    I1 = np.trace(strain_tensor)  # First invariant
    I2 = 0.5 * (I1**2 - np.trace(strain_tensor @ strain_tensor))  # Second invariant
    I3 = np.linalg.det(strain_tensor)  # Third invariant
    
    # Volumetric and deviatoric components
    volumetric_strain = I1 / 3
    deviatoric_strain = strain_tensor - volumetric_strain * np.eye(3)
    
    # Engineering strains (normal strains)
    engineering_strains = np.diag(strain_tensor)
    
    # Shear strains (engineering definition: γ = 2ε)
    shear_strains = 2 * np.array([strain_tensor[0,1], strain_tensor[1,2], strain_tensor[0,2]])
    
    # Maximum shear strain
    max_shear_strain = 0.5 * (principal_strains[0] - principal_strains[2])
    
    return {
        'strain_tensor': strain_tensor,
        'principal_strains': principal_strains,
        'principal_directions': principal_directions,
        'invariants': {'I1': I1, 'I2': I2, 'I3': I3},
        'volumetric_strain': volumetric_strain,
        'deviatoric_strain': deviatoric_strain,
        'engineering_strains': engineering_strains,
        'shear_strains': shear_strains,
        'max_shear_strain': max_shear_strain
    }

def plot_strain_analysis(strain_results):
    """
    Create visualization of strain analysis
    """
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    
    # 1. Principal strains bar plot
    ax1 = axes[0, 0]
    principal_strains = strain_results['principal_strains']
    colors = ['red', 'blue', 'green']
    bars = ax1.bar(['ε₁', 'ε₂', 'ε₃'], principal_strains, 
                   color=colors, alpha=0.7)
    ax1.set_title('Principal Strains')
    ax1.set_ylabel('Strain')
    ax1.axhline(y=0, color='black', linestyle='--', alpha=0.5)
    ax1.grid(True, alpha=0.3)
    
    # Add value labels on bars
    for bar, value in zip(bars, principal_strains):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{value:.6f}', ha='center', 
                va='bottom' if height >= 0 else 'top')
    
    # 2. Engineering strains
    ax2 = axes[0, 1]
    eng_strains = strain_results['engineering_strains']
    shear_strains = strain_results['shear_strains']
    
    x_pos = np.arange(len(eng_strains))
    bars1 = ax2.bar(x_pos - 0.2, eng_strains, 0.4, 
                     label='Normal strains', alpha=0.7)
    bars2 = ax2.bar(x_pos + 0.2, shear_strains, 0.4, 
                     label='Shear strains', alpha=0.7)
    
    ax2.set_title('Engineering Strains')
    ax2.set_xlabel('Strain Component')
    ax2.set_ylabel('Strain')
    ax2.set_xticks(x_pos)
    ax2.set_xticklabels(['εₓₓ/γₓᵧ', 'εᵧᵧ/γᵧz', 'εzz/γₓz'])
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # 3. Strain tensor visualization
    ax3 = axes[1, 0]
    im = ax3.imshow(strain_results['strain_tensor'], cmap='RdBu_r')
    ax3.set_title('Strain Tensor ε')
    ax3.set_xlabel('Column index')
    ax3.set_ylabel('Row index')
    
    # Add text annotations
    for i in range(3):
        for j in range(3):
            text = ax3.text(j, i, f'{strain_results["strain_tensor"][i, j]:.6f}',
                           ha="center", va="center", color="black")
    
    plt.colorbar(im, ax=ax3)
    
    # 4. Volumetric vs Deviatoric strain
    ax4 = axes[1, 1]
    vol_strain = strain_results['volumetric_strain']
    dev_strain_norm = np.linalg.norm(strain_results['deviatoric_strain'])
    
    ax4.bar(['Volumetric\nStrain', 'Deviatoric\nStrain\n(norm)'], 
            [vol_strain, dev_strain_norm], 
            color=['orange', 'purple'], alpha=0.7)
    ax4.set_title('Strain Decomposition')
    ax4.set_ylabel('Strain Magnitude')
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    return fig

def main():
    """
    Main analysis function for deformation measures
    """
    print("TKT4150 Biomechanics - Exercise 3, Task 1.2.a)")
    print("=" * 50)
    print("Deformation Measures Analysis")
    print()
    
    # Example displacement gradient (this would typically come from experimental data or FEA)
    # For demonstration, using a realistic biomechanical strain state
    print("1. Displacement Gradient Tensor")
    print("-" * 30)
    
    # Example: Bone under combined loading
    displacement_gradient = np.array([
        [0.001, 0.0005, 0.0002],   # ∂u₁/∂x₁, ∂u₁/∂x₂, ∂u₁/∂x₃
        [0.0003, -0.0008, 0.0001], # ∂u₂/∂x₁, ∂u₂/∂x₂, ∂u₂/∂x₃
        [0.0001, 0.0002, 0.0005]   # ∂u₃/∂x₁, ∂u₃/∂x₂, ∂u₃/∂x₃
    ])
    
    print("∇u =")
    print(displacement_gradient)
    print()
    
    # Calculate strain tensor
    print("2. Strain Tensor Calculation")
    print("-" * 30)
    strain_tensor = displacement_gradient_to_strain(displacement_gradient)
    print("ε = 0.5 * (∇u + (∇u)ᵀ) =")
    print(strain_tensor)
    print()
    
    # Comprehensive strain analysis
    print("3. Strain Analysis Results")
    print("-" * 30)
    results = analyze_strain_tensor(strain_tensor)
    
    print(f"Principal Strains:")
    for i, strain in enumerate(results['principal_strains']):
        print(f"  ε₁ = {strain:.6f}")
    print()
    
    print("Principal Directions:")
    for i, direction in enumerate(results['principal_directions'].T):
        print(f"  n₁ = [{direction[0]:.4f}, {direction[1]:.4f}, {direction[2]:.4f}]")
    print()
    
    print("Strain Invariants:")
    print(f"  I₁ = {results['invariants']['I1']:.6f}")
    print(f"  I₂ = {results['invariants']['I2']:.6f}")
    print(f"  I₃ = {results['invariants']['I3']:.6f}")
    print()
    
    print(f"Volumetric Strain: {results['volumetric_strain']:.6f}")
    print(f"Maximum Shear Strain: {results['max_shear_strain']:.6f}")
    print()
    
    print("Engineering Strains:")
    print(f"  εₓₓ = {results['engineering_strains'][0]:.6f}")
    print(f"  εᵧᵧ = {results['engineering_strains'][1]:.6f}")
    print(f"  εzz = {results['engineering_strains'][2]:.6f}")
    print()
    
    print("Engineering Shear Strains:")
    print(f"  γₓᵧ = {results['shear_strains'][0]:.6f}")
    print(f"  γᵧz = {results['shear_strains'][1]:.6f}")
    print(f"  γₓz = {results['shear_strains'][2]:.6f}")
    print()
    
    # Physical interpretation
    print("4. Physical Interpretation")
    print("-" * 30)
    
    if results['volumetric_strain'] > 0:
        print("• Material experiences volumetric expansion")
    else:
        print("• Material experiences volumetric compression")
    
    if results['principal_strains'][0] > 0:
        print("• Maximum principal strain is tensile")
    else:
        print("• Maximum principal strain is compressive")
    
    if results['principal_strains'][2] < 0:
        print("• Minimum principal strain is compressive")
    else:
        print("• Minimum principal strain is tensile")
    
    strain_magnitude = np.linalg.norm(results['strain_tensor'])
    print(f"• Overall strain magnitude: {strain_magnitude:.6f}")
    
    # Create visualization
    fig = plot_strain_analysis(results)
    plt.show()
    
    # Save results
    print("\n5. Results Summary")
    print("-" * 30)
    print("Analysis complete. Key findings:")
    print(f"- Maximum tensile strain: {max(results['principal_strains']):.6f}")
    print(f"- Maximum compressive strain: {min(results['principal_strains']):.6f}")
    print(f"- Maximum shear strain: {results['max_shear_strain']:.6f}")
    print(f"- Volume change: {results['volumetric_strain']*100:.4f}%")

if __name__ == "__main__":
    main()
