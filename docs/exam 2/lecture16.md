# AE731
## Theory of Elasticity
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering
October 21, 2019

----
## upcoming schedule

-   Oct 21 - Solution Strategies
-   Oct 23 - Exam 2 Review, HW 5 Due
-   Oct 28 - Exam 2 
-   Oct 30 - SPTE, Strain Energy

----
## outline

<!-- vim-markdown-toc GFM -->

* exam
* stress and equilibrium
* material behavior
* problem formulation

<!-- vim-markdown-toc -->

---
# exam

----
## exam format

-   Similar format to last exam
-   Three problems
-   Focus on organizing your work clearly to maximize partial credit

---
# stress and equilibrium

----
## topics

-   Traction
-   Stress transformation
-   Principal stress
-   Equilibrium

----
## derivations

-   Cauchy’s stress theorem
-   Max shear stress for plane stress
-   Mohr’s circle

----
## stress tensor

-   To simplify the notation, we introduce the stress tensor

$$\\sigma\_{ij} = t\_j^{(\\hat{e}\_i)}$$

(0,0,0) – (2,0,0); (2,0,0) – (2,2,0) – (0,2,0); (0,2,0) – (0,0,0); (0,0,2) – (2,0,2) – (2,2,2) – (0,2,2) – (0,0,2); (2,0,0) – (2,0,2); (2,2,0) – (2,2,2); (0,2,0) – (0,2,2); (0,0,0) – (0,0,2); (1,1,2) – (1,1,3) node\[above\] ----
## *σ*<sub>33</sub></span>; (1,1,2) – (2,1,2) node\[above\] <span>*σ*<sub>31</sub></span>; (1,1,2) – (1,2,2) node\[above\] <span>*σ*<sub>32</sub></span>; (2,1,1) – (3,1,1) node\[left\] <span>*σ*<sub>11</sub></span>; (2,1,1) – (2,1,2) node\[below left\] <span>*σ*<sub>13</sub></span>; (2,1,1) – (2,2,1) node\[above left\] <span>*σ*<sub>12</sub></span>; (1,2,1) – (1,3,1) node\[right\] <span>*σ*<sub>22</sub></span>; (1,2,1) – (2,2,1) node at (1.5,2,1.3) <span>*σ*<sub>21</sub></span>; (1,2,1) – (1,2,2) node\[below right\] <span>*σ*<sub>23</sub>;

----
## traction

-   We can find some interesting information about the traction vector by considering an arbitrary tetrahedron with some traction $\\hat{t}^{(n)}$ applied to the surface

    (2,0,0) – (3,0,0) node\[below left\] ----
## *x*<sub>1</sub></span>; (0,1.5,0) – (0,3,0) node\[right\] <span>*x*<sub>2</sub></span>; (0,0,1.5) – (0,0,3) node\[above\] <span>*x*<sub>3</sub></span>; (2,0,0) – (0,0,0) – (0,1.5,0); (0,0,0) – (0,0,1.5); (2,0,0) – (0,1.5,0) – (0,0,1.5) – (2,0,0); (1,.75,.75) – (2,1.5,1.5) node\[above\] <span>$\\hat{n}$</span>; (1,.75,.75) – (1,2,1) node \[right\] <span>$\\hat{t}^{(n)}$;

----
## traction

-   If we consider the balance of forces in the *x*<sub>1</sub>-direction
    *t*<sub>1</sub>*d**A* − *σ*<sub>11</sub>*d**A*<sub>1</sub> − *σ*<sub>21</sub>*d**A*<sub>2</sub> − *σ*<sub>31</sub>*d**A*<sub>3</sub> + *b*<sub>1</sub>*ρ**d**V* = 0

-   The area components are:
    $$\\begin{aligned}
            dA\_1 &= n\_1 dA\\\\
            dA\_2 &= n\_2 dA\\\\
            dA\_3 &= n\_3 dA\\\\
            \\end{aligned}$$

-   And $dV = \\frac{1}{3}h dA$.

----
## traction
$$t\_1 dA - \\sigma\_{11} n\_1 dA - \\sigma\_{21} n\_2 dA - \\sigma\_{31} n\_3 dA + b\_1 \\rho \\frac{1}{3}h dA = 0$$

