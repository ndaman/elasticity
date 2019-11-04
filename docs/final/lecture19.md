<span>upcoming schedule</span>

-   Nov 6 - Two - Dimensional Problems

-   Nov 8 - Two - Dimensional Problems, HW 6 Due

-   Nov 13 - SPTE, Two-Dimensional Problems

-   Nov 15 - Airy Stress Functions, HW 7 Due

### outline

\[sections numbered\]

Virtual Work
============

<span>virtual work</span>

-   The solution format we developed in Chapter 5 is known as *Strong Form*, and is not always a convenient solution form

-   We can use energy and work principles to develop additional solution methods

-   *Virtual Work* forms the basis for many of these methods

-   *Virtual Displacement* is a fictitious displacement such that the forces acting on the point remain unchanged

-   The work done by these forces is known as *Virtual Work*

<span>virtual work</span>

-   If we consider the elastic boundary-value problem, with tractions applied over the boundary *S*<sub>*t*</sub> and displacements applied over the boundary *S*<sub>*u*</sub>.

-   Virtual displacements denoted by *δ**u*<sub>*i*</sub> and are arbitrary, but cannot violate the displacement boundary condition, thus *δ**u*<sub>*i*</sub> = 0 on *S*<sub>*u*</sub>.

-   Virtual work done by surface and body forces can be written as
    *δ**W* = ∫<sub>*S*<sub>*t*</sub></sub>*T*<sub>*i*</sub><sup>*n*</sup>*δ**u*<sub>*i*</sub>*d**S* + ∫<sub>*V*</sub>*F*<sub>*i*</sub>*δ**u*<sub>*i*</sub>*d**V*

-   Since the virtual displacement is zero over *S*<sub>*u*</sub>, we can replace *S*<sub>*t*</sub> with *S* in the integral.
    *δ**W* = ∫<sub>*S*</sub>*T*<sub>*i*</sub><sup>*n*</sup>*δ**u*<sub>*i*</sub>*d**S* + ∫<sub>*V*</sub>*F*<sub>*i*</sub>*δ**u*<sub>*i*</sub>*d**V*

<span>virtual work</span>

-   We can follow the procedure from the uniqueness derivation in reverse
    $$\\begin{aligned}
            \\delta W &= \\int\_{S} T\_i^n \\delta u\_i dS + \\int\_V F\_i \\delta u\_i dV\\\\
            &= \\int\_{S} \\sigma\_{ij}n\_j \\delta u\_i dS + \\int\_V F\_i \\delta u\_i dV\\\\
            &= \\int\_V (\\sigma\_{ij}\\delta u\_i)\_{,j} dV + \\int\_V F\_i \\delta u\_i dV\\\\
            &= \\int\_V (\\sigma\_{ij,j}\\delta u\_i + \\sigma\_{ij}\\delta u\_{i,j}) dV + \\int\_V F\_i \\delta u\_i dV\\\\
            &= \\int\_V (-F\_i\\delta u\_i + \\sigma\_{ij}(\\delta \\epsilon\_{ij} + \\delta\\omega\_{ij})) dV + \\int\_V F\_i \\delta u\_i dV\\\\
            &= \\int\_V \\sigma\_{ij}\\delta \\epsilon\_{ij} dV
            \\end{aligned}$$

-   Notice that this gives the usual strain energy relationship, but without the factor of one-half.

-   This is because stress is constant during virtual displacement

<span>virtual work</span>

-   The virtual strain energy follows the same relationships developed previously, namely
    ∫<sub>*V*</sub>*δ**U* = ∫<sub>*S*</sub>*T*<sub>*i*</sub><sup>*n*</sup>*δ**u*<sub>*i*</sub> + ∫<sub>*V*</sub>*F*<sub>*i*</sub>*δ**u*<sub>*i*</sub>*d**V*

-   Because the external forces are unchanged during the virtual displacement, the *δ* operator can be placed outside the integrals.

