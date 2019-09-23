<span>upcoming schedule</span>

-   Oct 2 - Equilibrium

-   Oct 4 - Material Behavior, HW 3 Due

-   Oct 9 - Material Behavior

-   Oct 11 - Material Behavior

### outline

\[sections numbered\]

group problems
==============

<span>group one</span>

-   The stress state in a rectangle under biaxial loading is
    $$\\sigma\_{ij} = \\begin{bmatrix} X & 0 & 0\\\\
          0 & Y & 0\\\\
          0 & 0 & 0\\end{bmatrix}$$

-   Find the traction vector, as well as the normal and shearing stresses on some oblique plane, *S*

(0,0) – (0,3.5) node\[above\] <span>*x*<sub>2</sub></span>; (0,0) – (6,0) node\[right\] <span>*x*<sub>1</sub></span>; (1,1) – (1,3) – (5,3) – (5,1) – (1,1); (1.5,1.5) – (2.5,2.5); node at (1.7,2.5) <span>*S*</span>; (2.35,1.5) arc (0:45:0.85) node\[right\] <span>*θ*</span>;

<span>group two</span>

-   For the figure shown, what must the traction be on the other faces for the stress to be uniform and in equilibrium?

(0,0) – (0,3.5) node\[above\] <span>*x*<sub>2</sub></span>; (0,0) – (6,0) node\[right\] <span>*x*<sub>1</sub></span>; (1,1) – (1,3) – (3,3) – (3,1) – (1,1); (3,2) – (4,3) node\[right\] <span>*t*<sub>*i*</sub> = *σ*<sub>0</sub>⟨1, 1⟩</span>;

<span>group three</span>

-   For the figure shown, find the (uniform) stress tensor. What must the traction be on the last face?

(0,0) – (0,3.5) node\[above\] <span>*x*<sub>2</sub></span>; (0,0) – (6,0) node\[right\] <span>*x*<sub>1</sub></span>; (1,1) – (1,3) – (3,1) – (1,1); (2,2) – (3,2) node\[right\] <span>$t\_i=\\frac{\\sigma\_0}{\\sqrt{2}} \\langle 1, 0\\rangle$</span>; (2,1) – (2.5,0.5) node\[right\] <span>$t\_i=\\frac{\\sigma\_0}{2} \\langle 1, -1 \\rangle$</span>;

Other Stress Definitions
========================

<span>spherical and deviatoric stress</span>

-   The spherical and deviatoric stress definitions are identical to the analogous strain definitions

-   Spherical stress:
    $$\\tilde{\\sigma}\_{ij} = \\frac{1}{3}\\sigma\_{kk}\\delta\_{ij}$$

-   Deviatoric stress:
    $$\\hat{\\sigma}\_{ij} = \\sigma\_{ij} - \\tilde{\\sigma}\_{ij}$$

<span>failure theories</span>

-   Many failure theories rely on some form of combined stress

-   One measure is known as the *octahedral stress*

-   We define a special plane whose normal forms the same angle of intersection with the three principal directions

-   This plane is known as the *octahedral plane*

<span>octahedral stress</span>

(0,0,0) – (3,0,0) node\[below left\] <span>*n*<sup>(1)</sup></span>; (0,0,0) – (0,3,0) node\[right\] <span>*n*<sup>(2)</sup></span>; (0,0,0) – (0,0,3) node\[above\] <span>*n*<sup>(3)</sup></span>; (0,0,0) – (2,2,2) node\[above right\] <span>*n*<sup>*o*</sup></span>;

<span>octahedral stress</span>

-   In the principal direction we know that
    $$\\sigma\_{ij} = \\begin{bmatrix}
            \\sigma\_1 & 0 & 0\\\\
            0 & \\sigma\_2 & 0\\\\
            0 & 0 & \\sigma\_3
            \\end{bmatrix}$$

