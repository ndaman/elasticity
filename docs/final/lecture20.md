# AE731
## Theory of Elasticity
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering
November 20, 2019

----
## upcoming schedule

-   Nov 20 - Airy Stress, Homework 7 Due
-   Nov 25 - Airy Stress
-   Nov 27 - No Class (Thanksgiving Break)

<span>upcoming schedule</span>

-   11 Nov: Chapter 7 lecture, H/W 7 assigned, Chapter 8

-   16 Nov: Chapter 8 lecture

-   18 Nov: Chapter 8, H/W 7 due, H/W 8 assigned

-   23 Nov: special topics

-   25 Nov: No Class (Thanksgiving Break)

-   30 Nov: Final Exam Review, special topics, H/W 8 due

-   2 Dec: Final Exam Review, special topics

-   9 Dec: Final Exam 5:40 - 7:30pm

### outline

\[sections numbered\]

Airy Stress Functions
=====================

<span>airy stress function</span>

-   A stress function technique that can be used to solve many planar problems is known as the *Airy stress function*

-   This method reduces the governing equations for a planar problem to a single unknown function

-   We assume first that body forces are derivable from a *potential function*, *V*
    $$\\begin{aligned}
            F\_x &= -\\frac{\\partial V}{\\partial x}\\\\
            F\_y &= -\\frac{\\partial V}{\\partial y}
            \\end{aligned}$$

-   How restrictive is this assumption?

-   Most body forces are linear (gravity) and can easily be represented this way

<span>airy stress function</span>

-   Consider the following
    $$\\begin{aligned}
            \\sigma\_{xx} &= \\frac{\\partial^2 \\phi}{\\partial y^2} + V\\\\
            \\sigma\_{yy} &= \\frac{\\partial^2 \\phi}{\\partial x^2} + V\\\\
            \\tau\_{xy} &= -\\frac{\\partial^2 \\phi}{\\partial x \\partial y}
            \\end{aligned}$$

-   The function *ϕ* = *ϕ*(*x*, *y*) is known as the Airy stress function

-   When constructed in this way, equilibrium is automatically satisfied

<span>compatibility</span>

-   Substituting the Airy Stress function and potential function into the relationships, we find
    $$\\begin{aligned}
            \\frac{\\partial^4 \\phi}{\\partial x^4} + 2\\frac{\\partial^4 \\phi}{\\partial x^2 \\partial y^2} + \\frac{\\partial^4 \\phi}{\\partial y^4} &= - \\frac{1-2\\nu}{1-\\nu}\\left(\\frac{\\partial^2 V}{\\partial x^2} + \\frac{\\partial^2 V}{\\partial y^2}\\right) &\\text{plane strain}\\\\
            \\frac{\\partial^4 \\phi}{\\partial x^4} + 2\\frac{\\partial^4 \\phi}{\\partial x^2 \\partial y^2} + \\frac{\\partial^4 \\phi}{\\partial y^4} &= - (1-\\nu)\\left(\\frac{\\partial^2 V}{\\partial x^2} + \\frac{\\partial^2 V}{\\partial y^2}\\right) &\\text{plane stress}
            \\end{aligned}$$

-   If there are no body forces, or the potential function satisfies Laplace’s Equation
    ∇<sup>2</sup>*V* = 0
     Then both plane stress and plane strain reduce to
    $$\\frac{\\partial^4 \\phi}{\\partial x^4} + 2\\frac{\\partial^4 \\phi}{\\partial x^2 \\partial y^2} + \\frac{\\partial^4 \\phi}{\\partial y^4} = 0$$

Polar Coordinates
=================

<span>strain-displacement</span>

-   For planar problems we can reduce the strain-displacement relationships we learned previously
    $$\\begin{aligned}
            \\epsilon\_r &= \\frac{\\partial u\_r}{\\partial r}, \\epsilon\_\\theta = \\frac{1}{r}\\left(u\_r + \\frac{\\partial u\_\\theta}{\\partial \\theta}\\right), \\epsilon\_z = \\frac{\\partial u\_z}{\\partial z}\\\\
            \\epsilon\_{r \\theta} &= \\frac{1}{2} \\left(\\frac{1}{r} \\frac{\\partial u\_r}{\\partial \\theta} + \\frac{\\partial u\_\\theta}{\\partial r} - \\frac{u\_\\theta}{r}\\right) \\\\
            \\epsilon\_{\\theta z} &= \\frac{1}{2} \\left(\\frac{\\partial u\_\\theta}{\\partial z} + \\frac{1}{r}\\frac{\\partial u\_z}{\\partial \\theta}\\right)\\\\
            \\epsilon\_{zr} &= \\frac{1}{2}\\left(\\frac{\\partial u\_r}{\\partial z} + \\frac{\\partial u\_z}{\\partial r}\\right)
            \\end{aligned}$$

<span>strain-displacement</span>