-   We can also move all terms to the same side of the equation to write
    *δ*(∫<sub>*V*</sub>*U*−∫<sub>*S*</sub>*T*<sub>*i*</sub><sup>*n*</sup>*u*<sub>*i*</sub>−∫<sub>*V*</sub>*F*<sub>*i*</sub>*u*<sub>*i*</sub>*d**V*) = 0

-   Or, written in terms of virtual work
    *δ*(*U*<sub>*T*</sub> − *W*)=0

<span>virtual work</span>

-   The total potential energy of an elastic solid is (*U*<sub>*T*</sub> − *W*), and must be zero for a virtual displacement

-   These results are completely general, and apply to both linear and non-linear materials

-   Special theories for rods, beams, plates, and shells use this principle

-   Finite elements is also developed using virtual work

-   We can even use virtual work to re-derive the continuum results we found previously

<span>virtual work</span>

-   If we start with this form
    ∫<sub>*V*</sub>*σ*<sub>*i**j*</sub>*δ**ϵ*<sub>*i**j*</sub>*d**V* − ∫<sub>*S*</sub>*T*<sub>*i*</sub><sup>*n*</sup>*δ**u*<sub>*i*</sub>*d**S* − ∫<sub>*V*</sub>*F*<sub>*i*</sub>*δ**u*<sub>*i*</sub>*d**V* = 0

-   We can replace the first term by writing it as
    *σ*<sub>*i**j*</sub>*δ**ϵ*<sub>*i**j*</sub> = *σ*<sub>*i**j*</sub>*δ**u*<sub>*i*, *j*</sub> = (*σ*<sub>*i**j*</sub>*δ**u*<sub>*i*</sub>)<sub>,*j*</sub> − *σ*<sub>*i**j*, *j*</sub>*δ**u*<sub>*i*</sub>

-   Which leads to
    ∫<sub>*V*</sub>\[(*σ*<sub>*i**j*</sub>*δ**u*<sub>*i*</sub>)<sub>,*j*</sub> − *σ*<sub>*i**j*, *j*</sub>*δ**u*<sub>*i*</sub>\]*d**V* − ∫<sub>*S*</sub>*T*<sub>*i*</sub><sup>*n*</sup>*δ**u*<sub>*i*</sub>*d**S* − ∫<sub>*V*</sub>*F*<sub>*i*</sub>*δ**u*<sub>*i*</sub>*d**V* = 0

<span>virtual work</span>

-   We can use the divergence theorem to say that
    ∫<sub>*V*</sub>(*σ*<sub>*i**j*</sub>*δ**u*<sub>*i*</sub>)<sub>,*j*</sub>*d**V* = ∫<sub>*S*</sub>*σ*<sub>*i**j*</sub>*n*<sub>*j*</sub>*δ**u*<sub>*i*</sub>*d**S*

-   This gives
    ∫<sub>*V*</sub>\[*σ*<sub>*i**j*, *j*</sub> + *F*<sub>*i*</sub>\]*δ**u*<sub>*i*</sub>*d**V* + ∫<sub>*S*</sub>(*T*<sub>*i*</sub><sup>*n*</sup> − *σ*<sub>*i**j*</sub>*n*<sub>*j*</sub>)*δ**u*<sub>*i*</sub>*d**S* = 0

-   This will be satisfied if
    *σ*<sub>*i**j*, *j*</sub> + *F*<sub>*i*</sub> = 0(equilibrium)

-   And either
    *δ**u*<sub>*i*</sub> = 0(displacement boundary)

-   Or
    *T*<sub>*i*</sub><sup>*n*</sup> = *σ*<sub>*i**j*</sub>*n*<sub>*j*</sub>(traction boundary)

Ritz Method
===========

<span>ritz method</span>

-   While we have showed previously how virtual work can be used to develop analytic solutions, it is also convenient for approximate solutions