-   The normal vector for the octahedral plane in this system is
    $$n^o = \\frac{1}{\\sqrt{3}}\\langle 1, 1, 1 \\rangle$$

-   And the octahedral normal stress can be found by
    $$\\begin{aligned}
            \\sigma\_{oct} &= t\_i n\_i \\\\
            &= \\sigma\_{ij} n\_j n\_i \\\\
            &= \\frac{1}{3}\\sigma\_{kk}
            \\end{aligned}$$

<span>octahedral stress</span>

-   We can also find the shear stress in the octahedral plane
    $$\\begin{aligned}
            S^2 &= t\_i t\_i - N^2\\\\
            &= \\sigma\_{ij} n\_j \\sigma\_{ik} n\_k - N^2\\\\
            &= \\sigma\_1^2 n\_1^2 + \\sigma\_2^2 n\_2^2 + \\sigma\_3^2 n\_3^2 - N^2\\\\
            \\end{aligned}$$

-   We can simplify this to
    $$\\tau\_{oct} = \\frac{1}{3}\\sqrt{(\\sigma\_1-\\sigma\_2)^2+(\\sigma\_2-\\sigma\_3)^2+(\\sigma\_3-\\sigma\_1)^2}$$

-   Or in terms of invariants
    $$\\tau\_{oct} = \\frac{1}{3}\\sqrt{2I\_1^2 - 6I\_2}$$

<span>von mises stress</span>

-   Another common stress is known as the Von Mises stress

-   Von Mises stress is related to the *distortional strain energy*

-   Sometimes the Von Mises stress is referred to as the effective stress
    $$\\sigma\_e = \\sigma\_{VM} = \\frac{1}{\\sqrt{2}}\\sqrt{(\\sigma\_1-\\sigma\_2)^2+(\\sigma\_2-\\sigma\_3)^2+(\\sigma\_3-\\sigma\_1)^2}$$

<span>large deformation</span>

-   The stress tensor we have developed is known as the Cauchy stress tensor

-   The Cauchy stress tensor is expressed in the deformed coordinate system

-   This is appropriate for small deformation problems, where the un-deformed and deformed systems are nearly identical

-   For large deformation problems, we may wish to define stress in terms of the un-deformed coordinate system

-   Lagrangian stress is defined as
    $$\\sigma\_{pi}^L = \\frac{\\rho^0}{\\rho}\\sigma\_{ji} \\frac{\\partial x\_p^0}{\\partial x\_j}$$

<span>large deformations</span>

-   The Cauchy stress tensor is symmetric
    *σ*<sub>*i**j*</sub> = *σ*<sub>*j**i*</sub>

-   Substitution of this relationship for Lagrangian stress, however, gives
    $$\\sigma\_{pi}^L \\frac{\\partial x\_j}{x^0\_p} = \\sigma\_{pj}^L \\frac{\\partial x\_i}{\\partial x\_p^0}$$

-   Which indicates the *σ*<sub>*i**j*</sub><sup>*L*</sup> is not symmetric

<span>piola kirchoff stress</span>

-   We can force symmetry by changing the definition to
    $$\\frac{\\partial x\_i}{\\partial x\_j^0}\\sigma\_{pj}^K = \\frac{\\rho^0}{\\rho}\\sigma\_{ji} \\frac{\\partial x\_p^0}{\\partial x\_j}$$

-   From this we can find the Piola-Kirchoff stress, which is symmetric
    $$\\sigma\_{pq}^K = \\frac{\\rho^0}{\\rho}\\sigma\_{ji} \\frac{\\partial x\_p^0}{\\partial x\_i}\\frac{\\partial x\_q^0}{\\partial x\_j}$$

-   This is also known as the *second Piola stress tensor* or the *Kirchoff stress tensor*

-   In this course we focus on small deformations, so we will only use the Cauchy stress tensor

Equilibrium Equations
=====================

<span>static equilibrium</span>

<img src="../Figures/equilibrium" alt="image" /> \[fig:equilibrium\]