-   If we let *h* → 0 and divide by *d**A*
    *t*<sub>1</sub> = *σ*<sub>11</sub>*n*<sub>1</sub> + *σ*<sub>21</sub>*n*<sub>2</sub> + *σ*<sub>31</sub>*n*<sub>3</sub>

-   We can write this in index notation as
    *t*<sub>1</sub> = *σ*<sub>*i*1</sub>*n*<sub>*i*</sub>

-   We find, similarly
    $$\\begin{aligned}
            t\_2 &= \\sigma\_{i2} n\_i\\\\
            t\_3 &= \\sigma\_{i3} n\_i\\\\
            \\end{aligned}$$

----
## traction

-   We can further combine these results in index notation as
    *t*<sub>*j*</sub> = *σ*<sub>*i**j*</sub>*n*<sub>*i*</sub>

-   This means with knowledge of the nine components of *σ*<sub>*i**j*</sub>, we can find the traction vector at any point on any surface

----
## maximum shear stress

-   For plane stress problems, we can also use the stress transformation equations to find the maximum shear stress

-   We desire to maximize this equation:
    $$\\tau^\\prime\_{xy} = \\frac{\\sigma\_y - \\sigma\_x}{2}\\sin 2\\theta + \\tau\_{xy} \\cos 2\\theta$$

----
## maximum shear stress

-   Taking the derivative with respect to *θ* gives
    $$\\frac{\\partial}{\\partial \\theta} (\\tau^\\prime\_{xy}) = (\\sigma\_y-\\sigma\_x)\\cos 2\\theta - 2\\tau\_{xy} \\sin 2\\theta = 0$$

-   Which we can use to find 2*θ*
    $$2\\theta = \\tan ^{-1} \\left(\\frac{(\\sigma\_y-\\sigma\_x)}{2\\tau\_{xy}}\\right)$$

----
## maximum shear stress

-   Substituting back into the original equation gives
    $$\\tau^\\prime\_{max} = \\frac{\\sigma\_y - \\sigma\_x}{2}\\sin \\left\[\\tan ^{-1} \\left(\\frac{(\\sigma\_y-\\sigma\_x)}{2\\tau\_{xy}}\\right)\\right\] + \\tau\_{xy} \\cos \\left\[\\tan ^{-1} \\left(\\frac{(\\sigma\_y-\\sigma\_x)}{2\\tau\_{xy}}\\right)\\right\]$$

-   Note that
    $$\\begin{aligned}
            \\sin (\\tan ^{-1} (x)) &= \\frac{x}{\\sqrt{1+x^2}}\\\\
            \\cos (\\tan ^{-1} (x)) &= \\frac{1}{\\sqrt{1+x^2}}\\\\
            \\end{aligned}$$

----
## maximum shear stress

-   We note that
    $$\\sqrt{1+ \\left(\\frac{\\sigma\_y - \\sigma\_x}{2 \\tau\_{xy}}\\right)^2} = \\frac{\\sqrt{(\\sigma\_y-\\sigma\_x)^2+4\\tau\_{xy}^2}}{2\\tau\_{xy}}$$

-   And thus we find
    $$\\tau\_{max} = \\frac{(\\sigma\_y-\\sigma\_x)^2}{2 \\sqrt{(\\sigma\_y-\\sigma\_x)^2+4\\tau\_{xy}^2}} + \\frac{4\\tau\_{xy}^2}{2 \\sqrt{(\\sigma\_y-\\sigma\_x)^2+4\\tau\_{xy}^2}}$$

----
## maximum shear stress

-   Adding the terms and simplifying, we find
    $$\\tau\_{max} = \\sqrt{\\left(\\frac{\\sigma\_y-\\sigma\_x}{2}\\right)^2+\\tau\_{xy}^2}$$

----
## tractions

-   We can use what we know about principal values to find some interesting things about the tractions

-   Consider the traction vector on an arbitrary internal face, and decompose into Normal and Shear components.

    <img src="potato" alt="image" /> \[fig:potato\]

----
## tractions

-   The normal component can be found using the dot product
    $$N = \\hat{T}^n \\cdot \\hat{n}$$

