#import "@preview/dvdtyp:1.0.1": *

#show: dvdtyp.with(
  title: "Exercise 3",
  subtitle: [TKT4150 - Biomechanics],
  author: "Jan-Øivind Lima",
  accent: highlight,
)

#show link: underline
#show link: set text(fill: highlight)

#set math.mat(delim: "[")
#set math.equation(numbering: "(1)")

#outline(depth: none)

= Assignment 3
== Exercise 1: Principal and equivalent stress in femur bone of running human
The running human from the previous exercise is investigated further. The mechanics of the femur (the thigh bone)are in thes potlight this time. Fracture stress and density of bone are both given in Figure1. Experiments reveal that point P has the largest stress and that the yield strength of the femur is $σ_(max) = 130 "MPa"$. Preliminary calculations and experiments suggest the following stress in point P:

$ T = mat(-50,35, 0; 35, -70,0;0,0,0) $

#figure(
image("images/running2.png", width: 60%),
caption: "Running human.",
)

=== Principal stresses 

Given the stress tensor at point P:
$ T = mat(-50,35, 0; 35, -70,0;0,0,0) space "MPa" $

This is a 2D plane stress problem since $sigma_33 = 0$. We extract the 2D stress matrix:
$ T_(2D) = mat(-50, 35; 35, -70) space "MPa" $

*Principal Stress Calculation:*

Using eigenvalue analysis, the characteristic equation is:
$ det(T_(2D) - sigma I) = 0 $
$ det mat(-50-sigma, 35; 35, -70-sigma) = 0 $
$ (50+sigma)(70+sigma) - 35^2 = 0 $
$ sigma^2 + 120sigma + 2275 = 0 $

Solving this quadratic equation:
$ sigma_(1,2) = (-120 ± sqrt(120^2 - 4·2275))/2 = (-120 ± sqrt(5300})/2 $

*Principal Stresses:*
- $sigma_1 = -23.60$ MPa (least compressive)
- $sigma_2 = -96.40$ MPa (most compressive) 
- $sigma_3 = 0.00$ MPa (plane stress condition)

*Principal Directions:*

The principal directions make the following angles with the $x_1$-axis:
- Direction 1 (for $sigma_1$): $37.03°$
- Direction 2 (for $sigma_2$): $127.03°$ (or $37.03° + 90°$)
- Direction 3 (for $sigma_3$): along $x_3$-axis

*Maximum Shear Stress:*
$ tau_(max) = (sigma_1 - sigma_2)/2 = (-23.60 - (-96.40))/2 = 36.40 space "MPa" $

The analysis shows that the femur bone at point P experiences:
- Maximum compressive stress of 96.4 MPa
- The stress state is entirely compressive in the plane (both principal stresses are negative)
- Maximum shear stress of 36.4 MPa occurs at 45° to the principal directions

#figure(
image("images/ex3.1.1a-analysis.png", width: 60%),
caption: "Principal stress analysis for femur bone at point P. Top left: original stress state, top right: principal directions with angles, bottom left: Mohr's circle, bottom right: summary.",
)

#figure(
image("images/ex3.1.1a-3d.png", width: 50%),
caption: "3D visualization of principal stress directions relative to the coordinate system.",
)

The computational analysis was performed using Python (`ex3.1.1a.py`) and verified using both eigenvalue decomposition and analytical formulas for 2D principal stress analysis.

=== Stress lead to fracture?

The von Mises equivalent stress is calculated using:

$ sigma_"eq" = sqrt((sigma_1 - sigma_2)^2 + (sigma_2 - sigma_3)^2 + (sigma_3 - sigma_1)^2)/sqrt(2) $

Substituting our principal stresses (σ₁ = -23.60 MPa, σ₂ = -96.40 MPa, σ₃ = 0):

$ sigma_"eq" = sqrt((-23.60-(-96.40))^2 + (-96.40-0)^2 + (0-(-23.60))^2)/sqrt(2) $

$ sigma_"eq" = sqrt(72.80^2 + 96.40^2 + 23.60^2)/sqrt(2) = sqrt(15149.76)/sqrt(2) = 87.15 "MPa" $

*Result:* $σ_"eq" = 87.15 "MPa" < 130 "MPa"$ The given stress matrix does not lead to fracture in the feamur.

== Exercise 2: Deformation measures

=== Homogeneous deformation analysis

