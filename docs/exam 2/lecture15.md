<span>upcoming schedule</span>

-   Oct 18 - Formulation and Solution Strategies

-   Oct 23 - Exam 2 Review

-   Oct 25 - Strain Energy, HW 5 Due

-   Oct 30 - Exam 2

### outline

\[sections numbered\]

Review
======

<span>field equations</span>

-   Field equations that we have already found

-   Strain-displacement
    $$\\epsilon\_{ij} = \\frac{1}{2}(u\_{i,j} + u\_{j,i})$$

-   Equilibrium
    *σ*<sub>*i**j*, *j*</sub> + *F*<sub>*i*</sub> = 0

-   Constitutive (Hooke’s Law)
    $$\\begin{aligned}
            \\sigma\_{ij} &= \\lambda \\epsilon\_{kk}\\delta\_{ij} + 2\\mu \\epsilon\_{ij}\\\\
            \\epsilon\_{ij} &= \\frac{1+\\nu}{E}\\sigma\_{ij} - \\frac{\\nu}{E}\\sigma\_{kk} \\delta\_{ij}
            \\end{aligned}$$

<span>field equations</span>

-   There are 15 unique field equations to solve for the 15 unknowns

-   3 displacements (*u*<sub>*i*</sub>), 6 unique strain tensor terms (*ϵ*<sub>*i**j*</sub>), and 6 unique stress tensor terms (*σ*<sub>*i**j*</sub>)

-   These equations also depend on a knowledge of the material behavior (*λ*, *μ*) and body forces (usually gravity or zero)

<span>compatibility equations</span>

-   If continuous, single-valued displacements are specified, differentiation will result in well-behaved strain field

-   The inverse relationship, integration of a strain field to find displacement, may not always be true

-   There are cases where we can integrate a strain field to find a set of discontinuous displacements

<span>compatibility equations</span>

-   The compatibility equations enforce continuity of displacements to prevent this from occurring

-   To enforce this condition we consider the strain-displacement relations:
    $$\\epsilon\_{ij} = \\frac{1}{2}(u\_{i,j} + u\_{j,i})$$

-   and differentiate with respect to *x*<sub>*k*</sub> and *x*<sub>*l*</sub>
    $$\\epsilon\_{ij,kl} = \\frac{1}{2}(u\_{i,jkl} + u\_{j,ikl})$$

-   Or
    2*ϵ*<sub>*i**j*, *k**l*</sub> = *u*<sub>*i*, *j**k**l*</sub> + *u*<sub>*j*, *i**k**l*</sub>

<span>compatibility equations</span>

-   The so-called *Saint-Venant compatibility equations* in full are a system of 81 equations, but only six are useful (although even these six are not entirely linearly independent)

-   These six are found by setting *k* = *l*, or in expanded form
    $$\\begin{aligned}
            \\frac{\\partial^2 \\epsilon\_x}{\\partial y^2} + \\frac{\\partial^2 \\epsilon\_y}{\\partial x^2} &= 2\\frac{\\partial^2 \\epsilon\_{xy}}{\\partial x \\partial y}\\\\
            \\frac{\\partial^2 \\epsilon\_y}{\\partial z^2} + \\frac{\\partial^2 \\epsilon\_z}{\\partial y^2} &= 2\\frac{\\partial^2 \\epsilon\_{yz}}{\\partial y \\partial z}\\\\
            \\frac{\\partial^2 \\epsilon\_z}{\\partial x^2} + \\frac{\\partial^2 \\epsilon\_x}{\\partial z^2} &= 2\\frac{\\partial^2 \\epsilon\_{zx}}{\\partial z \\partial x}\\\\
            \\frac{\\partial^2 \\epsilon\_x}{\\partial y \\partial z} &= \\frac{\\partial}{\\partial x} \\left(-\\frac{\\partial \\epsilon\_{yz}}{\\partial x} + \\frac{\\partial \\epsilon\_{zx}}{\\partial y} + \\frac{\\partial \\epsilon\_{xy}}{\\partial z}\\right)\\\\
            \\frac{\\partial^2 \\epsilon\_y}{\\partial z \\partial x} &= \\frac{\\partial}{\\partial y} \\left(-\\frac{\\partial \\epsilon\_{zx}}{\\partial y} + \\frac{\\partial \\epsilon\_{xy}}{\\partial z} + \\frac{\\partial \\epsilon\_{yz}}{\\partial x}\\right)\\\\
            \\frac{\\partial^2 \\epsilon\_z}{\\partial x \\partial y} &= \\frac{\\partial}{\\partial z} \\left(-\\frac{\\partial \\epsilon\_{xy}}{\\partial z} + \\frac{\\partial \\epsilon\_{yz}}{\\partial x} + \\frac{\\partial \\epsilon\_{zx}}{\\partial y}\\right)
            \\end{aligned}$$

