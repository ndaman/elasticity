<span>upcoming schedule</span>

-   Oct 11 - Formulation and Solution Strategies, HW 4 Due

-   Oct 16 - No Class (fall break)

-   Oct 18 - Formulation and Solution Strategies

-   Oct 23 - Formulation and Solution Strategies

### outline

\[sections numbered\]

group problems
==============

<span>group one</span>

-   Consider some arbitrary, isotropic material under uni-axial tension

-   What occurs when $\\nu = \\frac{1}{2}$?

-   What about when *ν* &lt; 0?

<span>group two</span>

-   Consider a ±45<sup>∘</sup> laminate (which has an in-plane poisson’s ratio of 0.8) bonded on top of aluminum (which has an in-plane poisson’s ratio of 0.3)

-   What happens when this is loaded in tension? Why might this create problems in the adhesive joining the two?

<span>group three</span>

-   Use the table provided in these notes (or in the text) to re-write Hooke’s Law in terms of Young’s Modulus, *E* and shear modulus *G*.

Field Equations
===============

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

-   We can eliminate the displacement terms from the equation by interchanging the indexes to generate new equations
    $$\\begin{aligned}
            2\\epsilon\_{ik,jl} &= u\_{i,jkl} + u\_{k,ijl} \\\\
            2\\epsilon\_{jl,ik} &= u\_{j,ikl} + u\_{l,ijk}
            \\end{aligned}$$

-   Solving for *u*<sub>*i*, *j**k**l*</sub> and *u*<sub>*j*, *i**k**l*</sub>
    $$\\begin{aligned}
            u\_{i,jkl} &= 2\\epsilon\_{ik,jl} - u\_{k,ijl} \\\\
            u\_{j,ikl} &= 2\\epsilon\_{jl,ik} - u\_{l,ijk}
            \\end{aligned}$$

<span>compatibility equations</span>

-   Substituting these values into the equations gives
    2*ϵ*<sub>*i**j*, *k**l*</sub> = 2*ϵ*<sub>*i**k*, *j**l*</sub> − *u*<sub>*k*, *i**j**l*</sub> + 2*ϵ*<sub>*j**l*, *i**k*</sub> − *u*<sub>*l*, *i**j**k*</sub>

-   We now consider one more change of index equation
    2*ϵ*<sub>*k**l*, *i**j*</sub> = *u*<sub>*k*, *i**j**l*</sub> + *u*<sub>*l*, *i**j**k*</sub>

-   and substituting this result gives
    2*ϵ*<sub>*i**j*, *k**l*</sub> = 2*ϵ*<sub>*i**k*, *j**l*</sub> + 2*ϵ*<sub>*j**l*, *i**k*</sub> − 2*ϵ*<sub>*k**l*, *i**j*</sub>

-   Or, simplified
    *ϵ*<sub>*i**j*, *k**l*</sub> + *ϵ*<sub>*k**l*, *i**j*</sub> − *ϵ*<sub>*i**k*, *j**l*</sub> − *ϵ*<sub>*j**l*, *i**k*</sub> = 0

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

<span>compatibility equations</span>

-   The compatibility equations are necessary to ensure that the strain field is valid and will produce a continuous displacement field

-   While these equations are important and necessary in solving elasticity problems, they are not sufficient

-   15 equations with 15 “unknowns” but each of these “unknowns” could actually be a function with many more unknowns, we need to develop framework for simplifying the problem into something we can solve

Boundary Conditions
===================

<span>boundary conditions</span>

-   Boundary conditions commonly specify how a body is supported and/or how it is loaded

-   Mathematically we treat this conditions as *displacements* or *tractions* at boundary points.

-   Symmetry boundary conditions are also common, can reduce computational cost and simplify analytic solutions.

<span>boundary conditions</span>

<img src="bcs" alt="image" /> \[fig:bcs\]

<span>symmetric boundaries</span>

<img src="symmetric" alt="image" /> \[fig:symmetric\]

<span>coordinate systems</span>

<img src="coordinates" alt="image" /> \[fig:coordinates\]

<span>boundaries</span>

-   In many systems, the boundaries are parallel to the coordinate system, but this is not always the case

<img src="noncoordinate" alt="image" /> \[fig:noncoordinate\]

<span>boundaries</span>

-   We often translate traction boundary conditions into stress boundary conditions using Cauchy’s Stress Theorem

-   When the condition is on a face parallel to the coordinate system, this gives a zero-stress condition
    *t*<sub>*j*</sub> = *σ*<sub>*i**j*</sub>*n*<sub>*i*</sub>

-   This results in *σ*<sub>*x**y*</sub> = *σ*<sub>*y**y*</sub> = 0

-   When the boundary is not parallel to the coordinate system, we do not necessarily have any zero-stress conditions
    $$\\begin{aligned}
            t\_x &= \\sigma\_x n\_x + \\tau\_{xy} n\_y = 0 \\\\
            t\_y &= \\tau\_{xy} n\_x + \\sigma\_y n\_y = 0 \\\\
            \\end{aligned}$$

<span>interfaces</span>

-   When we deal with multiple materials, we must prescribe conditions at the interface of these materials