-   The Rayleigh-Ritz Method is an important approximate technique based on this method

-   In this method, trial functions are used as approximate solutions which satisfy the boundary conditions, but not necessarily the differential equations.

<span>ritz method</span>

-   For the elasticity displacement formulation, trial functions take the form
    $$\\begin{aligned}
            u &= u\_0 + \\sum\_{j=1}^{N}a\_ju\_j\\\\
            v &= v\_0 + \\sum\_{j=1}^{N}b\_jv\_j\\\\
            w &= w\_0 + \\sum\_{j=1}^{N}c\_jw\_j\\\\
            \\end{aligned}$$

-   The unknown constants are chosen to minimize the total potential energy.

<span>ritz method</span>

-   To minimize the total potential energy
    $$\\begin{aligned}
            \\frac{\\partial \\Pi}{\\partial a\_j} &= 0\\\\
            \\frac{\\partial \\Pi}{\\partial b\_j} &= 0\\\\
            \\frac{\\partial \\Pi}{\\partial c\_j} &= 0\\\\
            \\end{aligned}$$

-   The Ritz method is often used for simple shapes (rods, beams, plates, shells) where we typically only consider one component of the displacement.

<span>example</span>

; ; (0,0) – (3,0); \[90\]; \[270\];

<span>example</span>

-   We recall that the total potential energy is
    *Π* = *U*<sub>*T*</sub> − *W*

-   In a simple (Euler-Bernoulli) beam, we assume that the stress is a function of the vertical displacement, *w* and the cross-sectional area

-   All stress terms other than *σ*<sub>11</sub> are zero

<span>example</span>

-   The strain energy density is
    $$U = \\frac{\\sigma\_{11}^2}{2E} = \\frac{M^2 y^2}{2EI^2} = \\frac{E}{2}\\left(\\frac{d^2 w}{dx^2}\\right)^2 y^2$$

-   We integrate over the volume to find the total strain energy in the beam
    $$\\begin{aligned}
            U\_T &= \\int\_0^L \\left\[\\iint\_A \\frac{E}{2}\\left(\\frac{d^2 w}{dx^2}\\right)^2 y^2 dA \\right\] dx\\\\
            &= \\int\_0^L \\frac{EI}{2}\\left(\\frac{d^2 w}{dx^2}\\right)^2 dx
            \\end{aligned}$$

<span>example</span>

-   The work done by external forces is quite simple in this case
    *W* = *P**w*(*L*)

-   We now consider a trial function for *w*, let us consider a polynomial function
    $$w = a\_0 + a\_1 \\left(\\frac{x}{L}\\right) + a\_2 \\left(\\frac{x}{L}\\right)^2$$

<span>example</span>

-   We first ensure the trial solution satisfies the essential boundary conditions
    $$\\begin{aligned}
            w(0) &= 0\\\\
            0 &= a\_0 + a\_1 \\left(\\frac{0}{L}\\right) + a\_2 \\left(\\frac{0}{L}\\right)^2
            \\end{aligned}$$

-   And
    $$\\begin{aligned}
            \\frac{d w(0)}{dx} &= 0\\\\
            0 &= a\_1 \\left(\\frac{1}{L}\\right) + 2 a\_2 \\left(\\frac{0}{L}\\right)
            \\end{aligned}$$

<span>example</span>

-   This gives *a*<sub>0</sub> = *a*<sub>1</sub> = 0

-   *a*<sub>2</sub> is to be determined

-   The total potential energy is
    $$\\Pi = U\_t - W = \\int\_0^L \\frac{EI}{2}\\left(\\frac{d^2 w}{dx^2}\\right)^2 dx - Pw(L)$$

-   After differentiation and substitution, we find
    $$\\Pi = \\frac{EI}{2} \\int\_0^L \\left(\\frac{2a\_2}{L^2}\\right)^2 dx - Pa\_2$$

<span>example</span>