Consider the homogeneous deformation:
$ x_1 = X_1 + a X_2 $
$ x_2 = (1 + a) X_2 $
where $a = 0.1$.

#text(fill: blue, weight: "bold")[*Part 1: Visualization of square deformation*]

The square with corners A = (0,0), B = (1,0), C = (1,1), D = (0,1) deforms as follows:

*Original square corners:*
- A = (0, 0) → A' = (0.0, 0.0)
- B = (1, 0) → B' = (1.0, 0.0)  
- C = (1, 1) → C' = (1.1, 1.1)
- D = (0, 1) → D' = (0.1, 1.1)

The square becomes a parallelogram with shear deformation.

#figure(
image("images/deformation.png", width: 40%),
caption: "Deformation of square ABCD to A'B'C'D' under the given mapping with a=0.1.",
)

#text(fill: blue, weight: "bold")[*Part 2: Stretch calculations from geometry*]

*Stretch along AC (diagonal):*
- Original |AC| = √(1² + 1²) = √2 = 1.414
- Deformed |A'C'| = √(1.1² + 1.1²) = √2.42 = 1.556
- Stretch ratio: λ_AC = 1.556/1.414 = 1.100

*Stretch along BD (diagonal):*
- Original |BD| = √(1² + 1²) = √2 = 1.414
- Deformed |B'D'|: from (1,0) to (0.1, 1.1)
- |B'D'| = √((0.1-1)² + (1.1-0)²) = √(0.81 + 1.21) = √2.02 = 1.421
- Stretch ratio: λ_BD = 1.421/1.414 = 1.005

#text(fill: blue, weight: "bold")[*Part 3: Shear strain calculation*]

The shear strain γ between $bold(e)₁$ and $bold(e)₂$:
- Original angle between $bold(e)₁$ and $bold(e)₂$: π/2
- After deformation, $bold(e)₁$ remains (1,0), $bold(e)₂$ becomes (0.1, 1.1)
- New angle α: $cos α = (e_1 · e_2')/(|e_1||e_2'|) = 0.1/(1 × sqrt(0.1^2 + 1.1^2)) = 0.1/sqrt(1.22) = 0.0905$
- $α = arccos(0.0905) ≈ 1.480$ rad
- Shear strain: $γ = π/2 - α ≈ 1.571 - 1.480 = 0.091$ rad = 5.2°

#text(fill: blue, weight: "bold")[*Part 4: Deformation gradient F and Green strain E*]

*Deformation gradient tensor F:*
From the deformation mapping:
$ F = mat(∂x_1/∂X_1, ∂x_1/∂X_2; ∂x_2/∂X_1, ∂x_2/∂X_2) = mat(1, a; 0, 1+a) = mat(1, 0.1; 0, 1.1) $

*Green-Lagrange strain tensor E:*
$ E = 1/2(F^T F - I) $

$ F^T = mat(1, 0; 0.1, 1.1) $

$ F^T F = mat(1, 0; 0.1, 1.1) mat(1, 0.1; 0, 1.1) = mat(1, 0.11; 0.1, 1.21) $

$ E = 1/2(mat(1, 0.11; 0.1, 1.21) - mat(1, 0; 0, 1)) = mat(0, 0.055; 0.05, 0.105) $

#text(fill: blue, weight: "bold")[*Part 5: Stretch ratio for arbitrary direction*]

For direction $n_0 = cos θ e_1 + sin θ e_2$:
- Deformed vector: $n = F n_0 = mat(1, 0.1; 0, 1.1) mat(cos θ; sin θ) = mat(cos θ + 0.1 sin θ; 1.1 sin θ)$
- $|n_0| = 1$
- $|n| = sqrt((cos θ + 0.1 sin θ)^2 + (1.1 sin θ)^2)$
- $λ(θ) = sqrt(cos^2 θ + 0.2 cos θ sin θ + 0.01 sin^2 θ + 1.21 sin^2 θ)$
- $λ(θ) = sqrt(cos^2 θ + 0.2 cos θ sin θ + 1.22 sin^2 θ)$

*Longitudinal strain:* $ε = λ - 1$

For comparison with Green strain tensor:
$ε = n_0^T E n_0 = mat(cos θ, sin θ) mat(0, 0.055; 0.05, 0.11) mat(cos θ; sin θ)$
$ε = 0.055 cos θ sin θ + 0.05 cos θ sin θ + 0.11 sin^2 θ = 0.105 cos θ sin θ + 0.11 sin^2 θ$

