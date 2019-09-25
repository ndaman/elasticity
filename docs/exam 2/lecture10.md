# AE731
## Theory of Elasticity
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering
September 30, 2019

----
## upcoming schedule

-   Sep 30 - Equilibrium Equations
-   Oct 2 - Material Characterization, HW3 Due
-   Oct 7 - Thermoelasticity
-   Oct 9 - Boundary Conditions

----
## outline

<!-- vim-markdown-toc GFM -->

* other stress definitions
* equilibrium equations
* spherical and cylindrical coordinates

<!-- vim-markdown-toc -->

---
# other stress definitions

----
## spherical and deviatoric stress

-   The spherical and deviatoric stress definitions are identical to the analogous strain definitions
-   Spherical stress:

$$\\tilde{\\sigma}\_{ij} = \\frac{1}{3}\\sigma\_{kk}\\delta\_{ij}$$

-   Deviatoric stress:

$$\\hat{\\sigma}\_{ij} = \\sigma\_{ij} - \\tilde{\\sigma}\_{ij}$$

----
## failure theories

-   Many failure theories rely on some form of combined stress
-   One measure is known as the *octahedral stress*
-   We define a special plane whose normal forms the same angle of intersection with the three principal directions
-   This plane is known as the *octahedral plane*

----
## octahedral stress

![illustration of normal vector for octahedral stress](../images/octahedral.svg)

----
## octahedral stress

-   In the principal direction we know that

$$\\sigma\_{ij} = \\begin{bmatrix}
	\\sigma\_1 & 0 & 0\\\\
	0 & \\sigma\_2 & 0\\\\
	0 & 0 & \\sigma\_3
\\end{bmatrix}$$

-   The normal vector for the octahedral plane in this system is

$$n^o = \\frac{1}{\\sqrt{3}}\\langle 1, 1, 1 \\rangle$$

----
## octahedral stress

-   And the octahedral normal stress can be found by

$$\\begin{aligned}
	\\sigma\_{oct} &= t\_i n\_i \\\\
	&= \\sigma\_{ij} n\_j n\_i \\\\
	&= \\frac{1}{3}\\sigma\_{kk}
\\end{aligned}$$

----
## octahedral stress

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

----
## von mises stress

-   Another common stress is known as the Von Mises stress
-   Von Mises stress is related to the *distortional strain energy*
-   Sometimes the Von Mises stress is referred to as the effective stress

$$\\sigma\_e = \\sigma\_{VM} = \\frac{1}{\\sqrt{2}}\\sqrt{(\\sigma\_1-\\sigma\_2)^2+(\\sigma\_2-\\sigma\_3)^2+(\\sigma\_3-\\sigma\_1)^2}$$

----
## large deformation

-   The stress tensor we have developed is known as the Cauchy stress tensor
-   The Cauchy stress tensor is expressed in the deformed coordinate system
-   This is appropriate for small deformation problems, where the un-deformed and deformed systems are nearly identical
-   For large deformation problems, we may wish to define stress in terms of the un-deformed coordinate system

----
## large deformation

-   Lagrangian stress is defined as

$$\\sigma\_{pi}^L = \\frac{\\rho^0}{\\rho}\\sigma\_{ji} \\frac{\\partial x\_p^0}{\\partial x\_j}$$

----
## large deformations

-   The Cauchy stress tensor is symmetric

_σ_<sub>*ij*</sub> = *σ*<sub>*ji*</sub>

-   Substitution of this relationship for Lagrangian stress, however, gives

$$\\sigma\_{pi}^L \\frac{\\partial x\_j}{x^0\_p} = \\sigma\_{pj}^L \\frac{\\partial x\_i}{\\partial x\_p^0}$$

-   Which indicates the *σ*<sub>*ij*</sub><sup>*L*</sup> is not symmetric

----
## piola kirchoff stress

-   We can force symmetry by changing the definition to