-   We minimize the potential energy by letting $\\frac{\\partial \\Pi}{\\partial a\_j} = 0$
    $$\\begin{aligned}
            \\Pi &= \\frac{2EI a\_2^2}{L^3} - Pa\_2\\\\
            \\frac{\\partial \\Pi}{\\partial a\_2} &= \\frac{4EIa\_2}{L^3} - P = 0\\\\
            a\_2 &= \\frac{PL^3}{4EI}
            \\end{aligned}$$

-   Thus our approximate solution is
    $$w = \\frac{PL}{4EI}x^2$$

<span>example</span>

-   A simple cantilever beam of this form can be solved for exactly

-   The exact solution is
    $$w = \\frac{Px^2}{6EI}(3L-x)$$

<span>example</span>

<img src="ritz1" alt="image" /> \[fig:ritz1\]

<span>example</span>

-   If we considered one more term in our trial, we would have recovered the exact solution

-   In this case, more terms would be redundant

-   We could have also considered a trigonometric function

Two-Dimensional Problems
========================

<span>2d problems</span>

-   As we learned in Chapter 5, it is often very difficult to solve full problems in 3D

-   Some problems contain symmetry, or particular geometries which allow certain simplifications to be made

-   In this chapter we will consider the following 2D formulations

    -   Plane strain

    -   Plane stress

    -   Generalized plane stress

    -   Antiplane strain

<span>2d problems</span>

-   Airy stress functions provide a systematic method for solving 2D problems

-   We will also develop Airy stress function solution methods in polar (cylindrical or spherical) coordinates

Plane Strain
============

<span>plane strain</span>

-   Plane strain is a state we consider for very long bodies

-   If the body is sufficiently long, then the deformation field can be considered to be a function of *x* and *y* only
    $$\\begin{aligned}
            u &= u(x,y)\\\\
            v &= v(x,y)\\\\
            w &= 0
            \\end{aligned}$$

-   Results will be the same at every cross-section, so we may consider only a 2D cross-section

<span>plane strain</span>

-   We can use the strain-displacement relations to find the corresponding strains from our assumptions on the displacement
    $$\\begin{aligned}
            \\epsilon\_{xx} &= \\frac{\\partial u}{\\partial x}\\\\
            \\epsilon\_{yy} &= \\frac{\\partial v}{\\partial y}\\\\
            \\epsilon\_{xy} &= \\frac{1}{2}\\left(\\frac{\\partial u}{\\partial y} + \\frac{\\partial v}{\\partial x}\\right)\\\\
            \\epsilon\_{zz} &= \\epsilon\_{xz} = \\epsilon\_{yz} = 0
            \\end{aligned}$$

<span>plane strain</span>

-   We can use Hooke’s law to find the stresses
    $$\\begin{aligned}
            \\sigma\_{xx} &= \\lambda(\\epsilon\_{xx} + \\epsilon\_{yy}) + 2\\mu \\epsilon\_{xx}\\\\
            \\sigma\_{yy} &= \\lambda(\\epsilon\_{xx} + \\epsilon\_{yy}) + 2\\mu \\epsilon\_{yy}\\\\
            \\sigma\_{zz} &= \\lambda(\\epsilon\_{xx} + \\epsilon\_{yy})\\\\
            \\tau\_{xy} &= 2\\mu \\epsilon\_{xy} \\\\
            \\tau\_{xz} &= \\tau\_{yz} = 0
            \\end{aligned}$$

<span>plane strain</span>

-   We can use these relationships to reduce the equilibrium equations.

-   Recall that for equilibrium we have
    *σ*<sub>*i**j*, *j*</sub> + *F*<sub>*i*</sub> = 0

-   *τ*<sub>*x**z*</sub> = *τ*<sub>*y**z*</sub> = 0, so those terms will vanish

