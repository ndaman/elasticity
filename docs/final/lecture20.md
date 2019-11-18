# AE731
## Theory of Elasticity
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering
November 20, 2019

----
## upcoming schedule

-   Nov 20 - Polar Coordinates in Airy Stress, Homework 7 Due
-   Nov 25 - Polar Coordinates in Airy Stress
-   Nov 27 - No Class (Thanksgiving Break)
-   Dec 2 - Complex Methods
-   Dec 4 - Final Review, Homework 8 Due
-   Dec 11 - 3:00 - 4:50 Final Exam

----
## outline

<!-- vim-markdown-toc GFM -->

* polar coordinates
* examples

<!-- vim-markdown-toc -->

---
# polar coordinates

----
## strain-displacement

-   Reduced strain-displacement:

$$\\begin{aligned}
	\\epsilon\_r &= \\frac{\\partial u\_r}{\\partial r}, \\epsilon\_\\theta = \\frac{1}{r}\\left(u\_r + \\frac{\\partial u\_\\theta}{\\partial \\theta}\\right), \\epsilon\_z = \\frac{\\partial u\_z}{\\partial z}\\\\
	\\epsilon\_{r \\theta} &= \\frac{1}{2} \\left(\\frac{1}{r} \\frac{\\partial u\_r}{\\partial \\theta} + \\frac{\\partial u\_\\theta}{\\partial r} - \\frac{u\_\\theta}{r}\\right) \\\\
	\\epsilon\_{\\theta z} &= \\frac{1}{2} \\left(\\frac{\\partial u\_\\theta}{\\partial z} + \\frac{1}{r}\\frac{\\partial u\_z}{\\partial \\theta}\\right)\\\\
	\\epsilon\_{zr} &= \\frac{1}{2}\\left(\\frac{\\partial u\_r}{\\partial z} + \\frac{\\partial u\_z}{\\partial r}\\right)
\\end{aligned}$$

----
## strain-displacement

-   Which becomes

$$\\begin{aligned}
	\\epsilon\_r &= \\frac{\\partial u\_r}{\\partial r}\\\\
	\\epsilon\_\\theta &= \\frac{1}{r}\\left(u\_r + \\frac{\\partial u\_\\theta}{\\partial \\theta}\\right)\\\\
	\\epsilon\_{r \\theta} &= \\frac{1}{2} \\left(\\frac{1}{r} \\frac{\\partial u\_r}{\\partial \\theta} + \\frac{\\partial u\_\\theta}{\\partial r} - \\frac{u\_\\theta}{r}\\right) \\\\
\\end{aligned}$$

----
## integration

-   When we change variables in integration, we also need to account for the proper change in dV
-   *dV* = *dxdydz* ≠ *drdθdz*
-   We can find the correct *dV* by calculating the Jacobian

----
## jacobian

$$dV = dx dy dz = |\\frac{\\partial(x,y,z)}{\\partial(r,\\theta,z)}| dr d\\theta dz$$

$$dV = \\begin{vmatrix}
	\\frac{\\partial x}{\\partial r} & \\frac{\\partial x}{\\partial \\theta} & \\frac{\\partial x}{\\partial z}\\\\
	\\frac{\\partial y}{\\partial r} & \\frac{\\partial y}{\\partial \\theta} & \\frac{\\partial y}{\\partial z}\\\\
	\\frac{\\partial z}{\\partial r} & \\frac{\\partial z}{\\partial \\theta} & \\frac{\\partial z}{\\partial z}
\\end{vmatrix} dr d\\theta dz = r dr d\\theta dz$$

----
## hooke’s law

-   The tensor equation for Hooke’s Law is valid in polar/cylindrical/spherical coordinates too
-   We only need special equations when differentiating or integrating

$$\\begin{aligned}
	\\sigma\_{ij} &= \\lambda \\epsilon\_{kk}\\delta\_{ij} + 2\\mu \\epsilon\_{ij} - (3\\lambda + 2\\mu)\\alpha\\Delta T \\delta\_{ij}\\\\
	\\epsilon\_{ij} &= \\frac{1+\\nu}{E}\\sigma\_{ij} - \\frac{\\nu}{E}\\sigma\_{kk} \\delta\_{ij} + \\alpha\\Delta T \\delta\_{ij}
