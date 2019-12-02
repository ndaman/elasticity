# AE731
## Theory of Elasticity
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering
December 2, 2019

----
## upcoming schedule

-   Dec 2 - Complex Methods
-   Dec 4 - Final Review, Homework 8 Due
-   Dec 11 - 3:00 - 4:50 Final Exam

----
## outline

<!-- vim-markdown-toc GFM -->

* group problems
* complex variable methods
* research and courses

<!-- vim-markdown-toc -->

---
# group problems

----
## group 1

![group 1 airy stress problem](../images/group-1.png)

----
## group 2

![group 2 airy stress problem](../images/group-2.png)

----
## group 3

![group 3 airy stress problem](../images/group-3.png)

---
# complex variable methods

----
## complex variables

-   Complex variables are made up of a real portion and imaginary portion

_z_ = *x* + *iy*

-   Polar form is written as

_z_ = *r*(cos*θ* + *i*sin*θ*)=*re*<sup>*iθ*</sup>

-   We also define the complex conjugate, $\\bar{z}$

$$\\bar{z} = x - iy = re^{-i\\theta}$$

----
## complex variables

-   A function of complex variables will also be made up of a real and imaginary portion

_f_(*z*)=*f*(*x* + *iy*)=*u*(*x*, *y*)+*iv*(*x*, *y*)

-   We also define the complex conjugate of the complex function

$$\\bar{f(z)} = u(x,y) - i v(x,y)$$

----
## uses for complex variables

-   In Elasticity, complex variables are advantageous in many situations
-   Conformal mappings - allows a solution for a simple shape to be mapped onto a more complicated shape
-   With complex methods we can handle singularities, and quantify the order of a singularity
-   Multivalued displacements (dislocations)
-   Fracture mechanics
-   Westergaard functions (crack analysis)

----
## multiply connected domains

![multiply connected domains](../images/domains.PNG)

----
## mapping

![mapping](../images/mapping.PNG)

----
## westergaard stress function

-   The Westergaard stress function is convenient for many planar crack problems

$$\\begin{aligned}
	\\sigma\_x &= Re\[Z(z)\] - y Im\[Z^\\prime(z)\] - A\\\\
	\\sigma\_y &= Re\[Z(z)\] + y Im\[Z^\\prime(z)\] + A\\\\
	\\tau\_{xy} &= -y Re\[Z^\\prime(z)\]
\\end{aligned}$$

----
## crack example

![westergaard](../images/westergaard.PNG)

----
## crack example

-   Consider the Westergaard stress function

$$Z(z) = \\frac{Sz}{\\sqrt{z^2 - a^2}} - \\frac{S}{2}$$

---
# research and courses

----
## continuum mechanics

-   AE 831, even years Fall
-   A “bigger picture” version of 731
-   Develop framework for large deformation
-   Solids, fluids, and viscoelastic solids

----
## continuum mechanics - research

-   When carbon fiber composites are manufactured, there is always a time where both liquids and solids are present
-   If the system is under any motion, the fluid influences the fibers and the fibers influence the fluid
-   We can use continuum mechanics to model both together and predict where the fibers will be

----
## micromechanics and multi-scale modeling

-   AE 760AA, odd years Spring
-   Analytic and computational methods for multi-scale modeling
-   Particularly applicable to various forms of composites (3D printed, molded composites, etc.)

----
## fracture mechanics

-   AE 737 (very applied class, AE 731 not pre-req), AE 837 (theoretical and numberical fracture mechanics methods, AE 731 is a pre-req)
-   Research applications: characterize interlaminar fracture toughness, fatigue of aerospace structures, etc.