-   Although *σ*<sub>*z**z*</sub> ≠ 0, it only appears with a derivative of *z*, and it is a function of *x* and *y* only, so *σ*<sub>*z**z*</sub> will not appear in any non-trivial equilibrium equation
    $$\\begin{aligned}
            \\frac{\\partial \\sigma\_{xx}}{\\partial x} + \\frac{\\partial \\tau\_{xy}}{\\partial y} + F\_x &= 0\\\\
            \\frac{\\partial \\tau\_{xy}}{\\partial x} +\\frac{\\partial \\sigma\_{yy}}{\\partial y} +  F\_y &= 0
            \\end{aligned}$$

<span>plane strain</span>

-   We can use the strain-displacement equations and Hooke’s Law to write Navier’s equations for plane strain
    $$\\begin{aligned}
            \\mu \\nabla^2 u + (\\lambda + \\mu) \\frac{\\partial}{\\partial x} \\left(\\frac{\\partial u}{\\partial x} + \\frac{\\partial v}{\\partial y}\\right) + F\_x &= 0\\\\
            \\mu \\nabla^2 v + (\\lambda + \\mu) \\frac{\\partial}{\\partial y} \\left(\\frac{\\partial u}{\\partial x} + \\frac{\\partial v}{\\partial y}\\right) + F\_x &= 0
            \\end{aligned}$$

<span>plane strain</span>

-   We can also reduce the compatibility equations
    $$\\begin{aligned}
            \\frac{\\partial^2 \\epsilon\_x}{\\partial y^2} + \\frac{\\partial^2 \\epsilon\_y}{\\partial x^2} &= 2\\frac{\\partial^2 \\epsilon\_{xy}}{\\partial x \\partial y}\\\\
            \\frac{\\partial^2 \\epsilon\_y}{\\partial z^2} + \\frac{\\partial^2 \\epsilon\_z}{\\partial y^2} &= 2\\frac{\\partial^2 \\epsilon\_{yz}}{\\partial y \\partial z}\\\\
            \\frac{\\partial^2 \\epsilon\_z}{\\partial x^2} + \\frac{\\partial^2 \\epsilon\_x}{\\partial z^2} &= 2\\frac{\\partial^2 \\epsilon\_{zx}}{\\partial z \\partial x}\\\\
            \\frac{\\partial^2 \\epsilon\_x}{\\partial y \\partial z} &= \\frac{\\partial}{\\partial x} \\left(-\\frac{\\partial \\epsilon\_{yz}}{\\partial x} + \\frac{\\partial \\epsilon\_{zx}}{\\partial y} + \\frac{\\partial \\epsilon\_{xy}}{\\partial z}\\right)\\\\
            \\frac{\\partial^2 \\epsilon\_y}{\\partial z \\partial x} &= \\frac{\\partial}{\\partial y} \\left(-\\frac{\\partial \\epsilon\_{zx}}{\\partial y} + \\frac{\\partial \\epsilon\_{xy}}{\\partial z} + \\frac{\\partial \\epsilon\_{yz}}{\\partial x}\\right)\\\\
            \\frac{\\partial^2 \\epsilon\_z}{\\partial x \\partial y} &= \\frac{\\partial}{\\partial z} \\left(-\\frac{\\partial \\epsilon\_{xy}}{\\partial z} + \\frac{\\partial \\epsilon\_{yz}}{\\partial x} + \\frac{\\partial \\epsilon\_{zx}}{\\partial y}\\right)
            \\end{aligned}$$

<span>plane strain</span>

-   The only non-trivial term from the compatibility equations is
    $$\\frac{\\partial^2 \\epsilon\_x}{\\partial y^2} + \\frac{\\partial^2 \\epsilon\_y}{\\partial x^2} = 2\\frac{\\partial^2 \\epsilon\_{xy}}{\\partial x \\partial y}$$

