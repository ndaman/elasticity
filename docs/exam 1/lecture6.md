<span>upcoming schedule</span>

-   Sep 11 - Displacement and Strain

-   Sep 13 - Displacement and Strain

-   Sep 18 - Exam Review, Homework 2 Due

-   Sep 20 - Exam 1

### outline

\[sections numbered\]

example
=======

<span>example</span>

-   Calculate the deformation gradient, strain tensor, and rotation tensor for the given deformation
    $$\\begin{Bmatrix}
            u\_1 \\\\ u\_2 \\\\ u\_3
            \\end{Bmatrix} = \\begin{Bmatrix}
            xy^2z \\\\ xz \\\\ z^3
            \\end{Bmatrix}$$

-   Deformation gradient:
    $$F = u\_{i,j} = \\begin{bmatrix}
            y^2 z & 2 xyz & xy^2\\\\
            z & 0 & x\\\\
            0 & 0 & 3z^2
            \\end{bmatrix}$$

<span>example</span>

-   Strain tensor
    $$e\_{ij} = \\frac{1}{2}(u\_{i,j} + u\_{j,i})$$
    $$e\_{ij} = \\begin{bmatrix}
            y^2 z & xyz + \\frac{1}{2}z & \\frac{1}{2}xy^2\\\\
            xyz + \\frac{1}{2}z & 0 & \\frac{1}{2}x\\\\
            \\frac{1}{2}xy^2 & \\frac{1}{2}x & 3z^2
            \\end{bmatrix}$$

<span>example</span>

-   Rotation tensor
    $$\\omega\_{ij} = \\frac{1}{2}(u\_{i,j} - u\_{j,i})$$
    $$\\omega\_{ij} = \\begin{bmatrix}
            0 & xyz - \\frac{1}{2}z & \\frac{1}{2}xy^2\\\\
            -xyz + \\frac{1}{2}z & 0 & \\frac{1}{2}x\\\\
            -\\frac{1}{2}xy^2 & -\\frac{1}{2}x & 0
            \\end{bmatrix}$$

<span>example</span>

-   As we did with the deformation gradient, we can integrate the strain tensor to find the deformation (symmetric portion)
    $$e\_{ij} = \\begin{bmatrix}
            yz & xz & xy\\\\
            xz & 2y & \\frac{1}{2}x^2\\\\
            xy & \\frac{1}{2}x^2 & 3z^2
            \\end{bmatrix}$$

-   We start by integrating the diagonal terms
    *u* = ∫*y**z**d**x* = *x**y**z* + *f*(*y*, *z*)
    *v* = ∫2*y**d**y* = *y*<sup>2</sup> + *g*(*x*, *z*)
    *w* = ∫3*z*<sup>2</sup>*d**z* = *z*<sup>3</sup> + *h*(*x*, *y*)

<span>example</span>

-   Next we need to find the shear terms
    $$\\begin{aligned}
            e\_{xy} &= \\frac{1}{2}(u\_{,y}+v\_{,x})\\\\
            xz &= \\frac{1}{2}(xz + f\_{,y} + g\_{,x})
            \\end{aligned}$$
    $$\\begin{aligned}
            e\_{xz} &= \\frac{1}{2}(u\_{,z}+w\_{,x})\\\\
            xy &= \\frac{1}{2}(xy + f\_{,z} + h\_{,x})
            \\end{aligned}$$
    $$\\begin{aligned}
            e\_{yz} &= \\frac{1}{2}(v\_{,z}+w\_{,y})\\\\
            \\frac{1}{2}x^2 &= \\frac{1}{2}(g\_{,z} + h\_{,y})
            \\end{aligned}$$

<span>example</span>

-   Note that we cannot uniquely solve this (any arbitrary rotation *ω* can be added and will still produce a valid strain)

-   Let *f*(*y*, *z*)=0
    $$\\begin{aligned}
            g\_{,x} &= xz\\\\
            g(x,z) &= \\frac{1}{2}x^2 z
            \\end{aligned}$$
    $$\\begin{aligned}
            h\_{,x} &= xy \\\\
            h(x,z) &= \\frac{1}{2}x^2 y
            \\end{aligned}$$

