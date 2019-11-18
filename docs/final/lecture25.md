<span>upcoming schedule</span>

-   23 Nov: Complex Methods, Anisotropic Materials

-   25 Nov: No Class (Thanksgiving Break)

-   30 Nov: Final Exam Review, special topics, H/W 8 due

-   2 Dec: Final Exam Review, special topics

-   9 Dec: Final Exam 5:40 - 7:30pm

### outline

\[sections numbered\]

Airy Stress Function with Body Forces
=====================================

<span>body forces</span>

-   Recall that an Airy Stress function must satisfy the Beltrami-Mitchell compatibility equations

-   When there are no body forces, this can be written as
    $$\\nabla^4 \\phi = \\left(\\frac{\\partial ^2}{\\partial r^2} + \\frac{1}{r} \\frac{\\partial}{\\partial r} + \\frac{1}{r^2}\\frac{\\partial ^2}{\\partial \\theta^2}\\right)^2\\phi = 0$$

-   When body forces are significant, we can write the Beltrami-Mitchell equations in terms of the potential function, *V*
    $$\\nabla^4 \\phi = -\\frac{2(\\kappa - 1)}{\\kappa + 1} \\nabla^2 V$$

-   Where the parameter *κ* is used to differentiate between plane strain and plane stress
    $$\\begin{aligned}
            \\kappa &=  3 - 4\\nu &\\text{plain strain}\\\\
            \\kappa &= \\frac{3-\\nu}{1+\\nu} &\\text{plane stress}
            \\end{aligned}$$

<span>body forces</span>

-   We can find the potential function in polar coordinates using the following
    $$\\begin{aligned}
            \\rho b\_r &= -\\frac{\\partial V}{\\partial r}\\\\
            \\rho b\_\\theta &= -\\frac{1}{r} \\frac{\\partial V}{\\partial \\theta}
            \\end{aligned}$$

<span>particular solution</span>

-   We have already found the homogeneous, or complementary solution previously, if we consider
    *ϕ* = *ϕ*<sub>*H*</sub> + *ϕ*<sub>*P*</sub>

-   Then we can add the particular solution
    $$\\nabla^4 \\phi\_P = -\\frac{2(\\kappa - 1)}{\\kappa + 1} \\nabla^2 V$$

-   To the homogeneous solution to find the total solution

<span>polar coordinates</span>

-   If we consider only solutions which are periodic in *θ*, we find
    $$\\begin{aligned}
            \\phi &= a\_0 + a\_1 \\log r + a\_2 r^2 + a\_3 r^2 \\log r \\\\
            &+ (a\_4 + a\_5 \\log r + a\_6 r^2 + a\_7 r^2 \\log r)\\theta \\\\
            &+ \\left(a\_{11}r + a\_{12}r\\log r + \\frac{a\_{13}}{r} + a\_{14}r^3 + a\_{15}r\\theta + a\_{16} r\\theta \\log r\\right) \\cos \\theta\\\\
            &+  \\left(b\_{11}r + b\_{12}r\\log r + \\frac{b\_{13}}{r} + b\_{14}r^3 + b\_{15}r\\theta + b\_{16} r\\theta \\log r\\right) \\sin \\theta\\\\
            &+ \\sum\_{n=2}^{\\infty} (a\_{n1}r^n + a\_{n2}r^{2+n}+a\_{n3}r^{-n}+a\_{n4}r^{2-n})\\cos n\\theta\\\\
            &+ \\sum\_{n=2}^{\\infty} (b\_{n1}r^n + b\_{n2}r^{2+n}+a\_{n3}r^{-n}+b\_{n4}r^{2-n})\\sin n\\theta\\\\
            \\end{aligned}$$

<span>polar coordinates</span>

-   For axisymmetric problems, all field quantities are independent of *θ*

-   This reduces the general solution to
    *ϕ* = *a*<sub>0</sub> + *a*<sub>1</sub>log*r* + *a*<sub>2</sub>*r*<sup>2</sup> + *a*<sub>3</sub>*r*<sup>2</sup>log*r*

Examples
========

<span>curved beam</span>

<img src="curved_beam" alt="image" /> \[fig:curved\_beam\]

<span>rotating disk</span>

<img src="rotating_disk" alt="image" /> \[fig:rotating\_disk\]

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