-   Some common *interface conditions* are

    -   *Perfectly bonded interface* where displacements and tractions are continuous at the interface

    -   *Slip interface* where only normal displacements and tractions are continuous at the interface, with no tangential traction and potentially discontinuous tangential displacement

Stress Formulation
==================

<span>stress formulation</span>

-   For traction problems (i.e. traction is defined on all surfaces) it is convenient to re-formulate field equations in terms of stress only

-   Since displacements are eliminated, we will need to use the compatibility equations to ensure a continuous displacement field

-   It is desirable for this formulation to write the compatibility equations in terms of stress

<span>stress formulation</span>

-   We start by using Hooke’s law for each of the strain terms
    $$\\epsilon\_{ij} = \\frac{1+\\nu}{E}\\sigma\_{ij} - \\frac{\\nu}{E}\\sigma\_{kk} \\delta\_{ij}$$

-   After some tedious algebra, we find
    $$\\hspace{-1cm}
            \\sigma\_{ij,kk} + \\sigma\_{kk,ij} - \\sigma\_{ik,jk} - \\sigma\_{jk,ik} = \\frac{\\nu}{1+\\nu} (\\sigma\_{mm,kk}\\delta\_{ij} + \\sigma\_{mm,ij}\\delta\_{kk} - \\sigma\_{mm,jk}\\delta\_{ik} - \\sigma\_{mm,ik}\\delta\_{jk})$$

<span>stress formulation</span>

-   If we also include the equilibrium equations (*σ*<sub>*i**j*, *j*</sub> − *F*<sub>*i*</sub>) in the formulation, we find
    $$\\sigma\_{ij,kk} + \\frac{1}{1+\\nu}\\sigma\_{kk,ij} = \\frac{\\nu}{1+\\nu}\\sigma\_{mm,kk}\\delta\_{ij} - F\_{i,j} - F\_{j,i}$$

-   We can further simplify the equation by consider the case when *i* = *j* and nothing that
    $$\\sigma\_{ii,kk} = -\\frac{1+\\nu}{1-\\nu}F\_{i,i}$$

-   Which we can substitute into the equation to find
    $$\\sigma\_{ij,kk} + \\frac{1}{1+\\nu}\\sigma\_{kk,ij} = -\\frac{\\nu}{1+\\nu}\\delta\_{ij}F\_{k,k} - F\_{i,j} - F\_{j,i}$$

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

-   When working with traction boundary problems, these compatibility equations, together with the equilibrium equations, are sufficient to solve the problem

-   These partial differential equations are not easy to solve, and analytic problems approached this way are often solved only in 2D

-   Solutions are also commonly based on *stress functions*, which gives a base equation form that automatically satisfies equilibrium

<span>solution methods</span>

-   Direct method

    -   Solved via direction integration

    -   Limited to very simple geometries

-   Inverse method

    -   Choose a basic form for the solution based on our knowledge of the problem

    -   Solve for coefficients

    -   Usually we know the answer before we know the problem, it can be difficult to find useful problems for our solution

-   Semi-inverse method

    -   Only part of the solution is assumed

    -   Use direct integration to find the rest

Example
=======

<span>Levy’s problem</span>

-   Find the stresses in a semi-infinite wedge due to fluid pressure and its own self-weight

<img src="levee" alt="image" /> \[fig:levee\]

<span>Levy’s problem</span>

-   Since pressure varies linearly with depth, we will assume a linear state of stress
    $$\\begin{aligned}
            \\sigma\_{x} &= a\_1 x + b\_1 y + c\_1\\\\
            \\sigma\_{y} &= a\_2 x + b\_2 y + c\_2\\\\
            \\tau\_{xy} &= a\_{12}x + b\_{12} y + c\_{12}\\\\
            \\end{aligned}$$

-   This leaves 9 coefficients to be determined

<span>Levy’s problem</span>

-   First let us consider the boundary conditions at the apex of the dam

-   If we let the origin be at the apex of the dam, which must be traction free, we find
    *c*<sub>1</sub> = *c*<sub>2</sub> = *c*<sub>12</sub> = 0

<span>Levy’s problem</span>

-   Next let us consider the equilibrium equations
    $$\\begin{aligned}
            \\sigma\_{x,x} + \\tau\_{xy,y} + \\rho b\_x &= 0\\\\
            \\tau\_{xy,x} + \\sigma\_{y,y} + \\rho b\_y &= 0
            \\end{aligned}$$

-   Which in this case become
    $$\\begin{aligned}
            a\_1 + b\_{12} + 0 &= 0\\\\
            a\_{12} + b\_2 - \\rho g &= 0
            \\end{aligned}$$

<span>Levy’s problem</span>

-   The stresses can now be written as
    $$\\begin{aligned}
            \\sigma\_x &= a\_1 x + b\_1 y\\\\
            \\sigma\_y &= a\_2 x + b\_2 y\\\\
            \\tau\_{xy} &= -b\_2 x + \\rho g x - a\_1 y
            \\end{aligned}$$

<span>Levy’s problem</span>

-   The compatibility equations are all satisfied, as these linear functions will all go to zero when taking second derivatives

-   We now consider the boundary conditions along both faces