<span>example</span>
$$\\begin{aligned}
            \\frac{1}{2}x^2 &= \\frac{1}{2} \\left(g\_{,z} + h\_{,y}\\right)\\\\
            \\frac{1}{2}x^2 &= \\frac{1}{2} \\left(\\frac{1}{2}x^2 + \\frac{1}{2}x^2\\right)
            \\end{aligned}$$
$$\\begin{aligned}
            u &= xyz\\\\
            v &= y^2 + \\frac{1}{2}x^2z\\\\
            w &= z^3 + \\frac{1}{2}x^2y
            \\end{aligned}$$

group problems
==============

<span>group 1</span>

-   Sketch the deformed and undeformed shape of a rectangle under the following deformation
    $$\\begin{aligned}
            u &= 0.7x + 0.1y\\\\
            v &= 0.3x + 1.2y
            \\end{aligned}$$

<span>group 2</span>

-   For the following deformation, find the deformation gradient, strain, and rotation
    $$\\begin{aligned}
        u &= xyz\\\\
        v &= xy + z\\\\
        z &= y^2z
        \\end{aligned}$$

<span>group 3</span>

-   From the following strain field, find the displacements (you may assume no rotations)
    $$\\epsilon\_{ij} = \\begin{bmatrix}
            y & x + y \\\\
            x + y & x
        \\end{bmatrix}$$

Principal strains
=================

<span>principal strains</span>

-   Principal strains are found in exactly the same way as principal values discussed in Chapter 1
    det\[*e*<sub>*i**j*</sub> − *e**δ*<sub>*i**j*</sub>\]=0

-   Invariants can also be found in the same fashion as in any other tensor
    $$\\begin{aligned}
            \\vartheta\_1 &= e\_1 + e\_2 + e\_3\\\\
            \\vartheta\_2 &= e\_1 e\_2 + e\_2 e\_3 + e\_3 e\_1\\\\
            \\vartheta\_3 &= e\_1 e\_2 e\_3
            \\end{aligned}$$

<span>principal strains</span>

-   Principal strains and invariants have some important physical meanings

-   *ϑ*<sub>1</sub> is called the *cubical dilation*, and is related to the change in volume of the material

-   Note that in the principal direction, there are no shear strains
    $$\\begin{bmatrix}
            e\_1 & 0 & 0\\\\
            0 & e\_2 & 0 \\\\
            0 & 0 & e\_3
            \\end{bmatrix}$$

-   This means that there is only extensional strain in the principal direction (i.e. a cube will remain a rectangular prism, the corners will maintain 90<sup>∘</sup> angles)

<span>volume change</span>

-   Consider a rectangular prism with edges oriented in the principal directions

    (0,0,0) – (2,0,0) node\[below left\] <span>*x*<sub>1</sub></span>; (0,0,0) – (0,2,0) node\[right\] <span>*x*<sub>2</sub>, *x*<sub>2</sub><sup>′</sup></span>; (0,0,0) – (0,0,2) node\[above\] <span>*x*<sub>3</sub></span>; ; (0,0,0) – (1,0,0) – (1,1,0) – (0,1,0) – (0,0,0); (0,0,1) – (1,0,1) – (1,1,1) – (0,1,1) – (0,0,1); (0,0,0) – (0,0,1); (1,0,0) – (1,0,1); (1,1,0) – (1,1,1); (0,1,0) – (0,1,1); (0,0,0) – (2,0,0) – (2,2,0) – (0,2,0) – (0,0,0); (0,0,2) – (2,0,2) – (2,2,2) – (0,2,2) – (0,0,2); (0,0,0) – (0,0,2); (2,0,0) – (2,0,2); (2,2,0) – (2,2,2); (0,2,0) – (0,2,2); node at (1.2,0.5,0) <span>*W*</span>; node at (2.2,1,0) <span>*W*<sup>′</sup></span>; node at (0,1.2,0.5) <span>*H*</span>; node at (0,2.2,1) <span>*H*<sup>′</sup></span>; node at (0.5,0,1.2) <span>*L*</span>; node at (1,0,2.2) <span>*L*<sup>′</sup></span>;

<span>volume change</span>

-   The volume before deformation is *V* = *L**W**H*

-   The volume after deformation is given by *V*<sup>′</sup> = *L*<sup>′</sup>*W*<sup>′</sup>*H*<sup>′</sup>