-   The shear component can be found using the Pythagorean theorem
    $$S^2 = |\\hat{T}^n|^2 - N^2$$

----
## tractions

-   We now use the stress tensor in the principal direction to simplify the calculations
    $$\\begin{aligned}
            N &= \\hat{T}^n \\cdot \\hat{n}\\\\
            &= T^n\_i n\_i \\\\
            &= \\sigma\_{ji} n\_j n\_i\\\\
            &= \\sigma\_1 n\_1^2 + \\sigma\_2 n\_2^2 + \\sigma\_3 n\_3^2
            \\end{aligned}$$

----
## tractions

-   We also know that
    $$\\begin{aligned}
            |\\hat{T}^n|^2 &= \\hat{T}^n \\cdot \\hat{T}^n\\\\
            &= T\_i^n T\_i^n \\\\
            &= \\sigma\_{ji} n\_j \\sigma\_{ki} n\_k\\\\
            &= \\sigma\_1^2 n\_1^2 + \\sigma\_2^2 n\_2^2 + \\sigma\_3^2 n\_3^2
            \\end{aligned}$$

----
## mohr’s circle

-   If we constrain the normal vector to be a unit vector we can formulate the following inequalities
    $$\\begin{aligned}
            S^2 + (N-\\sigma\_2)(N-\\sigma\_3) &\\ge 0\\\\
            S^2 + (N-\\sigma\_3)(N-\\sigma\_1) &\\le 0\\\\
            S^2 + (N-\\sigma\_1)(N-\\sigma\_2) &\\ge 0\\\\
            \\end{aligned}$$

-   These inequalities form what is known as Mohr’s circle

----
## mohr’s circle

<img src="mohr" alt="image" /> \[fig:mohr\]

---
# material behavior

----
## topics

-   Hooke’s Law
-   Physical meaning of elastic constants
-   Thermal expansion

----
## hooke’s law

-   Can be written in terms of strain
    $$\\epsilon\_{ij} = \\frac{1+\\nu}{E}\\sigma\_{ij} - \\frac{\\nu}{E}\\sigma\_{kk} \\delta\_{ij}$$

-   Or stress
    *σ*<sub>*i**j*</sub> = *λ**ϵ*<sub>*k**k*</sub>*δ*<sub>*i**j*</sub> + 2*μ**ϵ*<sub>*i**j*</sub>

----
## hooke’s law

-   We should use a form appropriate for the material constants being used in the problem