-   We primarily deal with bodies in static equilibrium

-   This means that all forces and moments must sum to zero

-   For a closed sub-domain of volume *V* and surface area *S* with internal body forces and applied tractions, we find
    ∬<sub>*S*</sub>*T*<sub>*i*</sub><sup>*n*</sup>*d**S* + ∭<sub>*V*</sub>*F*<sub>*i*</sub>*d**V* = 0

<span>static equilibrium</span>

-   Using the Cauchy stress theorem, we can replace the traction vector with the stress tensor
    ∬<sub>*S*</sub>*σ*<sub>*j**i*</sub>*n*<sub>*j*</sub>*d**S* + ∭<sub>*V*</sub>*F*<sub>*i*</sub>*d**V* = 0

-   We can also apply the divergence theorem to convert the surface integral to a volume integral
    ∭<sub>*V*</sub>(*σ*<sub>*j**i*, *j*</sub> + *F*<sub>*i*</sub>)*d**V* = 0

-   Since the volume is arbitrary (we could choose any volume and the conditions for equilibrium would still hold), the integrand must vanish
    *σ*<sub>*j**i*, *j*</sub> + *F*<sub>*i*</sub> = 0

<span>equilibrium equations</span>

-   Written in scalar form, the equilibrium equations are
    $$\\begin{aligned}
            \\frac{\\partial \\sigma\_x}{\\partial x} + \\frac{\\partial \\tau\_{xy}}{\\partial y} + \\frac{\\partial \\tau\_{xz}}{\\partial z} + F\_x &= 0\\\\
            \\frac{\\partial \\tau\_{xy}}{\\partial x} + \\frac{\\partial \\sigma\_y}{\\partial y} + \\frac{\\partial \\tau\_{yz}}{\\partial z} + F\_y &= 0\\\\
            \\frac{\\partial \\tau\_{xz}}{\\partial x} + \\frac{\\partial \\tau\_{yz}}{\\partial y} + \\frac{\\partial \\sigma\_z}{\\partial z} + F\_z &= 0\\\\
            \\end{aligned}$$

<span>angular momentum</span>

-   Similarly, the principle of angular momentum states that the moment forces must all sum to zero as well
    ∬<sub>*S*</sub>*ϵ*<sub>*i**j**k*</sub>*x*<sub>*j*</sub>*T*<sub>*k*</sub><sup>*n*</sup>*d**S* + ∭<sub>*V*</sub>*ϵ*<sub>*i**j**k*</sub>*x*<sub>*j*</sub>*F*<sub>*k*</sub>*d**V* = 0

-   Once again we use Cauchy’s stress theorem
    ∬<sub>*S*</sub>*ϵ*<sub>*i**j**k*</sub>*x*<sub>*j*</sub>*σ*<sub>*l**k*</sub>*n*<sub>*l*</sub>*d**S* + ∭<sub>*V*</sub>*ϵ*<sub>*i**j**k*</sub>*x*<sub>*j*</sub>*F*<sub>*k*</sub>*d**V* = 0

-   And the divergence theorem
    ∭<sub>*V*</sub>\[(*ϵ*<sub>*i**j**k*</sub>*x*<sub>*j*</sub>*σ*<sub>*l**k*</sub>)<sub>,*l*</sub> + *ϵ*<sub>*i**j**k*</sub>*x*<sub>*j*</sub>*F*<sub>*k*</sub>\]*d**V* = 0

<span>angular momentum</span>

-   Expanding the derivative using the chain rule gives
    ∭<sub>*V*</sub>\[*ϵ*<sub>*i**j**k*</sub>*x*<sub>*j*, *l*</sub>*σ*<sub>*l**k*</sub> + *ϵ*<sub>*i**j**k*</sub>*x*<sub>*j*</sub>*σ*<sub>*l**k*, *l*</sub> + *ϵ*<sub>*i**j**k*</sub>*x*<sub>*j*</sub>*F*<sub>*k*</sub>\]*d**V* = 0