<span>beltrami-michell compatibility</span>

-   The compatibility equations in terms of stress are commonly known as the *Beltrami-Michell compatibility equations*

-   When there are no body forces, we can write the six expanded form equations as
    $$\\begin{aligned}
            (1+\\nu) \\nabla^2 \\sigma\_x + \\frac{\\partial^2}{\\partial x^2} (\\sigma\_x + \\sigma\_y + \\sigma\_z) &= 0\\\\
            (1+\\nu) \\nabla^2 \\sigma\_y + \\frac{\\partial^2}{\\partial y^2} (\\sigma\_x + \\sigma\_y + \\sigma\_z) &= 0\\\\
            (1+\\nu) \\nabla^2 \\sigma\_z + \\frac{\\partial^2}{\\partial z^2} (\\sigma\_x + \\sigma\_y + \\sigma\_z) &= 0\\\\
            (1+\\nu) \\nabla^2 \\tau\_{xy} + \\frac{\\partial^2}{\\partial x \\partial y} (\\sigma\_x + \\sigma\_y + \\sigma\_z) &= 0\\\\
            (1+\\nu) \\nabla^2 \\tau\_{yz} + \\frac{\\partial^2}{\\partial y \\partial z} (\\sigma\_x + \\sigma\_y + \\sigma\_z) &= 0\\\\
            (1+\\nu) \\nabla^2 \\tau\_{zx} + \\frac{\\partial^2}{\\partial z \\partial x} (\\sigma\_x + \\sigma\_y + \\sigma\_z) &= 0\\\\
            \\end{aligned}$$

<span>stress formulation</span>

-   For traction problems (i.e. traction is defined on all surfaces) it is convenient to re-formulate field equations in terms of stress only

-   Since displacements are eliminated, we will need to use the compatibility equations to ensure a continuous displacement field

-   It is desirable for this formulation to write the compatibility equations in terms of stress

<span>boundary conditions</span>

<img src="bcs" alt="image" /> \[fig:bcs\]

<span>symmetric boundaries</span>

<img src="symmetric" alt="image" /> \[fig:symmetric\]

<span>boundaries</span>

-   In many systems, the boundaries are parallel to the coordinate system, but this is not always the case

<img src="noncoordinate" alt="image" /> \[fig:noncoordinate\]

<span>solution procedure</span>

-   Solution procedure for stress/traction problems:

-   Assume stress function

-   Must be capable of meeting boundary conditions (linear, quadratic, etc.)

-   Enforce equilibrium

-   Check compatibility

-   Enforce boundary conditions

Displacement Formulation
========================

<span>displacement formulation</span>

-   Just as we posed all field equations in terms of stress for traction problems, it is convenient to pose all the field equations in terms of displacement when dealing with displacement boundary conditions

-   We can use the strain-displacement relations in Hooke’s law to find
    *σ*<sub>*i**j*</sub> = *λ**u*<sub>*k*, *k*</sub>*δ*<sub>*i**j*</sub> + *μ*(*u*<sub>*i*, *j*</sub> + *u*<sub>*j*, *i*</sub>)

<span>navier’s equations</span>

-   We can substitute this relationship into the equilibrium equations to find
    *μ**u*<sub>*i*, *k**k*</sub> + (*λ* + *μ*)*u*<sub>*k*, *k**i*</sub> + *F*<sub>*i*</sub> = 0

-   This is known as *Navier’s* or *Lamé’s equations* and is sometimes written in vector form as
    *μ*∇<sup>2</sup>**u** + (*λ* + *μ*)∇(∇ ⋅ **u**)+**F** = 0

<span>solutions</span>

-   General solutions to Navier’s equations are very difficult to obtain (as with the stress solution)

-   Later in the course, we will learn about *stress functions* and *displacement potential functions*

-   These functions provide a starting point to simplify solving this complicated partial differential equations

<span>example</span>

-   Determine when the following quadratic displacement field will be in equilibrium
    $$\\begin{aligned}
            u &= a\_1 x^2 + b\_1 y^2 + c\_1 xy + d\_1 x + e\_1 y + f\_1\\\\
            v &= a\_2 x^2 + b\_2 y^2 + c\_2 xy + d\_2 x + e\_2 y + f\_2\\\\
            w &= a\_3 x^2 + b\_3 y^2 + c\_3 xy + d\_3 x + e\_3 y + f\_3\\\\
            \\end{aligned}$$

<span>example</span>

-   We use the equilibrium equations in displacement
    *μ**u*<sub>*i*, *k**k*</sub> + (*λ* + *μ*)*u*<sub>*k*, *k**i*</sub> + *F*<sub>*i*</sub> = 0