$$\\frac{\\partial x\_i}{\\partial x\_j^0}\\sigma\_{pj}^K = \\frac{\\rho^0}{\\rho}\\sigma\_{ji} \\frac{\\partial x\_p^0}{\\partial x\_j}$$

-   From this we can find the Piola-Kirchoff stress, which is symmetric

$$\\sigma\_{pq}^K = \\frac{\\rho^0}{\\rho}\\sigma\_{ji} \\frac{\\partial x\_p^0}{\\partial x\_i}\\frac{\\partial x\_q^0}{\\partial x\_j}$$

-   This is also known as the *second Piola stress tensor* or the *Kirchoff stress tensor*
-   In this course we focus on small deformations, so we will only use the Cauchy stress tensor

---
# equilibrium equations

----
## static equilibrium

![an arbitrary body under arbitrary remote loading with internal body forces](../images/equilibrium.PNG)

----
## static equilibrium

-   We primarily deal with bodies in static equilibrium
-   This means that all forces and moments must sum to zero
-   For a closed sub-domain of volume *V* and surface area *S* with internal body forces and applied tractions, we find

∬<sub>*S*</sub>*T*<sub>*i*</sub><sup>*n*</sup>*dS* + ∭<sub>*V*</sub>*F*<sub>*i*</sub>*dV* = 0

----
## static equilibrium

-   Using the Cauchy stress theorem, we can replace the traction vector with the stress tensor

∬<sub>*S*</sub>*σ*<sub>*ji*</sub>*n*<sub>*j*</sub>*dS* + ∭<sub>*V*</sub>*F*<sub>*i*</sub>*dV* = 0

-   We can also apply the divergence theorem to convert the surface integral to a volume integral

∭<sub>*V*</sub>(*σ*<sub>*ji*, *j*</sub> + *F*<sub>*i*</sub>)*dV* = 0

----
## static equilibrium

-   Since the volume is arbitrary (we could choose any volume and the conditions for equilibrium would still hold), the integrand must vanish

_σ_<sub>*ji*, *j*</sub> + *F*<sub>*i*</sub> = 0

----
## equilibrium equations

-   Written in scalar form, the equilibrium equations are

$$\\begin{aligned}
	\\frac{\\partial \\sigma\_x}{\\partial x} + \\frac{\\partial \\tau\_{xy}}{\\partial y} + \\frac{\\partial \\tau\_{xz}}{\\partial z} + F\_x &= 0\\\\
	\\frac{\\partial \\tau\_{xy}}{\\partial x} + \\frac{\\partial \\sigma\_y}{\\partial y} + \\frac{\\partial \\tau\_{yz}}{\\partial z} + F\_y &= 0\\\\
	\\frac{\\partial \\tau\_{xz}}{\\partial x} + \\frac{\\partial \\tau\_{yz}}{\\partial y} + \\frac{\\partial \\sigma\_z}{\\partial z} + F\_z &= 0\\\\
\\end{aligned}$$

----
## angular momentum

-   Similarly, the principle of angular momentum states that the moment forces must all sum to zero as well

∬<sub>*S*</sub>*ϵ*<sub>*ijk*</sub>*x*<sub>*j*</sub>*T*<sub>*k*</sub><sup>*n*</sup>*dS* + ∭<sub>*V*</sub>*ϵ*<sub>*ijk*</sub>*x*<sub>*j*</sub>*F*<sub>*k*</sub>*dV* = 0

-   Once again we use Cauchy’s stress theorem

∬<sub>*S*</sub>*ϵ*<sub>*ijk*</sub>*x*<sub>*j*</sub>*σ*<sub>*lk*</sub>*n*<sub>*l*</sub>*dS* + ∭<sub>*V*</sub>*ϵ*<sub>*ijk*</sub>*x*<sub>*j*</sub>*F*<sub>*k*</sub>*dV* = 0

-   And the divergence theorem