\\end{aligned}$$

----
## equilibrium

-   We have already found the equilibrium equations in polar coordinates, they are

$$\\begin{aligned}
	\\frac{\\partial \\sigma\_r}{\\partial r} + \\frac{1}{r} \\frac{\\partial \\tau\_{r \\theta}}{\\partial \\theta} + \\frac{1}{r}(\\sigma\_r - \\sigma\_\\theta) + F\_r &= 0 \\\\
	\\frac{\\partial \\tau\_{r \\theta}}{\\partial r} + \\frac{1}{r} \\frac{\\partial \\sigma\_\\theta}{\\partial \\theta} + \\frac{2}{r}\\tau\_{r\\theta} + F\_\\theta &= 0
\\end{aligned}$$

----
## equilibrium

-   The equilibrium equations can be written in terms of displacement (Navier equations)
-   These are only useful when using a displacement formulation, but we are using stress functions
-   Instead we need the Beltrami-Mitchell compatibility equations

----
## compatibility

-   Substituting stress-strain relations into the compatibility equations gives

$$\\begin{aligned}
	\\nabla^2 (\\sigma\_r + \\sigma\_\\theta) &= -\\frac{1}{1-\\nu}\\left(\\frac{\\partial F\_r}{\\partial r} + \\frac{F\_r}{r} + \\frac{1}{r}\\frac{\\partial F\_\\theta}{\\partial \\theta}\\right) & \\text{(Plane Strain)}\\\\
	\\nabla^2 (\\sigma\_r + \\sigma\_\\theta) &= -(1+\\nu)\\left(\\frac{\\partial F\_r}{\\partial r} + \\frac{F\_r}{r} + \\frac{1}{r}\\frac{\\partial F\_\\theta}{\\partial \\theta}\\right) & \\text{(Plane Stress)}
\\end{aligned}$$

----
## airy stress functions

-   When the body forces are zero, we find

$$\\begin{aligned}
	\\sigma\_r &= \\frac{1}{r}\\frac{\\partial \\phi}{\\partial r} + \\frac{1}{r^2}\\frac{\\partial^2 \\phi}{\\partial \\theta^2}\\\\
	\\sigma\_\\theta &= \\frac{\\partial^2 \\phi}{\\partial r^2}\\\\
	\\tau\_{r\\theta} &= -\\frac{\\partial}{\\partial r} \\left( \\frac{1}{r} \\frac{\\partial \\phi}{\\partial \\theta} \\right)
\\end{aligned}$$

----
## airy stress functions

-   When body forces are zero, we find the following biharmonic equation for the Beltrami-Mitchell equations

∇<sup>4</sup>*ϕ* = 0

-   Where the Laplacian is

$$\\nabla^2 = \\frac{\\partial^2}{\\partial r^2} + \\frac{1}{r}\\frac{\\partial}{\\partial r} + \\frac{1}{r^2} \\frac{\\partial^2}{\\partial \\theta^2}$$

----
## polar coordinates

-   Recall that an Airy Stress function must satisfy the Beltrami-Mitchell compatibility equations

$$\\nabla^4 \\phi = \\left(\\frac{\\partial ^2}{\\partial r^2} + \\frac{1}{r} \\frac{\\partial}{\\partial r} + \\frac{1}{r^2}\\frac{\\partial ^2}{\\partial \\theta^2}\\right)^2\\phi = 0$$

-   One method which gives several useful solutions assumes that the Airy Stress function has the form *ϕ*(*r*, *θ*)=*f*(*r*)*e*<sup>*bθ*</sup>

----
## polar coordinates 

-   Substituting this into the compatibility equations (and canceling the common *e*<sup>*bθ*</sup>) term gives

$$f^{\\prime \\prime \\prime \\prime} + \\frac{2}{r} f^{\\prime \\prime \\prime} - \\frac{1-2b^2}{r^2}f^{\\prime \\prime} + \\frac{1-2b^2}{r^3}f^{\\prime} + \\frac{b^2(4+b^2)}{r^4}f = 0$$