-   Which become
    $$\\begin{aligned}
            \\epsilon\_r &= \\frac{\\partial u\_r}{\\partial r}\\\\
            \\epsilon\_\\theta &= \\frac{1}{r}\\left(u\_r + \\frac{\\partial u\_\\theta}{\\partial \\theta}\\right)\\\\
            \\epsilon\_{r \\theta} &= \\frac{1}{2} \\left(\\frac{1}{r} \\frac{\\partial u\_r}{\\partial \\theta} + \\frac{\\partial u\_\\theta}{\\partial r} - \\frac{u\_\\theta}{r}\\right) \\\\
            \\end{aligned}$$

<span>integration</span>

-   When we change variables in integration, we also need to account for the proper change in dV

-   *d**V* = *d**x**d**y**d**z* ≠ *d**r**d**θ**d**z*

-   We can find the correct *d**V* by calculating the Jacobian
    $$dV = dx dy dz = |\\frac{\\partial(x,y,z)}{\\partial(r,\\theta,z)}| dr d\\theta dz$$
    $$dV = \\begin{vmatrix}
            \\frac{\\partial x}{\\partial r} & \\frac{\\partial x}{\\partial \\theta} & \\frac{\\partial x}{\\partial z}\\\\
            \\frac{\\partial y}{\\partial r} & \\frac{\\partial y}{\\partial \\theta} & \\frac{\\partial y}{\\partial z}\\\\
            \\frac{\\partial z}{\\partial r} & \\frac{\\partial z}{\\partial \\theta} & \\frac{\\partial z}{\\partial z}
            \\end{vmatrix} dr d\\theta dz = r dr d\\theta dz$$

<span>hooke’s law</span>

-   The tensor equation for Hooke’s Law is valid in polar/cylindrical/spherical coordinates too

-   We only need special equations when differentiating or integrating
    $$\\begin{aligned}
            \\sigma\_{ij} &= \\lambda \\epsilon\_{kk}\\delta\_{ij} + 2\\mu \\epsilon\_{ij} - (3\\lambda + 2\\mu)\\alpha\\Delta T \\delta\_{ij}\\\\
            \\epsilon\_{ij} &= \\frac{1+\\nu}{E}\\sigma\_{ij} - \\frac{\\nu}{E}\\sigma\_{kk} \\delta\_{ij} + \\alpha\\Delta T \\delta\_{ij}
            \\end{aligned}$$

<span>equilibrium</span>

-   We have already found the equilibrium equations in polar coordinates, they are
    $$\\begin{aligned}
            \\frac{\\partial \\sigma\_r}{\\partial r} + \\frac{1}{r} \\frac{\\partial \\tau\_{r \\theta}}{\\partial \\theta} + \\frac{1}{r}(\\sigma\_r - \\sigma\_\\theta) + F\_r &= 0 \\\\
            \\frac{\\partial \\tau\_{r \\theta}}{\\partial r} + \\frac{1}{r} \\frac{\\partial \\sigma\_\\theta}{\\partial \\theta} + \\frac{2}{r}\\tau\_{r\\theta} + F\_\\theta &= 0
            \\end{aligned}$$

<span>equilibrium</span>

-   The equilibrium equations can be written in terms of displacement (Navier equations)

-   These are only useful when using a displacement formulation, but we are using stress functions

-   Instead we need the Beltrami-Mitchell compatibility equations

<span>compatibility</span>

-   Substituting stress-strain relations into the compatibility equations gives
    $$\\begin{aligned}
            \\nabla^2 (\\sigma\_r + \\sigma\_\\theta) &= -\\frac{1}{1-\\nu}\\left(\\frac{\\partial F\_r}{\\partial r} + \\frac{F\_r}{r} + \\frac{1}{r}\\frac{\\partial F\_\\theta}{\\partial \\theta}\\right) & \\text{(Plane Strain)}\\\\
            \\nabla^2 (\\sigma\_r + \\sigma\_\\theta) &= -(1+\\nu)\\left(\\frac{\\partial F\_r}{\\partial r} + \\frac{F\_r}{r} + \\frac{1}{r}\\frac{\\partial F\_\\theta}{\\partial \\theta}\\right) & \\text{(Plane Stress)}
            \\end{aligned}$$

<span>airy stress functions</span>

-   When the body forces are zero, we find
    $$\\begin{aligned}
            \\sigma\_r &= \\frac{1}{r}\\frac{\\partial \\phi}{\\partial r} + \\frac{1}{r^2}\\frac{\\partial^2 \\phi}{\\partial \\theta^2}\\\\
            \\sigma\_\\theta &= \\frac{\\partial^2 \\phi}{\\partial r^2}\\\\
            \\tau\_{r\\theta} &= -\\frac{\\partial}{\\partial r} \\left( \\frac{1}{r} \\frac{\\partial \\phi}{\\partial \\theta} \\right)
            \\end{aligned}$$

<span>airy stress functions</span>

