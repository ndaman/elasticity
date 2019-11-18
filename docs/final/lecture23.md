<span>upcoming schedule</span>

-   Nov 29 - Special Topics

-   Dec 4 - Final Exam Review, HW 8 Due

-   Dec 6 - Final Exam Review

### outline

\[sections numbered\]

group problems
==============

<span>group 1</span>

; ; ; (0,-0.5) – (0,0.5) – (6,0.5) – (6,-0.5) – (0,-0.5); \[-90\]; \[0.5\]\[0.5\]; (2.7,-1) node\[right\] <span>*L*</span> – (0,-1); (3.3,-1) – (6,-1); (3,0.25) node\[below\] <span>2*c*</span> – (3,0.5); (3,-0.25) – (3,-0.5); node at (3,2) <span>*q*</span>;

<span>group 2</span>

; ; ; ; (0,-0.5) – (0,0.5) – (6,0.5) – (6,-0.5) – (0,-0.5); \[-90\]; \[0.5\]\[0.5\]; (2.7,-1.5) node\[right\] <span>*L*</span> – (0,-1.5); (3.3,-1.5) – (6,-1.5); (3,0.25) node\[below\] <span>2*c*</span> – (3,0.5); (3,-0.25) – (3,-0.5); node at (3,2) <span>*q*</span>; ;

<span>group 3</span>

(0,0) – (2,0) – (2,2) – (0,2) – (0,0); (1,1) circle (0.25); (1,2.2) – (2,2.2) node \[above right\] <span>*τ*<sub>0</sub></span>; (2.2,1) – (2.2,2); (-0.2,1) – (-0.2,0) node \[below left\] <span>*τ*<sub>0</sub></span>; (1,-0.2) – (0,-0.2);

Examples
========

<span>curved beam</span>

<img src="curved_beam" alt="image" /> \[fig:curved\_beam\]

<span>rotating disk</span>

<img src="rotating_disk" alt="image" /> \[fig:rotating\_disk\]

special cases
=============

<span>wedge</span>

<img src="wedge" alt="image" style="width:70.0%" />

<span>wedge</span>

-   We can use the polar solution to model a wedge as shown on the previous slide

-   We choose terms which are bounded at *r* = 0 and uniform on the wedge boundaries, which gives the general solution as
    *ϕ* = *r*<sup>2</sup>(*a*<sub>2</sub> + *a*<sub>6</sub>*θ* + *a*<sub>21</sub>cos2*θ* + *b*<sub>21</sub>sin2*θ*)

<span>quarter plane</span>

-   We can now consider some special cases, for example when *α* = 0 and *β* = *π*/2 we have a quarter plane

-   We can solve Equation \[eq:wedge\] for various boundary conditions on the two edges of the quarter plane

<span>half space</span>

-   If we now consider *α* = 0 and *β* = *π* to form a half-space, the wedge solution reduces to
    *ϕ* = *a*<sub>6</sub>*r*<sup>2</sup>*θ* + *b*<sub>21</sub>*r*<sup>2</sup>sin2*θ*

<span>flamant problem</span>

<img src="concentrated" alt="image" style="width:70.0%" />

<span>flamant problem</span>

-   Flamant modified the wedge solution to consider concentrated loads

-   In an infinite continuum, a concentrated load gives unbounded traction at the point of application, so Flamant included terms with a 1/*r* singularity to allow equilibrium under a concentrated load

-   This gives a general solution (in the half-space) as
    *ϕ* = (*a*<sub>12</sub>*r*log*r* + *a*<sub>15</sub>*r**θ*)cos*θ* + (*b*<sub>12</sub>*r*log*r* + *b*<sub>15</sub>*r**θ*)sin*θ*

<span>flamant problem</span>

<img src="flamant2" alt="image" style="width:70.0%" />

<span>notch and crack problems</span>

<img src="crack" alt="image" style="width:70.0%" />

<span>notch and crack problems</span>

-   For the figure shown as *α* → 0 the problem becomes a crack, where the crack faces are traction-free

-   We use the following generalized form of the Polar Coordinate Airy Stress function
    *ϕ* = *r*<sup>*λ*</sup>\[*A*sin*λ**θ* + *B*cos*λ**θ* + *C*sin(*λ* − 2)*θ* + *D*cos(*λ* − 2)*θ*\]

-   Enforcing the traction-free boundary conditions on the crack faces gives
    sin2*π*(*λ* − 1)=0

Complex Variable Methods
========================

<span>complex variables</span>

-   Complex variables are made up of a real portion and imaginary portion
    *z* = *x* + *i**y*

-   Polar form is written as
    *z* = *r*(cos*θ* + *i*sin*θ*)=*r**e*<sup>*i**θ*</sup>

-   We also define the complex conjugate, $\\bar{z}$
    $$\\bar{z} = x - iy = re^{-i\\theta}$$

<span>complex variables</span>

-   A function of complex variables will also be made up of a real and imaginary portion
    *f*(*z*)=*f*(*x* + *i**y*)=*u*(*x*, *y*)+*i**v*(*x*, *y*)

-   We also define the complex conjugate of the complex function
    $$\\bar{f(z)} = u(x,y) - i v(x,y)$$

<span>uses for complex variables</span>

-   In Elasticity, complex variables are advantageous in many situations

-   Conformal mappings - allows a solution for a simple shape to be mapped onto a more complicated shape

-   With complex methods we can handle singularities, and quantify the order of a singularity

-   Multivalued displacements (dislocations)

-   Fracture mechanics

-   Westergaard functions (crack analysis)

<span>multiply connected domains</span>

<img src="domains" alt="image" /> \[fig:domains\]

<span>mapping</span>

<img src="mapping" alt="image" /> \[fig:mapping\]

<span>westergaard stress function</span>

-   The Westergaard stress function is convenient for many planar crack problems
    $$\\begin{aligned}
            \\sigma\_x &= Re\[Z(z)\] - y Im\[Z^\\prime(z)\] - A\\\\
            \\sigma\_y &= Re\[Z(z)\] + y Im\[Z^\\prime(z)\] + A\\\\
            \\tau\_{xy} &= -y Re\[Z^\\prime(z)\]
            \\end{aligned}$$

<span>crack example</span>

<img src="westergaard" alt="image" /> \[fig:westergaard\]

<span>crack example</span>

-   Consider the Westergaard stress function
    $$Z(z) = \\frac{Sz}{\\sqrt{z^2 - a^2}} - \\frac{S}{2}$$

research and courses
====================

<span>continuum mechanics</span>

-   AE 831, even years Fall

-   A “bigger picture” version of 731

-   Develop framework for large deformation

-   Solids, fluids, and viscoelastic solids

<span>continuum mechanics - research</span>

-   When carbon fiber composites are manufactured, there is always a time where both liquids and solids are present

-   If the system is under any motion, the fluid influences the fibers and the fibers influence the fluid

-   We can use continuum mechanics to model both together and predict where the fibers will be

<span>micromechanics and multi-scale modeling</span>

-   AE 760AA (860AA?), odd years Spring

-   Analytic and computational methods for multi-scale modeling

-   Particularly applicable to various forms of composites (3D printed, molded composites, etc.)

<span>fracture mechanics</span>

-   AE 737 (very applied class, AE 731 not pre-req), AE 837 (theoretical and numberical fracture mechanics methods, AE 731 is a pre-req)

-   Research applications: characterize interlaminar fracture toughness, fatigue of aerospace structures, etc.