#text(fill: blue, weight: "bold")[*Part 6: Maximum and minimum stretch directions*]

To find extrema, differentiate λ²(θ):
$ (λ^2)' = -2 cos θ sin θ + 0.2(cos^2 θ - sin^2 θ) + 2.44 sin θ cos θ = 0 $
$ 2.42 cos θ sin θ + 0.2 cos 2θ = 0 $
$ 1.21 sin 2θ + 0.2 cos 2θ = 0 $
$ tan 2θ = -0.2/1.21 = -0.165 $

Solutions:
- $2θ_1 = arctan(-0.165) ≈ -0.164$ rad → $θ_1 ≈ -0.082$ rad
- $2θ_2 = π + arctan(-0.165) ≈ 2.978$ rad → $θ_2 ≈ 1.489$ rad

*Maximum stretch:* $λ_"max" ≈ 1.122$ (at $θ ≈ 68.8°$ or 1.20 rad)
*Minimum stretch:* $λ_"min" ≈ 0.980$ (at $θ ≈ 158.9°$ or 2.77 rad)

*Principal strains from eigenvalues:*
- $E_1 = -0.01933$ (minimum principal strain)  
- $E_2 = 0.12933$ (maximum principal strain)

#text(fill: blue, weight: "bold")[*Part 7: Principal directions and verification*]

*Principal strains (eigenvalues of E):*
- $E_1 = -0.01933$ (minimum principal strain, compression)
- $E_2 = 0.12933$ (maximum principal strain, extension)

*Relationship to principal stretches:*
- $λ_1 = sqrt(2E_1 + 1) = sqrt(-0.03866 + 1) ≈ 0.980$
- $λ_2 = sqrt(2E_2 + 1) = sqrt(0.25866 + 1) ≈ 1.122$

*Verification:* These match our computed maximum/minimum stretches, confirming the principal strain analysis.

=== Longitudinal strain and stretch relationships

*Task:* Show that the longitudinal strain and the stretch in the line element aligned with the direction vector $bold(e)$ are, respectively:

$ ε = sqrt(1 + 2e_i E_(i j) e_j) - 1 $ (3)
$ λ = ε + 1 $ (4)

where longitudinal strain is defined as:
$ ε_l = (d s - d s_0) / d s_0 = d s / d s_0 - 1 $ (5)

and the stretch ratio λ is defined as:
$ λ = d s / d s_0 $ (6)

where $d s$ is the deformed length and $d s_0$ is the reference length of the material element.

*Derivation from continuum mechanics*

*Step 1: Consider a line element in the reference configuration*

Let $d bold(X)$ be an infinitesimal line element in the reference configuration with length:
$ d s_0 = |d bold(X)| = sqrt(d X_i d X_i) $

If this element is aligned with unit direction vector $bold(e)$, then:
$ d bold(X) = d s_0 bold(e) = d s_0 e_i bold(E)_i $

*Step 2: Deformed configuration*

In the deformed configuration, this element becomes $d bold(x)$ with length:
$ d s = |d bold(x)| = sqrt(d x_i d x_i) $

The relationship between deformed and reference configurations is:
$ d x_i = (∂x_i)/(∂X_j) d X_j = F_(i j) d X_j $

*Step 3: Length in deformed configuration*

For our line element aligned with $bold(e)$:
$ d x_i = F_(i j) d s_0 e_j $

The deformed length squared is:
$ (d s)^2 = d x_i d x_i = F_(i j) d s_0 e_j F_(i k) d s_0 e_k = (d s_0)^2 F_(i j) F_(i k) e_j e_k $

$ (d s)^2 = (d s_0)^2 (bold(F)^T bold(F))_(j k) e_j e_k $

*Step 4: Green strain tensor relationship*

The Green-Lagrange strain tensor is defined as:
$ bold(E) = 1/2 (bold(F)^T bold(F) - bold(I)) $

Therefore:
$ bold(F)^T bold(F) = 2 bold(E) + bold(I) $

Substituting:
$ (d s)^2 = (d s_0)^2 (2 E_(j k) + δ_(j k)) e_j e_k $
$ (d s)^2 = (d s_0)^2 (2 e_j E_(j k) e_k + e_j e_j) $

Since $bold(e)$ is a unit vector: $e_j e_j = 1$

$ (d s)^2 = (d s_0)^2 (1 + 2 e_j E_(j k) e_k) $

*Step 5: Stretch ratio*