-   When body forces are zero, we find the following biharmonic equation for the Beltrami-Mitchell equations
    ∇<sup>4</sup>*ϕ* = 0

-   Where the Laplacian is
    $$\\nabla^2 = \\frac{\\partial^2}{\\partial r^2} + \\frac{1}{r}\\frac{\\partial}{\\partial r} + \\frac{1}{r^2} \\frac{\\partial^2}{\\partial \\theta^2}$$

Antiplane Strain
================

<span>antiplane strain</span>

-   One theory to be aware of is known as “antiplane strain”

-   Used in geomechanics

-   Assumes that displacements are
    $$\\begin{aligned}
            u &= v = 0\\\\
            w &= w(x,y)
            \\end{aligned}$$

Polynomial Solutions
====================

<span>airy stress function solutions</span>

-   To solve a problem using Airy stress functions, we need to solve this biharmonic equation
    $$\\frac{\\partial^4 \\phi}{\\partial x^4} + 2\\frac{\\partial^4 \\phi}{\\partial x^2 \\partial y^2} + \\frac{\\partial^4 \\phi}{\\partial y^4} = 0$$

-   One solution to this is the power series
    $$\\phi(x,y) = \\sum\_{m=0}^{\\infty} \\sum\_{n=0}^{\\infty} A\_{mn} x^m y^n$$

<span>power series solution</span>

-   Note that terms for *m* + *n* ≤ 1 do not contribute to the stress, and can be neglected

-   Also note that for *m* + *n* ≤ 3 compatibility is automatically satisfied

-   For *m* + *n* ≥ 4 the coefficients must be related for compatibility to be satisfied

<span>example</span>

<img src="tension" alt="image" /> \[fig:tension\]

<span>example</span>

-   What are the boundary conditions in terms of the stress tensor?
    $$\\begin{aligned}
            \\sigma\_x (\\pm l,y) &= T\\\\
            \\sigma\_y (x, \\pm c) &= 0\\\\
            \\tau\_{xy} (\\pm l, y) &= \\tau\_{xy} (x, \\pm c) = 0
            \\end{aligned}$$

-   What is the simplest form of polynomial stress function that would satisfy these boundary conditions?
    $$\\begin{aligned}
            \\sigma\_{xx} &= \\frac{\\partial^2 \\phi}{\\partial y^2} + V\\\\
            \\sigma\_{yy} &= \\frac{\\partial^2 \\phi}{\\partial x^2} + V\\\\
            \\tau\_{xy} &= -\\frac{\\partial^2 \\phi}{\\partial x \\partial y}
            \\end{aligned}$$

<span>saint venant’s principle</span>

-   Some boundary conditions are cumbersome to model exactly

-   In this case we can use Saint Venant’s principle to express a statically equivalent version of the boundary conditions

<span>example</span>

<img src="bending" alt="image" /> \[fig:bending\]

<span>example</span>

-   Locally along the ends, there will be some tractions in order to apply the bending moment

-   These tractions will cancel out, however, so we can use Saint Venant’s principle to avoid modeling them explicitly
    $$\\begin{aligned}
            \\sigma\_y (x, \\pm c) &= 0\\\\
            \\tau\_{xy} (x, \\pm c) &= \\tau\_{xy} (\\pm L, y) = 0\\\\
            \\int\_{-c}^{c}\\sigma\_x (\\pm l,y)dy &= 0\\\\
            \\int\_{-c}^{c}\\sigma\_x (\\pm l,y)ydy &= -M
            \\end{aligned}$$

<span>example</span>

-   What is the simplest form of polynomial stress function that would satisfy these boundary conditions?
    $$\\begin{aligned}
            \\sigma\_{xx} &= \\frac{\\partial^2 \\phi}{\\partial y^2} + V\\\\
            \\sigma\_{yy} &= \\frac{\\partial^2 \\phi}{\\partial x^2} + V\\\\
            \\tau\_{xy} &= -\\frac{\\partial^2 \\phi}{\\partial x \\partial y}
            \\end{aligned}$$

<span>example</span>

<img src="distributed" alt="image" /> \[fig:distributed\]

<span>example</span>

-   In this case we can write the boundary conditions as
    $$\\begin{aligned}
            \\tau\_{xy}(x, \\pm c) &= 0\\\\
            \\sigma\_y (x,c) &= 0\\\\
            \\sigma\_y (x,-c) &= -w\\\\
            \\int\_{-c}^{c} \\sigma\_x (\\pm l, y) dy &= 0\\\\
            \\int\_{-c}^{c} \\sigma\_x (\\pm l, y) ydy &= 0\\\\
            \\int\_{-c}^{c} \\tau\_{xy} (\\pm l, y) dy &= \\mp wl\\\\
            \\end{aligned}$$

<span>example</span>

-   And find that the stress function
    $$\\phi = Ax^2 + Bx^2 y + Cx^2 y^3 + Dy^3 - \\frac{1}{5}C y^5$$

-   Can satisfy the boundary conditions as well as compatibility


