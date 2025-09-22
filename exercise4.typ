#import "@preview/dvdtyp:1.0.1": *

#show: dvdtyp.with(
  title: "Exercise 4",
  subtitle: [TKT4150 - Biomechanics],
  author: "Jan-Øivind Lima",
  accent: highlight,
)

#show link: underline
#show link: set text(fill: highlight)

#set math.mat(delim: "[")
#set math.equation(numbering: "(1)")

#outline(depth: none)

= Assignment 4
== Exercise 1: Cauchy equations

#figure(
  image("images/arteries-veins.png", width: 40%),
  caption: "Arteries and veins",
)

=== Formula for pressure in a still body of fluid

Starting with the Cauchy equation:
$ T_(i j,j) = (∂)/(∂x_j)(T_(i j)) = (∂)/(∂x_j)(-p δ_(i j)) = -(∂p)/(∂x_j) δ_(i j) $

$ = -(∂p)/(∂x_1) δ_(i 1) - (∂p)/(∂x_2) δ_(i 2) - (∂p)/(∂x_3) δ_(i 3) $

The pressure only depends on the vertical distance, so we can then reduce this to:
$ T_(i j,j) = -(∂p)/(∂x_3) space "for" i=3 $
$ = 0 space "otherwise" $

For equilibrium with no external acceleration, the Cauchy equation becomes:
$ -(∂p)/(∂z) + ρ g = 0 $

which gives:
$ ∇ p = (∂p)/(∂z) = ρ g $

Integrating:
$ p(z) = ∫ ρ g d z = ρ g z + C $

With boundary condition $p(z = 0) = p_0$, we get $C = p_0$, thus:

*Result:* $p(z) = ρ g z + p_0$

=== Blood pressure in foot 

Using the formula from the task above:
$ p(z) = ρ g z + p_0 $

Veins:
$ p_v (1.2m) &= p_(v h) + rho g h \
&= 10 k P a + 1000 (k g)/(m^3) dot 9.81 (m/s^2) dot 1.2 (m)\
&= 10 k P a + 11.8 k P a = 21.8 k P a $

Arteries:
$ p_a (1.2m) &= p_(a h) + rho g h \
&= 16 k P a + 1000 (k g)/(m^3) dot 9.81 (m/s^2) dot 1.2 (m)\
&= 16 k P a + 11.8 k P a = 27.8 k P a $

== Exercise 2: Hooke's law
=== Superposition
Apply superposition of three uni-axial cases:
- $σ_1$ only: $ε_1 = σ_1/η$, $ε_2 = ε_3 = -ν σ_1/η$
- $σ_2$ only: $ε_2 = σ_2/η$, $ε_1 = ε_3 = -ν σ_2/η$  
- $σ_3$ only: $ε_3 = σ_3/η$, $ε_1 = ε_2 = -ν σ_3/η$

Total strain in direction 1:
$ ε_1 = σ_1/η - ν σ_2/η - ν σ_3/η = σ_1/η + ν σ_1/η - ν/η(σ_1 + σ_2 + σ_3) $
$ ε_1 = (1+ν)/η σ_1 - ν/η "tr" bold(T) $<2a-result>

Similarly for $ε_2$ and $ε_3$, giving the general result.

=== Index notation tensor form 

The following shear stress-strain relation is assumed:
$ E_(i j) = (1+ν)/η T_(i j) space i ≠ j $<stress-strain>

From this, establish the index notation tensor version of Hooke's law, with strain on left hand side, that incorporates both normal and shear components.

From part a), we use @2a-result.

From @stress-strain, strains: $E_(i j) = (1+ν)/η T_(i j)$ for $i ≠ j$

We can unify these using the Kronecker delta $δ_(i j)$:

$ E_(i j) = (1+ν)/η T_(i j) - ν/η δ_(i j) "tr" bold(T) $