-   This can also be written in terms of stress (Beltrami-Mitchell)
    $$\\nabla^2(\\sigma\_x + \\sigma\_y) = -\\frac{1}{1-\\nu}\\left(\\frac{\\partial F\_x}{\\partial x} + \\frac{\\partial F\_y}{\\partial y}\\right)$$

<span>plane strain</span>

-   Plane strain is exact for a body of infinite length, but can also be useful for real shapes of finite length

-   Consider a long body with fixed and frictionless ends.

-   The boundary conditions for this case are
    $$\\begin{aligned}
            w(x,y,\\pm L) &= 0\\\\
            \\tau\_{xz}(x,y,\\pm L) &= 0\\\\
            \\tau\_{yz}(x,y,\\pm L) &= 0
            \\end{aligned}$$

-   Which give the same results as the infinite body plane strain assumptions

-   When the ends are not “fixed and frictionless” we can use Saint-Venants principle to apply plane strain in an approximate sense

Plane Stress
============

<span>plane stress</span>

-   If the thickness of a body is small compared to the other dimensions, we assume that there can not be much variation in any of the stress components in that direction

-   The assumptions for plane stress can be summarized as
    $$\\begin{aligned}
            \\sigma\_x &= \\sigma\_x(x,y)\\\\
            \\sigma\_y &= \\sigma\_y(x,y)\\\\
            \\tau\_{xy} &= \\tau\_{xy}(x,y)\\\\
            \\sigma\_z &= \\tau\_{xz} = \\tau\_{yz} = 0
            \\end{aligned}$$

-   To maintain these assumptions, there can be no body forces in the *z*-direction and no applied tractions in the *z*-direction.

-   Other body forces must be independent of *z*, or distributed symmetrically such that the average may be used.

<span>plane stress</span>

-   We can use Hooke’s law to find the corresponding values of strain
    $$\\begin{aligned}
            \\epsilon\_x &= \\frac{1}{E}(\\sigma\_x - \\nu \\sigma\_y)\\\\
            \\epsilon\_y &= \\frac{1}{E}(\\sigma\_y - \\nu \\sigma\_x)\\\\
            \\epsilon\_z &= -\\frac{\\nu}{E}(\\sigma\_x + \\sigma\_y)\\\\
            \\epsilon\_{xy} &= \\frac{1+\\nu}{E}\\tau\_{xy}\\\\
            \\epsilon\_{xz} &= \\epsilon\_{yz} = 0
            \\end{aligned}$$

<span>plane stress</span>

-   We can now find the displacements using the strain-displacement relationships
    $$\\begin{aligned}
            \\epsilon\_{x} &= \\frac{\\partial u}{\\partial x}\\\\
            \\epsilon\_{y} &= \\frac{\\partial v}{\\partial y}\\\\
            \\epsilon\_{z} &= \\frac{\\partial w}{\\partial z}\\\\
            \\epsilon\_{xy} &= \\frac{1}{2}\\left(\\frac{\\partial u}{\\partial y} + \\frac{\\partial v}{\\partial x}\\right)\\\\
            \\epsilon\_{yz} &= \\frac{1}{2}\\left(\\frac{\\partial v}{\\partial z} + \\frac{\\partial w}{\\partial y}\\right) = 0\\\\
            \\epsilon\_{xz} &= \\frac{1}{2}\\left(\\frac{\\partial u}{\\partial z} + \\frac{\\partial w}{\\partial x}\\right) = 0\\\\
            \\end{aligned}$$

<span>plane stress</span>

-   Since strain in the *z*-direction is not zero, *w* becomes a linear function of *z*

-   We also find that *u* and *v* will also be functions of *z*

-   These effects are normally neglected, leading to an approximation in the formulation

-   This is why we cannot use the full 3D compatibility equations to assess compatibility of a body with an assumed state of plane stress

<span>plane stress</span>