The stretch ratio is:
$ λ = d s / d s_0 = sqrt(1 + 2 e_i E_(i j) e_j) $

*Step 6: Longitudinal strain*

The longitudinal strain is:
$ ε = (d s - d s_0) / d s_0 = d s / d s_0 - 1 = λ - 1 $

Therefore:
$ ε = sqrt(1 + 2 e_i E_(i j) e_j) - 1 $

*Conclusion:* We have proven both relationships:
- $ λ = sqrt(1 + 2 e_i E_(i j) e_j) $ (stretch ratio)
- $ ε = λ - 1 = sqrt(1 + 2 e_i E_(i j) e_j) - 1 $ (longitudinal strain)

These equations show how the Green strain tensor $bold(E)$ directly relates to measurable quantities (stretch and strain) in any direction $bold(e)$.

=== Longitudinal strain for coordinate axes

*Task:* Use, $epsilon = sqrt(1 +2e_i E_(i j) e_j) - 1$, to determine the general expression for the longitudinal strain and stretch ratio in a line element aligned with the $x_k$-axis of the coordinate system where $k$ may be 1, 2, or 3.

*Step 1: Direction vector for x₁-axis*

For a line element aligned with the $x_1$-axis, the unit direction vector is:
$ bold(e) = bold(e)_1 = mat(1; 0; 0) $

So: $e_1 = 1$, $e_2 = 0$, $e_3 = 0$

*Step 2: Apply equation (3) for x₁-direction*

Using $ε = sqrt(1 + 2 e_i E_(i j) e_j) - 1$:

$ ε_1 = sqrt(1 + 2 e_i E_(i j) e_j) - 1 $

Expanding the sum:
$ e_i E_(i j) e_j = e_1 E_(1 j) e_j + e_2 E_(2 j) e_j + e_3 E_(3 j) e_j $

Since $e_1 = 1$ and $e_2 = e_3 = 0$:
$ e_i E_(i j) e_j = 1 · E_(1 j) e_j = E_(11) e_1 + E_(12) e_2 + E_(13) e_3 $
$ e_i E_(i j) e_j = E_(11) · 1 + E_(12) · 0 + E_(13) · 0 = E_(11) $

Therefore:
$ ε_1 = sqrt(1 + 2 E_(11)) - 1 $
$ λ_1 = sqrt(1 + 2 E_(11)) $

*Step 3: Generalization for arbitrary k*

Following the same procedure for any coordinate axis $x_k$:

For $bold(e) = bold(e)_k$, the unit vector has:
- $e_k = 1$ (component in the k-direction)
- $e_i = 0$ for all $i ≠ k$

Using the general formula:
$ e_i E_(i j) e_j = e_k E_(k j) e_j = E_(k k) e_k = E_(k k) $

*Step 4: General expressions*

For a line element aligned with the $x_k$-axis (where $k = 1, 2, 3$):

*Longitudinal strain:*
$ ε_k = sqrt(1 + 2 E_(k k)) - 1 $

*Stretch ratio:*
$ λ_k = sqrt(1 + 2 E_(k k)) $

*Step 5: Physical interpretation*

These results show that:
- The longitudinal strain in the $k$-direction depends only on the diagonal component $E_(k k)$ of the Green strain tensor
- Off-diagonal terms (shear components) do not contribute to the longitudinal strain along coordinate axes
- For small strains: $E_(k k) << 1$, so $ε_k ≈ E_(k k)$ (using $sqrt(1+x) ≈ 1 + x/2$ for small $x$)

*Examples:*
- $x_1$-direction: $ε_1 = sqrt(1 + 2 E_(11)) - 1$, $λ_1 = sqrt(1 + 2 E_(11))$
- $x_2$-direction: $ε_2 = sqrt(1 + 2 E_(22)) - 1$, $λ_2 = sqrt(1 + 2 E_(22))$
- $x_3$-direction: $ε_3 = sqrt(1 + 2 E_(33)) - 1$, $λ_3 = sqrt(1 + 2 E_(33))$

== Exercise 3: Laplace's Law for Membranes

Laplace's law states:
$ σ_1/r_1 + σ_2/r_2 = p/t $<laplace_law>

where $σ_i$ is the stress along $x_i$, $r_i$ the radius of the shell in $x_i$-direction, $p$ the internal pressure and $t$ the thickness of the membrane. For a thin-walled sphere, the following equation holds:

$ σ = σ_θ = σ_φ = r/(2t) p $<sphere>

For a thin-walled cylinder with capped ends, we have the following equations:
$ σ_z = r/(2t) p, space σ_θ = r/t p $<cylinder> 

=== Derive spherical membrane stress

*Task:* Use Laplace's law, given in  @laplace_law, to derive the formula for the membrane stress in  @sphere, for a spherical membrane.

*Solution:*

For a sphere, the geometry is symmetric in all directions, meaning:
- $r_1 = r_2 = r$ (same radius of curvature in both principal directions)
- $σ_1 = σ_2 = σ$ (same stress in both principal directions due to symmetry)

Substituting into Laplace's law @laplace_law:
$ σ_1/r_1 + σ_2/r_2 = p/t $

$ σ/r + σ/r = p/t $

$ (2σ)/r = p/t $

Solving for $σ$:
$ σ = (r p)/(2t) $

This matches @sphere: $σ = σ_θ = σ_φ = r/(2t) p$

*Physical interpretation:* The stress in a spherical pressure vessel is half that of a cylindrical vessel with the same radius and pressure, due to the biaxial nature of the stress distribution.

=== Derive cylindrical membrane stress

*Task:* Use Laplace's law to derive the membrane stress $σ_θ$ in @cylinder, for a cylindrical membrane.

*Solution:*

For a cylinder, we consider the hoop (circumferential) stress $σ_θ$. The geometry has:
- One principal radius: $r_1 = r$ (circumferential direction)
- Other principal radius: $r_2 = ∞$ (axial direction is straight, no curvature)

For the hoop stress analysis, we consider a circumferential section where:
- $σ_1 = σ_θ$ (hoop stress)
- $σ_2 = 0$ (no stress contribution from axial curvature since $r_2 = ∞$)

Applying Laplace's law:
$ σ_θ/r + 0/∞ = p/t $

$ σ_θ/r = p/t $

Solving for $σ_θ$:
$ σ_θ = (r p)/t $

This matches the hoop stress in @cylinder: $σ_θ = r/t p$

*Note:* The axial stress $σ_z = r/(2t) p$ comes from equilibrium of the end caps, which we'll derive in part c.

=== Free body diagram and axial stress derivation

*Task:* A thin-walled cylindrical container is subjected to an internal pressure $p_i$. The stress $σ_z$ on a plane perpendicular to the axis of the cylinder is given in @cylinder. Sketch a suitable free-body-diagram of the container, and derive the formula for $σ_z$ by requiring equilibrium of the free body.

*Solution:*

*Free Body Diagram:*
Consider a cylindrical section cut by a plane perpendicular to the cylinder axis. The free body consists of:
- Cylindrical wall with internal radius $r$ and wall thickness $t$
- Internal pressure $p_i$ acting on the circular cross-section
- Axial stress $σ_z$ acting on the cylindrical wall cross-section

#figure(
image("images/ex3.1.3c-free-body-diagram.png", width: 100%),
caption: "Free body diagram for cylindrical pressure vessel showing pressure forces (red) and axial stress forces (green).",
)

#figure(
image("images/ex3.1.3c-force-analysis.png", width: 80%),
caption: "Detailed force analysis and mathematical derivation for axial stress.",
)

*Force Analysis:*

*Forces due to internal pressure:*
- Acts on circular area: $A_"pressure" = π r^2$
- Total pressure force: $F_"pressure" = p_i × π r^2$ (acting axially outward)

*Forces due to axial stress:*
- Acts on wall cross-sectional area: $A_"wall" = π(r + t)^2 - π r^2 ≈ 2π r t$ (for thin wall: $t << r$)
- Total axial stress force: $F_"axial" = σ_z × 2π r t$ (acting axially inward)

*Equilibrium condition:*
For static equilibrium, forces must balance:
$ F_"axial" = F_"pressure" $

$ σ_z × 2π r t = p_i × π r^2 $

Solving for $σ_z$:
$ σ_z = (p_i × π r^2)/(2π r t) = (p_i r)/(2t) $

This gives us: $σ_z = r/(2t) p$, confirming @cylinder.

*Physical interpretation:* 
- Hoop stress $σ_θ = r p/t$ is twice the axial stress $σ_z = r p/(2t)$
- This is because the hoop stress resists circumferential expansion, while axial stress only needs to balance the pressure on the end caps
- The factor of 2 difference is fundamental to cylindrical pressure vessel design