*Verification:*
- When $i = j$: $E_(i i) = (1+ν)/η T_(i i) - ν/η "tr" bold(T)$ 
- When $i ≠ j$: $E_(i j) = (1+ν)/η T_(i j) - 0 = (1+ν)/η T_(i j)$

*Complete tensor form of Hooke's law:*
$ bold(E) = (1+ν)/η bold(T) - ν/η ("tr" bold(T)) bold(I) $

=== No task, only an equaion?
=== Plane stress conditions

*Given:* Inverse relation: $ T_(i j) = η/(1+ν) (E_(i j) + ν/(1-2ν) E_(k k) δ_(i j)) $<inverse-relation>

*Task:* Under plane stress conditions $T_(i 3) = 0$ for $i = 1,2,3$, show that @inverse-relation becomes:
$ T_(α β) = η/(1+ν) (E_(α β) + ν/(1-ν) E_(ρ ρ) δ_(α β)) space α = 1,2 $ (6)

*Solution:*

From $T_(33) = 0$ in equation (4):
$ E_(33) + ν/(1-2ν) E_(k k) = 0 $

Solving: $E_(33) = -ν/(1-2ν) E_(k k)$

Substituting back: $E_(k k) = E_(11) + E_(22) + E_(33) = E_(ρ ρ) - ν/(1-2ν) E_(k k)$

Therefore: $E_(k k) (1 + ν/(1-2ν)) = E_(ρ ρ)$, giving $E_(k k) = (1-2ν)/(1-ν) E_(ρ ρ)$

Substituting into equation (4): $ν/(1-2ν) E_(k k) = ν/(1-2ν) · (1-2ν)/(1-ν) E_(ρ ρ) = ν/(1-ν) E_(ρ ρ)$

Result: $T_(α β) = η/(1+ν) (E_(α β) + ν/(1-ν) E_(ρ ρ) δ_(α β))$

== Exercise 3: Navier's equations

The Cauchy equations read out:
$ T_(i j, j) + ρ b_i = ρ ü_i $

Compatibility requires:
$ E_(i j) = 1/2 (u_(i, j) + u_(j, i)) $

By introducing Hooke's law and Green's strain tensor, the Cauchy equations are simplified. The result is called Navier's equations.

=== Derive Navier's equations

From Hooke's law: $ T_(i j) = η/(1+ν) (E_(i j) + ν/(1-2ν) E_(k k) δ_(i j)) $

From compatibility: $ E_(i j) = 1/2 (u_(i, j) + u_(j, i)) $

Therefore: $ E_(k k) = E_(11) + E_(22) + E_(33) = 1/2 (2u_(1,1) + 2u_(2,2) + 2u_(3,3)) = u_(k,k) $

Substituting into Hooke's law:
$ T_(i j) = η/(1+ν) (1/2 (u_(i, j) + u_(j, i)) + ν/(1-2ν) u_(k,k) δ_(i j)) $

Taking divergence for Cauchy equation:
$ T_(i j, j) = η/(1+ν) (1/2 (u_(i, j j) + u_(j, i j)) + ν/(1-2ν) u_(k,k j) δ_(i j)) $

Since $u_(j, i j) = u_(j, j i) = u_(k,k i)$ and $δ_(i j, j) = 0$:
$ T_(i j, j) = η/(1+ν) (1/2 u_(i, j j) + 1/2 u_(k,k i) + ν/(1-2ν) u_(k,k i)) $
$ = η/(1+ν) (1/2 u_(i, j j) + (1/2 + ν/(1-2ν)) u_(k,k i)) $
$ = η/(1+ν) (1/2 u_(i, j j) + (1-2ν+2ν)/(2(1-2ν)) u_(k,k i)) $
$ = η/(1+ν) (1/2 u_(i, j j) + 1/(2(1-2ν)) u_(k,k i)) $

Substituting into Cauchy equation (7):
$ η/(1+ν) (1/2 u_(i, j j) + 1/(2(1-2ν)) u_(k,k i)) + ρ b_i = ρ ü_i $