-   Which can be simplified (recall that *σ*<sub>*j**i*, *j*</sub> + *F*<sub>*i*</sub> = 0)
    $$\\begin{aligned}
            \\iiint\_V \[ \\epsilon\_{ijk}\\delta\_{jl}\\sigma\_{lk} + \\epsilon\_{ijk}x\_j\\sigma\_{lk,l} + \\epsilon\_{ijk}x\_jF\_k \] dV &= 0\\\\
            \\iiint\_V \[ \\epsilon\_{ijk}\\sigma\_{jk} - \\epsilon\_{ijk}x\_jF\_k + \\epsilon\_{ijk}x\_jF\_k \] dV &= 0\\\\
            \\iiint\_V \\epsilon\_{ijk}\\sigma\_{jk} dV &= 0
            \\end{aligned}$$

<span>angular momentum</span>

-   Using the same argument as before (arbitrary volume) the integrand must vanish
    *ϵ*<sub>*i**j**k*</sub>*σ*<sub>*j**k*</sub> = 0

-   Since the alternating symbol is antisymmetric in *j**k*, *σ*<sub>*j**k*</sub> must be symmetric in *j**k* for this to vanish

-   And thus we have proved that the stress tensor is symmetric, thus equilibrium and angular momentum equations are satisfied when
    *σ*<sub>*j**i*, *j*</sub> + *F*<sub>*i*</sub> = 0

<span>example</span>

-   Under what circumstances is the following stress field in static equilibrium?

-   *σ*<sub>11</sub> = 3*x*<sub>1</sub> + *k*<sub>1</sub>*x*<sub>2</sub><sup>2</sup>, *σ*<sub>22</sub> = 2*x*<sub>1</sub> + 4*x*<sub>2</sub>, *σ*<sub>12</sub> = *σ*<sub>21</sub> = *a* + *b**x*<sub>1</sub> + *c**x*<sub>1</sub><sup>2</sup> + *d**x*<sub>2</sub> + *e**x*<sub>2</sub><sup>2</sup> + *f**x*<sub>1</sub>*x*<sub>2</sub>

-   We are only examining the stress field, so we neglect any internal body forces

-   The first equilibrium equation gives
    $$\\frac{\\partial \\sigma\_{11}}{\\partial x\_1} + \\frac{\\partial \\sigma\_{12}}{\\partial x\_2} = 0$$
    3 + *d* + 2*e**x*<sub>2</sub> + *f**x*<sub>1</sub> = 0

<span>example</span>

-   The second equilibrium equation gives
    $$\\frac{\\partial \\sigma\_{12}}{\\partial x\_1} + \\frac{\\partial \\sigma\_{22}}{\\partial x\_2} = 0$$
    *b* + 2*c**x*<sub>1</sub> + *f**x*<sub>2</sub> + 4 = 0

Spherical and Cylindrical Coordinates
=====================================

<span>cylindrical coordinates</span>

(0,0,0) – (3,0,0) node\[below left\] <span>*x*<sub>1</sub></span>; (0,0,0) – (0,3,0) node\[right\] <span>*x*<sub>2</sub></span>; (0,0,0) – (0,0,3) node\[above\] <span>*x*<sub>3</sub></span>; (0,0,0) – (2,0,0) node\[below\] <span>*r*</span>; ; (0,0,0) – (0,0,2) node\[above left\] <span>*z*</span>;

<span>stress in cylindrical coordinates</span>

-   We can also define stress in a cylindrical coordinate system

    <img src="../Figures/cylindrical" alt="image" /> \[fig:cylindrical\]

<span>stress in cylindrical coordinates</span>

-   The stress tensor in cylindrical coordinates is
    $$\\sigma\_{ij} = \\begin{bmatrix}
            \\sigma\_r & \\tau\_{r\\theta}& \\tau\_{rz} \\\\
            \\tau\_{r\\theta} & \\sigma\_{\\theta} & \\tau\_{\\theta z}\\\\
            \\tau\_{rz} & \\tau\_{\\theta z} & \\sigma\_z
            \\end{bmatrix}$$