-   If we consider *u*<sub>*i*, *k**k*</sub>, we find
    $$\\begin{aligned}
            u\_{1,kk} &= 2a\_1 + 2b\_1\\\\
            u\_{2,kk} &= 2a\_2 + 2b\_2\\\\
            u\_{3,kk} &= 2a\_3 + 2b\_3
            \\end{aligned}$$

<span>example</span>

-   The next term is more difficult, so first let us note that *u*<sub>*k*, *k**i*</sub> = (*u*<sub>*k*, *k*</sub>)<sub>,*i*</sub>

-   This gives
    *u*<sub>*k*, *k**i*</sub> = (2*a*<sub>1</sub>*x* + *c*<sub>1</sub>*y* + *d*<sub>1</sub> + 2*b*<sub>2</sub>*y* + *c*<sub>2</sub>*x* + *e*<sub>2</sub> + 0)<sub>,*i*</sub>

-   We can now differentiate this to find
    $$\\begin{aligned}
            u\_{k,k1} &= 2a\_1 + c\_2\\\\
            u\_{k,k2} &= c\_1 + 2b\_2\\\\
            u\_{k,k3} &= 0
            \\end{aligned}$$

<span>example</span>

-   Finally, we can obtain the equilibrium equations as
    $$\\begin{aligned}
            \\mu(2a\_1 + 2b\_1) + (\\lambda+\\mu)(2a\_1 + c\_2) + F\_x &= 0\\\\
            \\mu(2a\_2 + 2b\_2) + (\\lambda+\\mu)(c\_1 + 2b\_2) + F\_y &= 0\\\\
            \\mu(2a\_3 + 2b\_3) + (\\lambda+\\mu)(0) + F\_z &= 0
            \\end{aligned}$$

Principle of Superposition
==========================

<span>principle of superposition</span>

-   Any problem governed by linear equations can be superposed

-   By the principle of superposition if
    *σ*<sub>*i**j*</sub><sup>(1)</sup>, *ϵ*<sub>*i**j*</sub><sup>(1)</sup>, *u*<sub>*i*</sub><sup>(1)</sup>
     are the solution to an elasticity problem with body forces *F*<sub>*i*</sub><sup>(1)</sup> and surface tractions *t*<sub>*i*</sub><sup>(1)</sup> and
    *σ*<sub>*i**j*</sub><sup>(2)</sup>, *ϵ*<sub>*i**j*</sub><sup>(2)</sup>, *u*<sub>*i*</sub><sup>(2)</sup>
     are the solution to an elasticity problem with body forces *F*<sub>*i*</sub><sup>(2)</sup> and surface tractions *t*<sub>*i*</sub><sup>(2)</sup>, then
    *σ*<sub>*i**j*</sub><sup>(1)</sup> + *σ*<sub>*i**j*</sub><sup>(2)</sup>, *ϵ*<sub>*i**j*</sub><sup>(1)</sup> + *ϵ*<sub>*i**j*</sub><sup>(2)</sup>, *u*<sub>*i*</sub><sup>(1)</sup> + *u*<sub>*i*</sub><sup>(2)</sup>
     are the solution to that problem with body forces *F*<sub>*i*</sub><sup>(1)</sup> + *F*<sub>*i*</sub><sup>(2)</sup> and surface tractions *t*<sub>*i*</sub><sup>(1)</sup> + *t*<sub>*i*</sub><sup>(2)</sup>

<span>principle of superposition</span>

-   Superposition is a very useful tool in real elasticity problems

-   A large number of basic elasticity solutions have already been solved, these can be looked up

-   Basic problems often do not have direct real-world applications

-   Many real-world problems can be broken down into the sum of multiple basic problems

<span>principle of superposition</span>

<img src="superposition1" alt="image" /> \[fig:superposition1\]

Saint-Venant’s Principle
========================

<span>saint-venant’s principle</span>

-   The stress, strain, and displacement fields caused by statically equivalent forces are approximately the same far away from the load points

<img src="saint-venant" alt="image" /> \[fig:saint-venant\]

<span>saint-venant’s principle</span>

-   Often the stress/strain field we are concerned with is far away from the load point

-   In this case we can use a statically equivalent load

-   We apply the load in whatever way makes the problem easiest

Examples
========

<span>baseball</span>

-   Consider a baseball with an incombressible rubber core

-   Model the stress field due to some external pressure, *p* given the governing equation is
    $$\\frac{d}{dr} \\left( \\frac{1}{r^2} \\frac{d}{dr}(r^2 u\_r)\\right) = 0$$

<span>hollow cylinder</span>

-   Consider a long, hollow cylinder with pressure applied on both the inner and outer faces

-   Find the stress field given the governing equation
    $$\\frac{\\partial}{\\partial r} \\left( \\frac{1}{r} \\frac{\\partial}{\\partial r} (ru\_r)\\right) = 0$$