∭<sub>*V*</sub>\[(*ϵ*<sub>*ijk*</sub>*x*<sub>*j*</sub>*σ*<sub>*lk*</sub>)<sub>,*l*</sub> + *ϵ*<sub>*ijk*</sub>*x*<sub>*j*</sub>*F*<sub>*k*</sub>\]*dV* = 0

----
## angular momentum

-   Expanding the derivative using the chain rule gives

∭<sub>*V*</sub>\[*ϵ*<sub>*ijk*</sub>*x*<sub>*j*, *l*</sub>*σ*<sub>*lk*</sub> + *ϵ*<sub>*ijk*</sub>*x*<sub>*j*</sub>*σ*<sub>*lk*, *l*</sub> + *ϵ*<sub>*ijk*</sub>*x*<sub>*j*</sub>*F*<sub>*k*</sub>\]*dV* = 0

-   Which can be simplified (recall that *σ*<sub>*ji*, *j*</sub> + *F*<sub>*i*</sub> = 0)

$$\\begin{aligned}
	\\iiint\_V \[ \\epsilon\_{ijk}\\delta\_{jl}\\sigma\_{lk} + \\epsilon\_{ijk}x\_j\\sigma\_{lk,l} + \\epsilon\_{ijk}x\_jF\_k \] dV &= 0\\\\
	\\iiint\_V \[ \\epsilon\_{ijk}\\sigma\_{jk} - \\epsilon\_{ijk}x\_jF\_k + \\epsilon\_{ijk}x\_jF\_k \] dV &= 0\\\\
	\\iiint\_V \\epsilon\_{ijk}\\sigma\_{jk} dV &= 0
\\end{aligned}$$

----
## angular momentum

-   Using the same argument as before (arbitrary volume) the integrand must vanish

_ϵ_<sub>*ijk*</sub>*σ*<sub>*jk*</sub> = 0

-   Since the alternating symbol is antisymmetric in *jk*, *σ*<sub>*jk*</sub> must be symmetric in *jk* for this to vanish

-   And thus we have proved that the stress tensor is symmetric, thus equilibrium and angular momentum equations are satisfied when

_σ_<sub>*ji*, *j*</sub> + *F*<sub>*i*</sub> = 0

----
## example

-   Under what circumstances is the following stress field in static equilibrium?

-   *σ*<sub>11</sub> = 3*x*<sub>1</sub> + *k*<sub>1</sub>*x*<sub>2</sub><sup>2</sup>, *σ*<sub>22</sub> = 2*x*<sub>1</sub> + 4*x*<sub>2</sub>, *σ*<sub>12</sub> = *σ*<sub>21</sub> = *a* + *bx*<sub>1</sub> + *cx*<sub>1</sub><sup>2</sup> + *dx*<sub>2</sub> + *ex*<sub>2</sub><sup>2</sup> + *fx*<sub>1</sub>*x*<sub>2</sub>

-   We are only examining the stress field, so we neglect any internal body forces
-   The first equilibrium equation gives

$$\\frac{\\partial \\sigma\_{11}}{\\partial x\_1} + \\frac{\\partial \\sigma\_{12}}{\\partial x\_2} = 0$$

3 + *d* + 2*ex*<sub>2</sub> + *fx*<sub>1</sub> = 0

----
## example

-   The second equilibrium equation gives

$$\\frac{\\partial \\sigma\_{12}}{\\partial x\_1} + \\frac{\\partial \\sigma\_{22}}{\\partial x\_2} = 0$$

_b_ + 2*cx*<sub>1</sub> + *fx*<sub>2</sub> + 4 = 0

---
# spherical and cylindrical coordinates

----
## cylindrical coordinates

**TODO** insert figure

----
## stress in cylindrical coordinates

-   We can also define stress in a cylindrical coordinate system

![an illustration of the stress tensor terms in cylindrical coordinates](../images/cylindrical.PNG)

----
## stress in cylindrical coordinates

-   The stress tensor in cylindrical coordinates is

