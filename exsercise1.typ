#import "@preview/dvdtyp:1.0.1": *

#show: dvdtyp.with(
  title: "Exercise 1",
  subtitle: [TKT4150 - Biomechanics],
  author: "Jan-Øivind Lima",
  accent: highlight,
)

#show link: underline
#show link: set text(fill: highlight)

#set math.mat(delim: "[")

#outline(depth: none)

= Assignment 1
== Exercise 1: Eulerian vs. Lagrangian coordinate systems

In continuum mechanics, a coordinate system has to be defined. Two main alternatives exist: Eulerian and
Lagrangian.

=== Explain the diﬀerence between the two coordinate systems, and provide a simple drawing to support it.

The Eulerian coordinate system focuses on specific locations in the space through which the fluid flows. It describes the motion of the fluid at these fixed points as time progresses. In contrast, the Lagrangian coordinate system follows individual fluid particles as they move through space and time.

A simple drawing to illustrate the difference:

#figure(
  image("images/euler-lagra.png", width: 50%,)
)

=== Based on the different coordinate systems, we get diﬀerent kinds of derivatives. Show how you can use the chain rule to establish the _material derivative_.

The material derivative, also known as the total derivative or substantial derivative, describes the rate of change of a quantity (such as temperature, velocity, or concentration) as it is experienced by a moving fluid particle. It combines both the local rate of change at a fixed point and the convective rate of change due to the movement of the fluid.

The material derivative Dφ/Dt of a scalar field φ (e.g., temperature, concentration) is given by:
$ (D φ)/(D t) = (∂φ)/(∂t) + (u · ∇φ) $

== Exercise 2: Reynolds’ transport theorem

The fundamental principles in mechanics; mass, momentum and energy conservation, are all valid for particle mechanics. In cases where it is inconvenient or impossible to track particles in a system, a diﬀerent approach is sought. The equations representing these principles can be transformed to be valid for a predefined bounded volume; a control volume. This is done using the Reynolds’ transport theorem.

=== Explain the differences between an _extensive_ and an _intensive_ property.

Extensive properties are physical quantities that depend on the amount of matter or size of the system. They are additive for subsystems, meaning that if you combine two systems, the extensive property of the combined system is the sum of the extensive properties of the individual systems. Examples of extensive properties include mass, volume, and total energy.

=== Derive Reynolds’ transport theorem.

Reynolds' transport theorem provides a relationship between the rate of change of an extensive property within a control volume and the flux of that property across the control surface.

=== Consider Figure 2. Apply Reynolds’ transport theorem applied to momentum to determine the pressure drop from A1 to A2. Show your control volume. You may neglect viscous eﬀects along the wall of the pipe and assume laminar flow.

#figure(
  image("images/ex1-ex2.png", width: 50%,),
  caption: "Fluid flows through a narrow pipe with area A1 at velocity v1 into a larger pipe with area A2 with a velocity v2 shortly after the junction."
  )

A steady, incompressible CV bounded by:
- an inlet plane just upstream of the step (area A₁, uniform V₁, pressure p₁),
- an outlet plane far enough downstream that the profile is again uniform (area A₂, V₂, p₂),
- the pipe wall including the step.
Neglect wall shear. In the separated/recirculation region on the step, the pressure on the step face is ≈ p₂.

Linear momentum (Reynolds transport theorem)

External pressure forces on the CV:
- Inlet face: $+p_1 A_1$
- Outlet face: $-p_2 A_2$
- Step face: $+p_2(A_2 - A_1)$

The net pressure foce is then:

$ sum(F_x) = p_1 A_1 - p_2 A_2 + p_2(A_2 - A_1) = (p_1 - p_2)A_1 $

Momentum flux:
$ dot(m)(V_2 - V_1) = (rho A_2 V_2^2 - rho A_1 V_1^2) = rho Q (V_2 - V_1), Q = A_2 V_2 = A_1 V_1 $

Set force = momentum rate:

$ (p_1 - p_2)A_1 = rho Q (V_2 - V_1) $

This gives the pressure change as:

$ p_1 - p_2 = rho V_1(V_2 - V_1) $

== Exercise 3: Velocity field

A velocity field is given by

$
  v_1 = (-alpha x_1)/(t_0-t), v_2 = (alpha x_2)/(t_0-t), v_3 = 0
$

where $alpha$ and $t_0$ are constants.

=== Show that the flow is volume preserving, or _isochoric_.

To show that the flow is volume preserving (isochoric), we need to demonstrate that the divergence of the velocity field is zero. The divergence of a velocity field v = (v1, v2, v3) is given by:
$ ∇ · v = (∂v_1)/(∂x_1) + (∂v_2)/(∂x_2) + (∂v_3)/(∂x_3) $
Calculating the partial derivatives:
$ (∂v_1)/(∂x_1) = (∂/∂x_1)((-alpha x_1)/(t_0-t)) = -alpha/(t_0-t) $
$ (∂v_2)/(∂x_2) = (∂/∂x_2)((alpha x_2)/(t_0-t)) = alpha/(t_0-t) $
$ (∂v_3)/(∂x_3) = (∂/∂x_3)(0) = 0 $
Adding these together:
$ ∇ · v = -alpha/(t_0-t) + alpha/(t_0-t) + 0 = 0 $
Since the divergence is zero, the flow is volume preserving (isochoric).

=== Determine the local acceleration, the convective acceleration and the particle acceleration $bold(dot(v))$.

The local acceleration is given by the partial derivative of the velocity field with respect to time:
$ (∂v)/(∂t) = (∂/∂t)((-alpha x_1)/(t_0-t), (alpha x_2)/(t_0-t), 0) = (alpha x_1/(t_0-t)^2, -alpha x_2/(t_0-t)^2, 0) $
The convective acceleration is given by the dot product of the velocity field and the gradient of the velocity field:
$ (v · ∇)v = ((-alpha x_1)/(t_0-t), (alpha x_2)/(t_0-t), 0) · (∂/∂x_1, ∂/∂x_2, ∂/∂x_3)((-alpha x_1)/(t_0-t), (alpha x_2)/(t_0-t), 0) $
Calculating the gradient:
$ ∇v = ((-alpha)/(t_0-t), 0, 0; 0, (alpha)/(t_0-t), 0; 0, 0, 0) $
Now, calculating the convective acceleration:
$ (v · ∇)v = ((-alpha x_1)/(t_0-t), (alpha x_2)/(t_0-t), 0) · ((-alpha)/(t_0-t), 0, 0; 0, (alpha)/(t_0-t), 0; 0, 0, 0) = (alpha^2 x_1/(t_0-t)^2, -alpha^2 x_2/(t_0-t)^2, 0) $
The particle acceleration is the sum of the local and convective accelerations:
$ bold(dot(v)) &= (∂v)/(∂t) + (v · ∇)v \
 &= (alpha x_1/(t_0-t)^2 + alpha^2 x_1/(t_0-t)^2, -alpha x_2/(t_0-t)^2 - alpha^2 x_2/(t_0-t)^2, 0)\
 &= (alpha(1 + alpha)x_1/(t_0-t)^2, -alpha(1 + alpha)x_2/(t_0-t)^2, 0) $   