-   The equilibrium equations reduce the same form in plane stress as they did for plane strain
    $$\\begin{aligned}
            \\frac{\\partial \\sigma\_{xx}}{\\partial x} + \\frac{\\partial \\tau\_{xy}}{\\partial y} + F\_x &= 0\\\\
            \\frac{\\partial \\tau\_{xy}}{\\partial x} +\\frac{\\partial \\sigma\_{yy}}{\\partial y} +  F\_y &= 0
            \\end{aligned}$$

-   But the Navier equations in terms of displacement do not reduce to exactly the same form
    $$\\begin{aligned}
            \\mu \\nabla^2 u + \\frac{E}{2(1-\\nu)} \\frac{\\partial}{\\partial x} \\left(\\frac{\\partial u}{\\partial x} + \\frac{\\partial v}{\\partial y}\\right) + F\_x &= 0\\\\
            \\mu \\nabla^2 v + \\frac{E}{2(1-\\nu)} \\frac{\\partial}{\\partial y} \\left(\\frac{\\partial u}{\\partial x} + \\frac{\\partial v}{\\partial y}\\right) + F\_y &= 0
            \\end{aligned}$$

<span>navier equations</span>

-   The factor in the plane strain Navier equations is
    (*λ* + *μ*)

-   We can convert this to *E*, *ν* to better compare with the plane stress equation
    $$\\begin{aligned}
            \\lambda + \\mu &= \\frac{\\nu E}{(1+\\nu)(1-2\\nu)} + \\frac{E}{2(1+\\nu)}\\\\
            &= \\frac{2\\nu E}{2(1+\\nu)(1-2\\nu)} + \\frac{E(1-2\\nu)}{2(1+\\nu)(1-2\\nu)}\\\\
            &= \\frac{2\\nu E + E - 2\\nu E}{2(1+\\nu)(1-2\\nu)}\\\\
            &= \\frac{E}{2(1+\\nu)(1-2\\nu)}
            \\end{aligned}$$

<span>compatibility</span>

-   Due to the approximations we made earlier, we neglect all compatibility equations with *ϵ*<sub>*z*</sub>, even though these may not be zero
    $$\\frac{\\partial^2 \\epsilon\_x}{\\partial y^2} + \\frac{\\partial^2 \\epsilon\_y}{\\partial x^2} = 2 \\frac{\\partial^2 \\epsilon\_{xy}}{\\partial x \\partial y}$$

-   or in terms of stress
    $$\\nabla^2 (\\sigma\_{xx} + \\sigma\_{yy}) = -(1+\\nu)\\left(\\frac{\\partial F\_x}{\\partial x} + \\frac{\\partial F\_y}{\\partial y}\\right)$$

<span>conversion</span>

-   While plane strain and plane stress give similar results, they are not identical

-   We can convert between plane strain and plane stress by replacing *E* and *ν*

    |                              |               *E*              |         *ν*         |
    |:----------------------------:|:------------------------------:|:-------------------:|
    | Plane stress to plane strain |      $\\frac{E}{1-\\nu^2}$     | $\\frac{v}{1-\\nu}$ |
    | Plane strain to plane stress | $\\frac{E(1+2\\nu)}{1+\\nu^2}$ | $\\frac{v}{1+\\nu}$ |

    \[tab:addlabel\]

-   When *ν* = 0, plane strain and plane stress give identical results

Generalized Plane Stress
========================

<span>generalized plane stress</span>

-   Some approximations introduced inconsistencies in the plane stress formulation

-   We can formulate plane stress problems in an alternate fashion to avoid these inconsistencies

-   Generalized plane stress is based on averaging the field quantities through the thickness
    $$\\bar{\\psi} = \\frac{1}{2h} \\int\_{-h}^{h}\\psi (x,y,z) dz$$

<span>generalized plane stress</span>

-   We again assume that the thickness, 2*h*, is much smaller than the other dimensions

-   We also assume that tractions on the surfaces *z* = ±*h* are zero

-   Edge loadings must have no *z* component and are independent of *z*