$$\\sigma\_{ij} = \\begin{bmatrix}
	\\sigma\_r & \\tau\_{r\\theta}& \\tau\_{rz} \\\\
	\\tau\_{r\\theta} & \\sigma\_{\\theta} & \\tau\_{\\theta z}\\\\
	\\tau\_{rz} & \\tau\_{\\theta z} & \\sigma\_z
\\end{bmatrix}$$

----
## equilibrium in cylindrical coordinates

-   Using the derivative relationships developed in Chapter 1, we can express the equilibrium equations as

$$\\begin{aligned}
	\\frac{\\partial \\sigma\_r}{\\partial r} + \\frac{1}{r} \\frac{\\partial \\tau\_{r \\theta}}{\\partial \\theta} + \\frac{\\partial \\tau\_{rz}}{\\partial z} + \\frac{1}{r}(\\sigma\_r - \\sigma\_\\theta) + F\_r &= 0\\\\
	\\frac{\\partial \\tau\_{r \\theta}}{\\partial r} + \\frac{1}{r} \\frac{\\partial \\sigma\_\\theta}{\\partial \\theta} + \\frac{\\partial \\tau\_{\\theta z}}{\\partial z} + \\frac{2}{r}\\tau\_{r\\theta} + F\_\\theta &= 0\\\\
	\\frac{\\partial \\tau\_{r z}}{\\partial r} + \\frac{1}{r} \\frac{\\partial \\tau\_{\\theta z}}{\\partial \\theta} + \\frac{\\partial \\sigma\_z}{\\partial z} + \\frac{1}{r}\\tau\_{rz} + F\_z &= 0
\\end{aligned}$$

----
## spherical coordinates

-   We can do the same thing in spherical coordinates

![an illustration of the stress tensor terms in spherical coordinates](../images/spherical.PNG)

----
## spherical coordinates

-   The stress tensor in spherical coordinates is

$$\\sigma\_{ij} = \\begin{bmatrix}
	\\sigma\_r & \\tau\_{r\\phi}& \\tau\_{r\\theta} \\\\
	\\tau\_{r\\phi} & \\sigma\_{\\phi} & \\tau\_{\\phi \\theta}\\\\
	\\tau\_{r\\theta} & \\tau\_{\\phi \\theta} & \\sigma\_\\theta
\\end{bmatrix}$$

----
## equilibrium in spherical coordinates

-   Using the derivative relationships developed in Chapter 1, we can express the equilibrium equations as

$$\\begin{aligned}
	\\frac{\\partial \\sigma\_r}{\\partial r} + \\frac{1}{r} \\frac{\\partial \\tau\_{r \\phi}}{\\partial \\phi} + \\frac{1}{r \\sin \\phi}\\frac{\\partial \\tau\_{r\\theta}}{\\partial \\theta} + \\frac{1}{r}(2\\sigma\_r - \\sigma\_\\phi - \\sigma\_\\theta + \\tau\_{r\\phi}\\cot \\phi) + F\_r &= 0\\\\
	\\frac{\\partial \\tau\_{r \\phi}}{\\partial r} + \\frac{1}{r} \\frac{\\partial \\sigma\_\\phi}{\\partial \\phi} + \\frac{1}{r \\sin \\phi}\\frac{\\partial \\tau\_{\\phi \\theta}}{\\partial \\theta} + \\frac{1}{r}\[(\\sigma\_\\phi -\\sigma\_\\theta)\\cot \\phi + 3\\tau\_{r\\phi}\] + F\_\\phi &= 0\\\\
	\\frac{\\partial \\tau\_{r \\theta}}{\\partial r} + \\frac{1}{r} \\frac{\\partial \\tau\_{\\phi \\theta}}{\\partial \\phi} + \\frac{1}{r \\sin \\phi}\\frac{\\partial \\sigma\_\\theta}{\\partial \\theta} + \\frac{1}{r}(2 \\tau\_{\\phi \\theta}\\cot \\phi + 3 \\tau\_{r \\theta}) + F\_\\theta &= 0
\\end{aligned}$$