*Navier's equation:*
$ η/(2(1+ν)) u_(i, j j) + η/(2(1+ν)(1-2ν)) u_(k,k i) + ρ b_i = ρ ü_i $

== Exercise 4: Hyperelasticity

A material is hyperelastic if there exists a potential function $φ = φ(E_(i j))$ that satisfies $T_(i j) = (∂φ)/(∂E_(i j))$, i.e. the stress is defined by a potential function of the strain. An equivalent definition of hyperelasticity requires that the stress power $ω$ may be derived from a scalar valued potential $φ(E_(i j))$:

$ ω = dot(φ) = (∂φ)/(∂E_(i j)) dot(E)_(i j) $ (9)

=== Stress power

Stress power $ω$ is the rate of energy dissipation or storage per unit volume in a deforming material. It represents:
- Power = Energy/Time per unit volume
- $ω = T_(i j) dot(E)_(i j)$ (stress × strain rate)
- Physical meaning: Rate of work done by internal stresses during deformation

=== Equivalence of definitions


*Definition 1:* $ T_(i j) = (∂φ)/(∂E_(i j)) $ (stress from potential)
*Definition 2:* $ ω = dot(φ) = (∂φ)/(∂E_(i j)) dot(E)_(i j) $ (stress power from potential rate)

From Definition 1, substitute into stress power:
$ ω = T_(i j) dot(E)_(i j) = (∂φ)/(∂E_(i j)) dot(E)_(i j) $

Using chain rule: $dot(φ) = (∂φ)/(∂E_(i j)) dot(E)_(i j)$

Therefore: $ω = dot(φ)$, which is Definition 2.

Conversely, if $ω = dot(φ) = (∂φ)/(∂E_(i j)) dot(E)_(i j)$ and $ω = T_(i j) dot(E)_(i j)$, then:
$ T_(i j) dot(E)_(i j) = (∂φ)/(∂E_(i j)) dot(E)_(i j) $

Since this holds for arbitrary $dot(E)_(i j)$: $T_(i j) = (∂φ)/(∂E_(i j))$

The definitions are equivalent.

== Exercise 5: Piola-Kirchhoff stress

=== Tensor form relations

*Cauchy stress (true stress):* $bold(σ)$ - stress per unit deformed area

*First Piola-Kirchhoff stress:* $bold(P)$ - force per unit reference area
$ bold(P) = J bold(σ) bold(F)^(-T) $

*Second Piola-Kirchhoff stress:* $bold(S)$ - reference configuration stress  
$ bold(S) = bold(F)^(-1) bold(P) = J bold(F)^(-1) bold(σ) bold(F)^(-T) $

*Relations:*
- $bold(P) = J bold(σ) bold(F)^(-T)$ (Cauchy → First PK)
- $bold(S) = bold(F)^(-1) bold(P)$ (First PK → Second PK)  
- $bold(S) = J bold(F)^(-1) bold(σ) bold(F)^(-T)$ (Cauchy → Second PK)

where $J = det(bold(F))$ is the Jacobian of deformation.

=== Symmetry of second Piola-Kirchhoff stress

From angular momentum balance, the Cauchy stress is symmetric: $bold(σ) = bold(σ)^T$

The second Piola-Kirchhoff stress is:
$ bold(S) = J bold(F)^(-1) bold(σ) bold(F)^(-T) $

Taking the transpose:
$ bold(S)^T = (J bold(F)^(-1) bold(σ) bold(F)^(-T))^T $
$ = J (bold(F)^(-T))^T bold(σ)^T (bold(F)^(-1))^T $
$ = J bold(F)^(-1) bold(σ)^T bold(F)^(-T) $

Since $bold(σ) = bold(σ)^T$ (Cauchy stress is symmetric):
$ bold(S)^T = J bold(F)^(-1) bold(σ) bold(F)^(-T) = bold(S) $

Therefore, the second Piola-Kirchhoff stress tensor is symmetric: $bold(S) = bold(S)^T$