-   Body forces also cannot have a *z* component and must be independent of *z* or symmetrically distributed through the thickness

-   As in plane stress, this will give *w* as a linear function of *z* which means
    *w*(*x*, *y*, *z*)= − *w*(*x*, *y*, −*z*)

<span>generalized plane stress</span>

-   If we take the average value of all field variables we find
    $$\\begin{aligned}
            \\bar{u} &= \\bar{u}(x,y)\\\\
            \\bar{v} &= \\bar{v}(x,y)\\\\
            \\bar{w} &= \\bar{w}(x,y)\\\\
            \\bar{\\sigma\_z} &= \\bar{\\tau\_{xz}} = \\bar{\\tau\_{yz}} = 0\\\\
            \\bar{\\sigma\_x} &= \\lambda^\*(\\bar{\\epsilon\_x}+\\bar{\\epsilon\_y}) + 2\\mu \\bar{\\epsilon\_x}\\\\
            \\bar{\\sigma\_y} &= \\lambda^\*(\\bar{\\epsilon\_x}+\\bar{\\epsilon\_y}) + 2\\mu \\bar{\\epsilon\_y}\\\\
            \\bar{\\tau\_{xy}} &= 2\\mu \\bar{\\epsilon\_{xy}}\\\\
            \\bar{\\epsilon\_z} &= - \\frac{\\lambda}{\\lambda + 2\\mu} (\\bar{\\epsilon\_x}+ \\bar{\\epsilon\_y})
            \\end{aligned}$$

-   Where $\\lambda^\* = \\frac{2\\lambda \\mu}{\\lambda + 2\\mu}$

<span>generalized plane stress</span>

-   We can also write the equilibrium equations in terms of the averaged values
    $$\\begin{aligned}
            \\frac{\\partial \\bar{\\sigma\_x}}{\\partial x} + \\frac{\\partial \\bar{\\tau\_{xy}}}{\\partial x} + \\bar{F}\_x &= 0\\\\
            \\frac{\\partial \\bar{\\tau\_{xy}}}{\\partial x} + \\frac{\\partial \\bar{\\sigma\_{y}}}{\\partial y} + \\bar{F}\_y &= 0
            \\end{aligned}$$

-   Or in terms of displacements
    $$\\begin{aligned}
            \\mu \\nabla^2 \\bar{u} + (\\lambda^\* + \\mu) \\frac{\\partial}{\\partial x} \\left(\\frac{\\partial \\bar{u}}{\\partial x} + \\frac{\\partial \\bar{v}}{\\partial y}\\right) + \\bar{F}\_x &= 0\\\\
            \\mu \\nabla^2 \\bar{u} + (\\lambda^\* + \\mu) \\frac{\\partial}{\\partial y} \\left(\\frac{\\partial \\bar{u}}{\\partial x} + \\frac{\\partial \\bar{v}}{\\partial y}\\right) + \\bar{F}\_y &= 0
            \\end{aligned}$$

<span>compatibility</span>

-   The compatibility relations reduce to
    $$\\nabla^2 (\\bar{\\sigma\_x} + \\bar{\\sigma\_y}) = - \\frac{2(\\lambda^\* + \\mu)}{\\lambda^\* + 2\\mu} \\left(\\frac{\\partial \\bar{F}\_x}{\\partial x} + \\frac{\\partial \\bar{F}\_y}{\\partial y}\\right)$$

-   When we write the coefficient $\\frac{2(\\lambda^\* + \\mu)}{\\lambda^\* + 2\\mu}$ in terms of *E* and *ν*, we find
    $$\\frac{2(\\lambda^\* + \\mu)}{\\lambda^\* + 2\\mu} = 1 + \\nu$$

-   Which means this is an identical result to the simple plane stress derivation

-   Thus the generalized plane stress method is not particularly useful

<span>beam example</span>

<img src="../Figures/figure_1" alt="Displacement for beam under pure bending" />
