&lt;handout:0&gt;

<img src="jimmy" alt="image" style="width:80.0%" />

&lt;handout:0&gt;

<img src="trickortreat" alt="image" style="width:30.0%" />

<span>upcoming schedule</span>

-   Nov 1 - Strain Energy

-   Nov 6 - Two - Dimensional Problems

-   Nov 8 - Two - Dimensional Problems, HW 6 Due

-   Nov 13 - SPTE, Two-Dimensional Problems

-   Nov 15 - Airy Stress Functions, HW 7 Due

### outline

\[sections numbered\]

Integral Theorems
=================

<span>clapeyron’s theorem</span>

-   If we return to the uniqueness derivation, the only non-general assumptions were
    $$\\begin{aligned}
            \\sigma\_{ij,j} &= 0\\\\
            T\_i^n &= \\sigma\_{ij}n\_j = 0 \\qquad \\text{Along traction boundary}\\\\
            u\_i &= 0 \\qquad \\text{Along displacement boundary} \\\\
            \\end{aligned}$$

-   This means that for any elastic body we can say
    2∫<sub>*V*</sub>*U**d**V* = ∫<sub>*S*</sub>*σ*<sub>*i**j*</sub>*n*<sub>*j*</sub>*u*<sub>*i*</sub>*d**S* − ∫<sub>*V*</sub>*σ*<sub>*i**j*, *j*</sub>*u*<sub>*i*</sub>*d**V*

<span>clapeyron’s theorem</span>

-   If we consider an elastic body in equilibrium, we can say that
    *σ*<sub>*i**j*, *j*</sub> = −*F*<sub>*i*</sub>

-   We also know by Cauchy’s stress theorem that
    *T*<sub>*i*</sub><sup>*n*</sup> = *σ*<sub>*i**j*</sub>*n*<sub>*j*</sub>

-   Both of these can be substituted to give
    2∫<sub>*V*</sub>*U**d**V* = ∫<sub>*S*</sub>*T*<sub>*i*</sub><sup>*n*</sup>*u*<sub>*i*</sub>*d**S* + ∫<sub>*V*</sub>*F*<sub>*i*</sub>*u*<sub>*i*</sub>*d**V*

-   This means that the strain energy is equal to half the work done by the body forces and surface tractions.

<span>betti/rayleigh reciprocal theorem</span>

-   We can derive another theorem by returning to
    2∫<sub>*V*</sub>*U**d**V* = ∫<sub>*S*</sub>*σ*<sub>*i**j*</sub>*n*<sub>*j*</sub>*u*<sub>*i*</sub>*d**S* − ∫<sub>*V*</sub>*σ*<sub>*i**j*, *j*</sub>*u*<sub>*i*</sub>*d**V*

-   Consider two different sets of forces and displacements acting on the same body
    *T*<sub>*i*</sub><sup>(1)</sup>, *F*<sub>*i*</sub><sup>(1)</sup>, *u*<sub>*i*</sub><sup>(1)</sup>and*T*<sub>*i*</sub><sup>(2)</sup>, *F*<sub>*i*</sub><sup>(2)</sup>, *u*<sub>*i*</sub><sup>(2)</sup>

<span>betti/rayleigh reciprocal theorem</span>

-   We now consider the work done by the forces in the first system acting through the displacements of the second system
    2∫<sub>*V*</sub>*U**d**V* = ∫<sub>*V*</sub>*σ*<sub>*i**j*</sub><sup>(1)</sup>*ϵ*<sub>*i**j*</sub><sup>(2)</sup> = ∫<sub>*S*</sub>*T*<sub>*i*</sub><sup>(1)</sup>*u*<sub>*i*</sub><sup>(2)</sup>*d**S* + ∫<sub>*V*</sub>*F*<sub>*i*</sub><sup>(1)</sup>*u*<sub>*i*</sub><sup>(2)</sup>*d**V*

-   We can similarly write
    ∫<sub>*V*</sub>*σ*<sub>*i**j*</sub><sup>(2)</sup>*ϵ*<sub>*i**j*</sub><sup>(1)</sup> = ∫<sub>*S*</sub>*T*<sub>*i*</sub><sup>(2)</sup>*u*<sub>*i*</sub><sup>(1)</sup>*d**S* + ∫<sub>*V*</sub>*F*<sub>*i*</sub><sup>(2)</sup>*u*<sub>*i*</sub><sup>(1)</sup>*d**V*

<span>betti/rayleigh reciprocal theorem</span>

-   We can now use Hooke’s Law and symmetry to say that
    *σ*<sub>*i**j*</sub><sup>(1)</sup>*ϵ*<sub>*i**j*</sub><sup>(2)</sup> = *C*<sub>*i**j**k**l*</sub>*ϵ*<sub>*k**l*</sub><sup>(1)</sup>*ϵ*<sub>*i**j*</sub><sup>(2)</sup> = *C*<sub>*k**l**i**j*</sub>*ϵ*<sub>*k**l*</sub><sup>(1)</sup>*ϵ*<sub>*i**j*</sub><sup>(2)</sup> = *ϵ*<sub>*k**l*</sub><sup>(1)</sup>*σ*<sub>*k**l*</sub><sup>(2)</sup>

-   If *σ*<sub>*i**j*</sub><sup>(1)</sup>*ϵ*<sub>*i**j*</sub><sup>(2)</sup> = *σ*<sub>*i**j*</sub><sup>(2)</sup>*ϵ*<sub>*i**j*</sub><sup>(1)</sup>, then we can also say that the strain energies are equivalent, proving the Betti/Rayleigh Reciprocal Theorem
    ∫<sub>*S*</sub>*T*<sub>*i*</sub><sup>(1)</sup>*u*<sub>*i*</sub><sup>(2)</sup>*d**S* + ∫<sub>*V*</sub>*F*<sub>*i*</sub><sup>(1)</sup>*u*<sub>*i*</sub><sup>(2)</sup>*d**V* = ∫<sub>*S*</sub>*T*<sub>*i*</sub><sup>(2)</sup>*u*<sub>*i*</sub><sup>(1)</sup>*d**S* + ∫<sub>*V*</sub>*F*<sub>*i*</sub><sup>(2)</sup>*u*<sub>*i*</sub><sup>(1)</sup>*d**V*

<!-- -->

-   The Betti/Rayleigh Reciprocal Theorem is used to derive the Integral Formulation of Elasticity

-   Also known as Somigliana’s Identity

-   Used for Boundary Element Method (BEM) and Boundary Integral Equation methods (BIE), but we will not use it in this class

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
            U\_T &= \\int\_0^L \\left\[\\iiint\_A \\frac{E}{2}\\left(\\frac{d^2 w}{dx^2}\\right)^2 y^2 dA \\right\] dx\\\\
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