|          |                                 *λ*=|                        *μ* = *G*=|                                                *E*=|                                    *ν*=|                            *K*=|
|---------:|------------------------------------:|---------------------------------:|---------------------------------------------------:|---------------------------------------:|-------------------------------:|
|  *λ*, *μ*|                                     |                                  |  $\\frac{\\mu(3\\lambda + 2\\mu)}{\\lambda + \\mu}$|  $\\frac{\\lambda}{2(\\lambda + \\mu)}$|  $\\frac{3\\lambda + 2\\mu}{3}$|
|  *G*, *E*|              $\\frac{G(2G-E)}{E-3G}$|                                  |                                                    |                      $\\frac{E-2G}{2G}$|            $\\frac{GE}{3(3G-E}$|
|  *G*, *ν*|            $\\frac{2G\\nu}{1-2\\nu}$|                                  |                                       2*G*(1 + *G*)|                                        |       $\\frac{2G(1+G)}{3(1-2G}$|
|  *E*, *ν*|  $\\frac{\\nu E}{(1+\\nu)(1-2\\nu)}$|            $\\frac{E}{2(1+\\nu)}$|                                                    |                                        |          $\\frac{E}{3(1-2\\nu}$|
|  *K*, *E*|             $\\frac{3K(3K-E)}{9K-E}$|               $\\frac{3EK}{9K-E}$|                                                    |                      $\\frac{3K-E}{6K}$|                                |
|  *ν*, *K*|             $\\frac{3K\\nu}{1+\\nu}$|  $\\frac{3K(1-2\\nu)}{2(1+\\nu)}$|                                      3*K*(1 − 2*ν*)|                                        |                                |

\[tab:addlabel\]

----
## physical meaning

-   Young’s modulus

-   Poisson’s ratio

-   Shear modulus

-   Bulk modulus

----
## thermoelasticity

-   Separate strain into mechanical and thermal components
    *ϵ*<sub>*i**j*</sub> = *ϵ*<sub>*i**j*</sub><sup>(*M*)</sup> + *ϵ*<sub>*i**j*</sub><sup>(*T*)</sup>

-   For isotropic materials:
    *ϵ*<sub>*i**j*</sub><sup>(*T*)</sup> = *α*(*T* − *T*<sub>0</sub>)*δ*<sub>*i**j*</sub>

----
## thermoelasticity

-   We can combine this with Hooke’s Law to find
    $$\\epsilon\_{ij} = \\frac{1+\\nu}{E}\\sigma\_{ij} -\\frac{\\nu}{E}\\sigma\_{kk}\\delta\_{ij} + \\alpha (T-T\_0)\\delta\_{ij}$$

-   Or formulated in terms of stress (and Lamé constants)
    *σ*<sub>*i**j*</sub> = *λ**ϵ*<sub>*k**k*</sub>*δ*<sub>*i**j*</sub> + 2*μ**ϵ*<sub>*i**j*</sub> − (3*λ* + 2*μ*)*α*(*T* − *T*<sub>0</sub>)*δ*<sub>*i**j*</sub>

---
# problem formulation

----
## topics

-   Boundary conditions
-   Compatibility
-   Beltrami-Michell
-   Navier’s Equations
-   Superposition

----
## boundary conditions

-   Traction
-   Displacement
-   Mixed

----
## compatibility equations

-   If continuous, single-valued displacements are specified, differentiation will result in well-behaved strain field

-   The inverse relationship, integration of a strain field to find displacement, may not always be true

-   There are cases where we can integrate a strain field to find a set of discontinuous displacements

----
## compatibility equations

-   The compatibility equations enforce continuity of displacements to prevent this from occurring

-   To enforce this condition we consider the strain-displacement relations:
    $$\\epsilon\_{ij} = \\frac{1}{2}(u\_{i,j} + u\_{j,i})$$

-   and differentiate with respect to *x*<sub>*k*</sub> and *x*<sub>*l*</sub>
    $$\\epsilon\_{ij,kl} = \\frac{1}{2}(u\_{i,jkl} + u\_{j,ikl})$$

-   Or
    2*ϵ*<sub>*i**j*, *k**l*</sub> = *u*<sub>*i*, *j**k**l*</sub> + *u*<sub>*j*, *i**k**l*</sub>

----
## compatibility equations

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

----
## compatibility equations

-   Substituting these values into the equations gives
    2*ϵ*<sub>*i**j*, *k**l*</sub> = 2*ϵ*<sub>*i**k*, *j**l*</sub> − *u*<sub>*k*, *i**j**l*</sub> + 2*ϵ*<sub>*j**l*, *i**k*</sub> − *u*<sub>*l*, *i**j**k*</sub>

-   We now consider one more change of index equation
    2*ϵ*<sub>*k**l*, *i**j*</sub> = *u*<sub>*k*, *i**j**l*</sub> + *u*<sub>*l*, *i**j**k*</sub>

-   and substituting this result gives
    2*ϵ*<sub>*i**j*, *k**l*</sub> = 2*ϵ*<sub>*i**k*, *j**l*</sub> + 2*ϵ*<sub>*j**l*, *i**k*</sub> − 2*ϵ*<sub>*k**l*, *i**j*</sub>

-   Or, simplified
    *ϵ*<sub>*i**j*, *k**l*</sub> + *ϵ*<sub>*k**l*, *i**j*</sub> − *ϵ*<sub>*i**k*, *j**l*</sub> − *ϵ*<sub>*j**l*, *i**k*</sub> = 0

----
## beltrami-michell

-   When working with stress functions, it is convenient to check compatibility of the stress function directly

-   Using Hooke’s Law, we can formulate compatibility in terms of stress

-   These are known as the Beltrami-Michell equations

----
## navier’s equations

-   Similarly, we can write the equilibrium equations in terms of displacement

-   This is convenient when dealing with displacement boundary conditions

-   Known as Navier’s equations