-   We can relate the side lengths after deformation to strains
    $$e\_1 = \\frac{L^\\prime - L}{L}$$
    *L**e*<sub>1</sub> + *L* = *L*<sup>′</sup>

-   We can now write the volume as *V*<sup>′</sup> = *L*(1 + *e*<sub>1</sub>)*W*(1 + *e*<sub>2</sub>)*H*(1 + *e*<sub>3</sub>)

<span>volume change</span>

-   After multiplication, the deformed volume is given as
    *V*<sup>′</sup> = *L**W**H*(1 + *e*<sub>1</sub> + *e*<sub>2</sub> + *e*<sub>3</sub> + *e*<sub>1</sub>*e*<sub>2</sub> + *e*<sub>2</sub>*e*<sub>3</sub> + *e*<sub>1</sub>*e*<sub>3</sub> + *e*<sub>1</sub>*e*<sub>2</sub>*e*<sub>3</sub>)

-   For small strains, *e*<sub>*i*</sub> ≪ 1, therefore *e*<sub>1</sub>, *e*<sub>2</sub>, and *e*<sub>3</sub> will be much larger than *e*<sub>1</sub>*e*<sub>2</sub>, *e*<sub>2</sub>*e*<sub>3</sub>, *e*<sub>1</sub>*e*<sub>3</sub> and *e*<sub>1</sub>*e*<sub>2</sub>*e*<sub>3</sub>.
    *V*<sup>′</sup> = *L**W**H*(1 + *e*<sub>1</sub> + *e*<sub>2</sub> + *e*<sub>3</sub>)

<span>volume change</span>

-   A “dilatation” is defined as the change in volume divided by the original volume
    $$\\frac{\\Delta V}{V} = \\frac{V^\\prime - V}{V}$$

-   Substituting the relationships found earlier
    $$\\frac{V^\\prime - V}{V} = \\frac{LWH(1+e\_1+e\_2+e\_3) - LWH}{LWH}$$

-   Which simplifies to
    *e*<sub>1</sub> + *e*<sub>2</sub> + *e*<sub>3</sub> = *ϑ*<sub>1</sub>

Spherical and deviatoric strains
================================

<span>spherical strain</span>

-   This dilatation can be used to find the so-called *spherical strain*
    $$\\begin{aligned}
            \\tilde{e}\_{ij} = \\frac{1}{3} e\_{kk} \\delta\_{ij} = \\frac{1}{3} \\vartheta\_1 \\delta\_{ij}
            \\end{aligned}$$

-   The *deviatoric strain* is found by subtracting the spherical strain from the strain tensor
    $$\\hat{e}\_{ij} = e\_{ij} - \\frac{1}{3} e\_{kk} \\delta\_{ij}$$

Strain transformation
=====================

<span>strain transformation</span>

-   The usual tensor transformation applies to the strain tensor as well
    *e*<sub>*i**j*</sub><sup>′</sup> = *Q*<sub>*i**m*</sub>*Q*<sub>*j**n*</sub>*e*<sub>*m**n*</sub>

-   In many instances, however, we are only concerned with the strain within a plane (for example, when using strain gages).

-   For an in-plane rotation (rotation about *z*-axis), we find
    $$Q\_{ij} = \\begin{bmatrix}
            \\cos \\theta & \\cos (90-\\theta) & \\cos 90\\\\
            \\cos (90+\\theta) & \\cos \\theta & \\cos 90\\\\
            \\cos 90 & \\cos 90 & \\cos 0\\\\
            \\end{bmatrix} = \\begin{bmatrix}
            \\cos \\theta & \\sin \\theta & 0\\\\
            -\\sin \\theta & \\cos \\theta & 0\\\\
            0 & 0 & 1\\\\
            \\end{bmatrix}$$

<span>strain transformation</span>

