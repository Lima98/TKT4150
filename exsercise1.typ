#import "@preview/dvdtyp:1.0.1": *
#import "@preview/cetz:0.4.1"

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
  image("image.png", width: 50%,)
)

=== Based on the diﬀerent coordinate systems, we get diﬀerent kinds of derivatives. Show how you can use the chain rule to establish the _material derivative_.

The material derivative, also known as the total derivative or substantial derivative, describes the rate of change of a quantity (such as temperature, velocity, or concentration) as it is experienced by a moving fluid particle. It combines both the local rate of change at a fixed point and the convective rate of change due to the movement of the fluid.

The material derivative Dφ/Dt of a scalar field φ (e.g., temperature, concentration) is given by:
$ (D φ)/(D t) = (∂φ)/(∂t) + (u · ∇φ) $

== Exercise 2: Reynolds’ transport theorem

The fundamental principles in mechanics; mass, momentum and energy conservation, are all valid for particle mechanics. In cases where it is inconvenient or impossible to track particles in a system, a diﬀerent approach is sought. The equations representing these principles can be transformed to be valid for a predefined bounded volume; a control volume. This is done using the Reynolds’ transport theorem.

=== Explain the diﬀerences between an _extensive_ and an _intensive_ property.

Extensive properties are physical quantities that depend on the amount of matter or size of the system. They are additive for subsystems, meaning that if you combine two systems, the extensive property of the combined system is the sum of the extensive properties of the individual systems. Examples of extensive properties include mass, volume, and total energy.

=== Derive Reynolds’ transport theorem.

Reynolds' transport theorem provides a relationship between the rate of change of an extensive property within a control volume and the flux of that property across the control surface.

=== Consider Figure 1. Apply Reynolds’ transport theorem applied to momentum to determine the pressure drop from A1 to A2. Show your control volume. You may neglect viscous eﬀects along the wall of the pipe and assume laminar flow.

#figure(
  image("image-1.png", width: 50%,),
  caption: "Fluid flows through a narrow pipe with area A1 at velocity v1 into a larger pipe with area A2 with a velocity v2 shortly after the junction."
  )

To apply Reynolds' transport theorem to momentum, we start with the general form of the theorem for an extensive property B:
$ (d/d t) ∫_(C V) ρ b d V + ∫_(C S) ρ b (u · n) d A = ∑ F_"ext" $
Where:
- CV is the control volume
- CS is the control surface
- ρ is the fluid density
- b is the intensive property (momentum per unit mass, which is velocity v) 
- u is the velocity vector of the fluid
- n is the outward-pointing unit normal vector on the control surface
- F_ext represents the external forces acting on the control volume

For momentum, we set b = v (velocity). The left side of the equation represents the rate of change of momentum within the control volume and the net flux of momentum across the control surface. The right side represents the sum of external forces acting on the control volume, which in this case includes pressure forces at the inlet and outlet.