<span>equilibrium in cylindrical coordinates</span>

-   Using the derivative relationships developed in Chapter 1, we can express the equilibrium equations as
    $$\\begin{aligned}
            \\frac{\\partial \\sigma\_r}{\\partial r} + \\frac{1}{r} \\frac{\\partial \\tau\_{r \\theta}}{\\partial \\theta} + \\frac{\\partial \\tau\_{rz}}{\\partial z} + \\frac{1}{r}(\\sigma\_r - \\sigma\_\\theta) + F\_r &= 0\\\\
            \\frac{\\partial \\tau\_{r \\theta}}{\\partial r} + \\frac{1}{r} \\frac{\\partial \\sigma\_\\theta}{\\partial \\theta} + \\frac{\\partial \\tau\_{\\theta z}}{\\partial z} + \\frac{2}{r}\\tau\_{r\\theta} + F\_\\theta &= 0\\\\
            \\frac{\\partial \\tau\_{r z}}{\\partial r} + \\frac{1}{r} \\frac{\\partial \\tau\_{\\theta z}}{\\partial \\theta} + \\frac{\\partial \\sigma\_z}{\\partial z} + \\frac{1}{r}\\tau\_{rz} + F\_z &= 0
            \\end{aligned}$$

<span>spherical coordinates</span>

-   We can do the same thing in spherical coordinates

<img src="../Figures/spherical" alt="image" /> \[fig:spherical\]

<span>spherical coordinates</span>

-   The stress tensor in spherical coordinates is
    $$\\sigma\_{ij} = \\begin{bmatrix}
            \\sigma\_r & \\tau\_{r\\phi}& \\tau\_{r\\theta} \\\\
            \\tau\_{r\\phi} & \\sigma\_{\\phi} & \\tau\_{\\phi \\theta}\\\\
            \\tau\_{r\\theta} & \\tau\_{\\phi \\theta} & \\sigma\_\\theta
            \\end{bmatrix}$$

<span>equilibrium in spherical coordinates</span>

-   Using the derivative relationships developed in Chapter 1, we can express the equilibrium equations as
    $$\\begin{aligned}
            \\frac{\\partial \\sigma\_r}{\\partial r} + \\frac{1}{r} \\frac{\\partial \\tau\_{r \\phi}}{\\partial \\phi} + \\frac{1}{r \\sin \\phi}\\frac{\\partial \\tau\_{r\\theta}}{\\partial \\theta} + \\frac{1}{r}(2\\sigma\_r - \\sigma\_\\phi - \\sigma\_\\theta + \\tau\_{r\\phi}\\cot \\phi) + F\_r &= 0\\\\
            \\frac{\\partial \\tau\_{r \\phi}}{\\partial r} + \\frac{1}{r} \\frac{\\partial \\sigma\_\\phi}{\\partial \\phi} + \\frac{1}{r \\sin \\phi}\\frac{\\partial \\tau\_{\\phi \\theta}}{\\partial \\theta} + \\frac{1}{r}\[(\\sigma\_\\phi -\\sigma\_\\theta)\\cot \\phi + 3\\tau\_{r\\phi}\] + F\_\\phi &= 0\\\\
            \\frac{\\partial \\tau\_{r \\theta}}{\\partial r} + \\frac{1}{r} \\frac{\\partial \\tau\_{\\phi \\theta}}{\\partial \\phi} + \\frac{1}{r \\sin \\phi}\\frac{\\partial \\sigma\_\\theta}{\\partial \\theta} + \\frac{1}{r}(2 \\tau\_{\\phi \\theta}\\cot \\phi + 3 \\tau\_{r \\theta}) + F\_\\theta &= 0
            \\end{aligned}$$