-   If we multiply this out, for the in-plane strain terms (*e*<sub>*x*</sub><sup>′</sup>, *e*<sub>*x*</sub><sup>′</sup>, and *e*<sub>*x**y*</sub><sup>′</sup>) we find
    $$\\begin{aligned}
            e^\\prime\_x &= e\_x \\cos ^2 \\theta + e\_y \\sin^2 \\theta + 2 e\_{xy} \\sin \\theta \\cos \\theta \\\\
            e^\\prime\_y &= e\_x \\sin ^2 \\theta + e\_y \\cos^2 \\theta - 2 e\_{xy} \\sin \\theta \\cos \\theta \\\\
            e^\\prime\_{xy} &= -e\_x \\sin \\theta \\cos \\theta + e\_y \\sin \\theta \\cos \\theta + e\_{xy} (\\cos^2 \\theta - \\sin^2 \\theta)
            \\end{aligned}$$

-   This is often re-written using the double-angle formulas
    $$\\begin{aligned}
            e^\\prime\_x &= \\frac{e\_x + e\_y}{2} + \\frac{e\_x - e\_y}{2}\\cos 2\\theta + e\_{xy} \\sin 2\\theta \\\\
            e^\\prime\_y &= \\frac{e\_x + e\_y}{2} - \\frac{e\_x - e\_y}{2}\\cos 2\\theta - e\_{xy} \\sin 2\\theta \\\\
            e^\\prime\_{xy} &= \\frac{e\_y - e\_x}{2}\\sin 2\\theta + e\_{xy} \\cos 2\\theta
            \\end{aligned}$$

<span>strain transformation</span>

-   Many times it is easy to measure the axial strain directly with strain gages, but the shear strain cannot be easily measured

-   We can use an extra, off-axis strain gage, together with the strain transformation equations, to calculate the shear strain

-   Many companies already do this with “rosettes” which have strain gages at specified angles built-in

<span>example</span>

(0,0) – (4,0) node\[right\] <span>*x*</span>; (0,0) – (0,2) node\[above\] <span>*y*</span>; (2,.5) to\[\*R=*ϵ*<sub>*b*</sub>\] (2,2.5); (2,.5) to\[\*R=*ϵ*<sub>*c*</sub>\] (0.268,1.5); (2,.5) to\[\*R=*ϵ*<sub>*a*</sub>\] (3.732,1.5);

(1.472,0.85) arc (30:90:1.7) node at (1.,1.7) <span>*θ*<sub>1</sub> = 60<sup>∘</sup></span>; (0,1.5) arc (90:150:1.5) node at (-0.7,1.5) <span>*θ*<sub>2</sub> = 60<sup>∘</sup></span>;

<span>example</span>

-   Given that *ϵ*<sub>*a*</sub> = 0.005, *ϵ*<sub>*b*</sub> = −0.002 and *ϵ*<sub>*c*</sub> = 0.003, find *e*<sub>*x*</sub>, *e*<sub>*y*</sub>, and *e*<sub>*x**y*</sub>.

-   Note that *e*<sub>*y*</sub> = *ϵ*<sub>*b*</sub> = −0.002

-   Set coordinate system so that *ϵ*<sub>*b*</sub> = *e*<sub>*x*</sub><sup>′</sup>.

-   Use equation for *e*<sub>*x*</sub><sup>′</sup> with *θ* = 30.
    $$\\alert{e^\\prime\_x} = \\frac{e\_x + \\alert{e\_y}}{2} + \\frac{e\_x - \\alert{e\_y}}{2}\\cos 60 + e\_{xy} \\sin 60$$

<span>example</span>

-   We have two unknowns in this equation, so we need another

-   We can use the equation for *e*<sub>*y*</sub><sup>′</sup> with *θ* = 60 so that *ϵ*<sub>*b*</sub> = *e*<sub>*x*</sub><sup>′</sup>
    $$\\alert{e^\\prime\_y} = \\frac{e\_x + \\alert{e\_y}}{2} - \\frac{e\_x - \\alert{e\_y}}{2}\\cos 120 - e\_{xy} \\sin 120$$

-   Substituting known values and simplifying:
    $$\\begin{aligned}
            0.01 + 0.002 - 0.002 \\cos 60 &= e\_x (1+\\cos 60) + e\_{xy} \\sin 60 \\\\
            0.006 + 0.002 + 0.002 \\cos 120 &= e\_x (1-\\cos 120) - e\_{xy} \\sin 120
            \\end{aligned}$$

-   And solving we find *e*<sub>*x*</sub> = 0.006, *e*<sub>*y*</sub> = −0.002, and *e*<sub>*x**y*</sub> = 0.00231.