----
## polar coordinates

-   To solve this, we perform a change of variables, letting *r* = *e*<sup>*ξ*</sup>, which gives

_f_<sup>′′′′</sup> − 4*f*<sup>′′′</sup> + (4 + 2*b*<sup>2</sup>)*f*<sup>′′</sup> − 4*b*<sup>2</sup>*f*<sup>′</sup> + *b*<sup>2</sup>(4 + *b*<sup>2</sup>)*f* = 0

-   We now consider *f* to have the form *f* = *e*<sup>*aξ*</sup> which generates the characteristic equation

(*a*<sup>2</sup> + *b*<sup>2</sup>)(*a*<sup>2</sup> − 4*a* + 4 + *b*<sup>2</sup>)=0

----
## polar coordinates

-   This has solutions

$$\\begin{aligned}
	a &= \\pm ib, \\pm 2ib\\\\
	\\text{OR}\\\\
	b &= \\pm ia, \\pm i(a-2)
\\end{aligned}$$

----
## polar coordinates

-   If we consider only solutions which are periodic in *θ*, we find

$$\\begin{aligned}
	\\phi &= a\_0 + a\_1 \\log r + a\_2 r^2 + a\_3 r^2 \\log r \\\\
	&+ (a\_4 + a\_5 \\log r + a\_6 r^2 + a\_7 r^2 \\log r)\\theta \\\\
	&+ \\left(a\_{11}r + a\_{12}r\\log r + \\frac{a\_{13}}{r} + a\_{14}r^3 + a\_{15}r\\theta + a\_{16} r\\theta \\log r\\right) \\cos \\theta\\\\
	&+  \\left(b\_{11}r + b\_{12}r\\log r + \\frac{b\_{13}}{r} + b\_{14}r^3 + b\_{15}r\\theta + b\_{16} r\\theta \\log r\\right) \\sin \\theta\\\\
	&+ \\sum\_{n=2}^{\\infty} (a\_{n1}r^n + a\_{n2}r^{2+n}+a\_{n3}r^{-n}+a\_{n4}r^{2-n})\\cos n\\theta\\\\
	&+ \\sum\_{n=2}^{\\infty} (b\_{n1}r^n + b\_{n2}r^{2+n}+a\_{n3}r^{-n}+b\_{n4}r^{2-n})\\sin n\\theta\\\\
\\end{aligned}$$

----
## polar coordinates

-   For axisymmetric problems, all field quantities are independent of *θ*
-   This reduces the general solution to

_ϕ_ = *a*<sub>0</sub> + *a*<sub>1</sub>log*r* + *a*<sub>2</sub>*r*<sup>2</sup> + *a*<sub>3</sub>*r*<sup>2</sup>log*r*

----
## polar coordinates

![table with pre-calculated airy stress terms in polar coordinates](../images/polar-table1.png)

----
## polar coordinates

![continued table of polar coordinate airy stress terms](../images/polar-table2.png)

---
# examples

----
## tube under uniform pressure

![tube under uniform pressure](../images/tube.PNG) <!-- .element width="40%" -->

----
## pressurized hole

![pressurized hole](../images/pressure_hole.PNG) <!-- .element width="50%" -->

----
## stress-free hole in tension

![hole in tension](../images/tension_hole.PNG) <!-- .element width="60%" -->

----
## stress-free hole in tension

![plot of stress around hole](../images/plot.PNG) <!-- .element width="50%" -->

----
## concentrated force

![concentrated force problem](../images/concentrated.PNG) <!-- .element width="50%" -->

----
## concentrated force

![flamant solution](../images/flamant1.PNG) <!-- .element width="60%" -->

----
## concentrated force

![flamant solution](../images/flamant2.PNG) <!-- .element width="60%" -->

----
## wedge

![wedge problem](../images/wedge.PNG) <!-- .element width="50%" -->

----
## notch/crack

![notch or crack problem](../images/crack.PNG) <!-- .element width="60%" -->

----
## curved beam

![solution for a curved beam](../images/curved_beam.PNG)

----
## rotating disk

![rotating disk problem](../images/rotating_disk.PNG)
