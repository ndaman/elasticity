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

* polar coordinate solutions
* examples

<!-- vim-markdown-toc -->

---
# polar coordinate solutions

----
## polar coordinates

-   Recall that an Airy Stress function must satisfy the Beltrami-Mitchell compatibility equations

$$\\nabla^4 \\phi = \\left(\\frac{\\partial ^2}{\\partial r^2} + \\frac{1}{r} \\frac{\\partial}{\\partial r} + \\frac{1}{r^2}\\frac{\\partial ^2}{\\partial \\theta^2}\\right)^2\\phi = 0$$

-   One method which gives several useful solutions assumes that the Airy Stress function has the form *ϕ*(*r*, *θ*)=*f*(*r*)*e*<sup>*bθ*</sup>
-   Substituting this into the compatibility equations (and canceling the common *e*<sup>*bθ*</sup>) term gives

$$f^{\\prime \\prime \\prime \\prime} + \\frac{2}{r} f^{\\prime \\prime \\prime} - \\frac{1-2b^2}{r^2}f^{\\prime \\prime} + \\frac{1-2b^2}{r^3}f^{\\prime} + \\frac{b^2(4+b^2)}{r^4}f = 0$$

----
## polar coordinates

-   To solve this, we perform a change of variables, letting *r* = *e*<sup>*ξ*</sup>, which gives

_f_<sup>′′′′</sup> − 4*f*<sup>′′′</sup> + (4 + 2*b*<sup>2</sup>)*f*<sup>′′</sup> − 4*b*<sup>2</sup>*f*<sup>′</sup> + *b*<sup>2</sup>(4 + *b*<sup>2</sup>)*f* = 0

-   We know consider *f* to have the form *f* = *e*<sup>*aξ*</sup> which generates the characteristic equation

(*a*<sup>2</sup> + *b*<sup>2</sup>)(*a*<sup>2</sup> − 4*a* + 4 + *b*<sup>2</sup>)=0

-   And has solutions

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

![polar coordinate table of airy stress terms](../images/polar-table1.png)

----
## polar coordinate

![second page of polar coordinate table of airy stress terms](../images/polar-table2.png)

---
# examples

----
## tube under uniform pressure

![tube under uniform pressure](../images/tube.PNG)

----
## pressurized hole

![pressurized hole](../images/pressure_hole.PNG)

----
## stress-free hole in tension

![hole in tension](../images/tension_hole.PNG)

----
## stress-free hole in tension

![plot of stress around hole](../images/plot.PNG)

----
## concentrated force

![concentrated force problem](../images/concentrated.PNG)

----
## concentrated force

![flamant solution](../images/flamant1.PNG)

----
## concentrated force

![flamant solution](../images/flamant2.PNG)

----
## wedge

![wedge problem](../images/wedge.PNG)

----
## notch/crack

![notch or crack problem](../images/crack.PNG)

----
## curved beam

![solution for a curved beam](../images/curved_beam.PNG)

----
## rotating disk

![rotating disk problem](../images/rotating_disk.PNG)
