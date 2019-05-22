<span>upcoming schedule</span>

-   Sep 6 - Homework 1 Due, Displacement and Strain

-   Sep 11 - Displacement and Strain

-   Sep 13 - Displacement and Strain

-   Sep 18 - Exam Review, Homework 2 Due

-   Sep 20 - Exam 1

### outline

\[sections numbered\]

Chapter outline
===============

<span>chapter outline</span>

-   General description of deformations

-   Assumptions for small deformations

-   Definition of strain

-   Strain transformation

-   Principal strains

-   Strain compatibility

-   Strain in cylindrical and spherical coordinates

General deformations
====================

<span>general deformation</span>

-   When deformations are large, the deformed and un-deformed shapes can be quite different

-   It can be convenient to refer to material properties in the deformed or un-deformed configuration

-   Lagrangian reference: quantities are in terms of the original (un-deformed) configuration

-   Eulerian reference: quantities are in terms of deformed configuration

<span>material derivatives</span>

-   We refer to the undeformed configuration as *x*<sub>*i*</sub><sup>0</sup> and the deformed configuration as *x*<sub>*i*</sub>

-   If some quantity, *ϕ* is expressed in the undeformed configuration as *ϕ*(*x*<sub>1</sub><sup>0</sup>, *x*<sub>2</sub><sup>0</sup>, *x*<sub>3</sub><sup>0</sup>, *t*) then the material derivative is
    $$\\frac{d\\phi}{dt} = \\frac{\\partial \\phi}{\\partial t}$$

-   However in Eulerian form $\\bar{\\phi} (x\_1, x\_2, x\_3, t) = \\phi(x\_1^0,x\_2^0,x\_3^0,t)$ the material derivative becomes
    $$\\frac{d\\bar{\\phi}}{dt} = \\frac{\\partial \\bar{\\phi}}{\\partial t} + \\frac{\\partial \\bar{ \\phi}}{\\partial x\_j}\\frac{d x\_j}{dt}$$

<span>deformation</span>

-   A *deformation* is a comparison of two states. The deformation of a material point is expressed as
    $$\\begin{gathered}
            x\_i = x\_i(x\_1^0, x\_2^0, x\_3^0) \\quad \\text{or} \\quad x\_i^0 = x\_i^0(x\_1, x\_2, x\_3)
            \\end{gathered}$$

-   For example, consider the 2D deformation
    $$\\begin{gathered}
            \\begin{Bmatrix}
            x\_1 \\\\ x\_2
            \\end{Bmatrix} =
            \\begin{Bmatrix}
            2 x\_1^0 \\\\ x\_2^0
            \\end{Bmatrix} \\quad \\text{or} \\quad
            \\begin{Bmatrix}
            x\_1^0 \\\\ x\_2^0
            \\end{Bmatrix}
             = \\begin{Bmatrix}
             \\frac{1}{2} x\_1 \\\\ x\_2
             \\end{Bmatrix}
            \\end{gathered}$$

    (0,0) – (0,2); (0,0) – (3,0); (0,0) – (1,0) node\[below\] <span>*x*<sub>1</sub><sup>0</sup></span> – (1,1) – (0,1) node\[left\] <span>*x*<sub>2</sub><sup>0</sup></span> – (0,0); (1,1) – (2,1) node\[right\] <span>*x*<sub>2</sub></span> – (2,0) node\[below\] <span>*x*<sub>1</sub></span>;

<span>displacement</span>

-   A displacement is the shortest distance traveled when a particle moves from one location to another

-   Displacement is identical in Eulerian and Lagrangian descriptions
    *u*<sub>*i*</sub> = (*x*<sub>*i*</sub> − *x*<sub>*i*</sub><sup>0</sup>)

    (0,0) – (0,2); (0,0) – (3,0); (0,0) – (1,0) – (1,1) – (0,1) – (0,0); (1,1) – (2,1) – (2,0); (0.75,0.5) circle (2pt) node\[above\] <span>*P*<sup>0</sup></span>; (1.5,0.5) circle (2pt) node\[above\] <span>*P*</span>; (0.75,0.5) – (1.5,0.5) node\[below left\] <span>*u*<sub>*i*</sub></span>;

Small deformation theory
========================

<span>deformation gradients</span>

plot \[smooth cycle\] coordinates <span>(5,0.25) (6,0.35) (6.5, 0.2) (7,0.5) (7,1.65) (6.5,2.75) (5.8,2.75) (5.3,1.45) (4.8,0.85) </span> node at (6,1.7) <span>*D*′</span>; (3.1,1.7) edge \[bend left\] node\[above\] <span>*φ*</span> (5.0,1.7); plot \[smooth cycle\] coordinates <span>(1.0,.1)(1.5,.2)(2.8,.5)(2.9,1.5)(2.8,2.8)(1.4,2.5)(0.5,0.5)</span> node at (1.8,1.7) <span>*D*</span>; (1.5,0.5) – (2.45,0.88) node at (1.9,0.9) <span>*d**x*<sub>*i*</sub><sup>0</sup></span>; (1.5,0.5) circle (2pt) node at (1.2,0.4) <span>*P*<sub>0</sub></span>; (2.5,0.9) circle (2pt) node at (2.7,0.95) <span>*P*</span>; (5.5,0.9) – (6.4,0.6) node at (6.0,1.0) <span>*d**x*<sub>*i*</sub></span>; (5.5,0.9) circle (2pt) node at (5.2,1.0) <span>*P*<sub>0</sub><sup>′</sup></span>; (6.45,0.59) circle (2pt) node at (6.7,0.59) <span>*P*<sup>′</sup></span>;

<span>deformation gradients</span>

-   The position of the two points, *P*<sub>0</sub><sup>′</sup> and *P*<sup>′</sup>, is related by
    $$\\begin{aligned}
            P\_0^\\prime &= x\_i (x\_i^0) &\\\\
            P^\\prime &= x\_i + dx\_i &=x\_i(x\_i^0 + dx\_i^0)
            \\end{aligned}$$

-   We can approximate *x*<sub>*i*</sub>(*x*<sub>*i*</sub><sup>0</sup> + *d**x*<sub>*i*</sub><sup>0</sup>) with a Taylor series expansion
    $$\\approx x\_i (x\_i^0) + \\frac{\\partial x\_i^0}{\\partial x\_j} dxj^0 + \\frac{1}{2}\\frac{\\partial^2x\_i}{\\partial x\_j^0 \\partial x\_k^0} dx\_j^0 dx\_k^0 + ...$$

<span>deformation gradients</span>

-   If the deformation is small, we can neglect higher-order terms of the expansion
    $$P^\\prime = x\_i + dx\_i = x\_i (x\_i^0) + \\frac{\\partial x\_i^0}{\\partial x\_j} dxj^0$$

-   Which gives
    $$dx\_i = \\frac{\\partial x\_i^0}{\\partial x\_j} dx\_j^0$$

<span>deformation gradients</span>

-   In index notation we write displacements as *u*<sub>*i*</sub>

-   The deformation gradient can be written in this notation as
    $$F = u\_{i,j} = \\begin{bmatrix}
            \\frac{\\partial u\_1}{\\partial x\_1} & \\frac{\\partial u\_1}{\\partial x\_2} & \\frac{\\partial u\_1}{\\partial x\_3}\\\\
            \\frac{\\partial u\_2}{\\partial x\_1} & \\frac{\\partial u\_2}{\\partial x\_2} & \\frac{\\partial u\_2}{\\partial x\_3}\\\\
            \\frac{\\partial u\_3}{\\partial x\_1} & \\frac{\\partial u\_3}{\\partial x\_2} & \\frac{\\partial u\_3}{\\partial x\_3}
            \\end{bmatrix}$$

<span>translation</span>

(0,0) – (0,3); (0,0) – (3,0); (0,0) – (1,0) – (1,1) – (0,1) – (0,0); (2,2) – (2,3) – (3,3) – (3,2) – (2,2); (0,2.5) – (2,2.5) node at (1,2.8) <span>*A*</span>; (2.5,0) – (2.5,2) node at (2.8,1) <span>*B*</span>;

-   x-displacement
    *u*<sub>1</sub> = *x*<sub>1</sub><sup>0</sup> + *A*

-   y-displacement
    *u*<sub>2</sub> = *x*<sub>2</sub><sup>0</sup> + *B*

<span>translation</span>

-   Deformation gradient
    $$F = u\_{i,j} = \\begin{bmatrix}
            \\frac{\\partial u\_1}{\\partial x\_1} & \\frac{\\partial u\_1}{\\partial x\_2}\\\\
            \\frac{\\partial u\_2}{\\partial x\_1} & \\frac{\\partial u\_2}{\\partial x\_2}   \\end{bmatrix}$$
    $$F = \\begin{bmatrix}
            1 & 0 \\\\ 0 & 1
            \\end{bmatrix}$$

<span>rotation</span>

(0,0) – (0,2); (0,0) – (2,0); (0,0) – (1,0) – (1,1) – (0,1) – (0,0); (0,0) – (-.707,.707) – (0,1.414) – (0.707,0.707) – (0,0); (0.5,0) arc (0:45:0.5) node (theta) \[below right = -0.1cm and 0.3cm\] <span>*θ*</span>;

-   x-displacement
    *u*<sub>1</sub> = *x*<sub>1</sub><sup>0</sup>cos*θ* − *x*<sub>2</sub><sup>0</sup>sin*θ*

-   y-displacement
    *u*<sub>2</sub> = *x*<sub>1</sub><sup>0</sup>sin*θ* + *x*<sub>2</sub><sup>0</sup>cos*θ*

<span>rotation</span>

-   Deformation gradient
    $$F = u\_{i,j} = \\begin{bmatrix}
            \\frac{\\partial u\_1}{\\partial x\_1} & \\frac{\\partial u\_1}{\\partial x\_2}\\\\
            \\frac{\\partial u\_2}{\\partial x\_1} & \\frac{\\partial u\_2}{\\partial x\_2}   \\end{bmatrix}$$
    $$F = \\begin{bmatrix}
            \\cos \\theta & -\\sin \\theta \\\\ \\sin \\theta & \\cos \\theta
            \\end{bmatrix}$$

<span>simple shear</span>

(0,0) – (0,2); (0,0) – (2,0); (0,0) – (1,0) – (1,1) – (0,1) – (0,0); (0,0) – (0.5,1) – (1.5,1) – (1,0) – (0,0);

-   x-displacement
    $$u\_1 = x\_1^0 + \\frac{1}{2} x\_2^0$$

-   y-displacement
    *u*<sub>2</sub> = *x*<sub>2</sub><sup>0</sup>

<span>simple shear</span>

-   Deformation gradient
    $$F = u\_{i,j} = \\begin{bmatrix}
            \\frac{\\partial u\_1}{\\partial x\_1} & \\frac{\\partial u\_1}{\\partial x\_2}\\\\
            \\frac{\\partial u\_2}{\\partial x\_1} & \\frac{\\partial u\_2}{\\partial x\_2}   \\end{bmatrix}$$
    $$F = \\begin{bmatrix}
            1 & \\frac{1}{2} \\\\ 0 & 1
            \\end{bmatrix}$$

<span>pure shear</span>

-   Sometimes it is important to eliminate rotations

-   We can design an experiment with a state of pure shear by inducing this deformation
    $$F = \\begin{bmatrix}
            1 & \\frac{1}{2} \\\\ \\frac{1}{2} & 1
            \\end{bmatrix}$$

-   We can integrate our usual relationship to find *u*<sub>1</sub> and *u*<sub>2</sub>

<span>pure shear</span>
$$\\frac{\\partial u\_1}{\\partial x\_1} = 1$$
*u*<sub>1</sub> = *x*<sub>1</sub> + *f*(*x*<sub>2</sub>)
$$\\frac{\\partial u\_1}{\\partial x\_2} = \\frac{1}{2}$$
$$\\frac{\\partial f}{\\partial x\_2} = \\frac{1}{2}$$
$$u\_1 = x\_1 + \\frac{1}{2} x\_2$$

<span>pure shear</span>
$$\\frac{\\partial u\_2}{\\partial x\_2} = 1$$
*u*<sub>2</sub> = *x*<sub>2</sub> + *g*(*x*<sub>1</sub>)
$$\\frac{\\partial u\_2}{\\partial x\_1} = \\frac{1}{2}$$
$$\\frac{\\partial g}{\\partial x\_1} = \\frac{1}{2}$$
$$u\_2 = x\_2 + \\frac{1}{2} x\_1$$

<span>pure shear</span>

(0,0) – (0,2); (0,0) – (2,0); (0,0) – (1,0) – (1,1) – (0,1) – (0,0); (0,0) – (1,0.5) – (1.5,1.5) – (0.5,1) – (0,0);

Strain
======

<span>strain definition</span>

-   We can separate the deformation gradient into symmetric and antisymmetric parts
    *u*<sub>*i*, *j*</sub> = *e*<sub>*i**j*</sub> + *ω*<sub>*i**j*</sub>

-   Where
    $$\\begin{aligned}
            e\_{ij} &= \\frac{1}{2}(u\_{i,j} + u\_{j,i})\\\\
            \\omega\_{ij} &= \\frac{1}{2}(u\_{i,j} - u\_{j,i})
            \\end{aligned}$$

-   *e*<sub>*i**j*</sub> is known as the strain tensor

-   *ω*<sub>*i**j*</sub> is known as the rotation tensor

<span>geometric description of strain</span>

-   Strain definitions

-   Engineering strain
    $$e^E = \\frac{\\Delta L}{L\_0}$$

-   True strain
    $$e^T = \\frac{\\Delta L}{L\_0 + \\Delta L}$$

-   Logarithmic strain
    $$e^L = \\int\_{L\_0}^L e^T = \\int\_{L\_0}^L \\frac{dl}{l} = \\ln \\left(\\frac{L}{L\_0}\\right)$$

<span>geometric description of strain</span>

-   Large strain: *Δ**L* = *L*<sub>0</sub>
    $$\\begin{aligned}
                e^E &= 1.00\\\\
                e^T &= 0.50\\\\
                e^L &= 0.69
            \\end{aligned}$$

-   Small strain: *Δ**L* = 0.05*L*<sub>0</sub>
    $$\\begin{aligned}
                e^E &= 0.050\\\\
                e^T &= 0.048\\\\
                e^L &= 0.049
            \\end{aligned}$$

<span>geometric description of strain</span>

(0,0) – (3,0); (0,0) – (0,3); (0.5,0.5) node\[above right\] <span>*A*</span> – (1.5,0.5) node\[above left\] <span>*B*</span> – (1.5,1.5) node\[below left\] <span>*C*</span> – (0.5,1.5) node\[below right\] <span>*D*</span> – (0.5,0.5); node at (1.0,0.65) <span>*d**x*</span>; node at (0.65,1) <span>*d**y*</span>; (1.8,1.8) node\[above right\] <span>*A*<sup>′</sup></span> – (3.0,2.1) node\[above left\] <span>*B*<sup>′</sup></span>– (3.3,3.3) node\[below left\] <span>*C*<sup>′</sup></span> – (2.1,3.0) node\[below right\] <span>*D*<sup>′</sup></span> – (1.8,1.8); (0.5,0.25) – (1.8,0.25); (0.5,0.5) – (0.5,0.1); (1.8,1.8) – (1.8,0.1); node at (1.1,0.1) <span>*u*(*x*, *y*)</span>; (1.5,0.5) – (3.0,0.5); (3.0,2.1) – (3.0,0.35); node at (2.25,0.35) <span>*u*(*x* + *d**x*, *y*)</span>; (0.5,0.5) – (0.1,0.5); (1.8,1.8) – (0.1,1.8); (0.25,1.4) – (0.25,1.8); (0.25,0.9) – (0.25,0.5); node at (0.25,1.1) <span>*v*(*x*, *y*)</span>; (0.5,1.9) – (0.5,1.5); (0.5,2.6) – (0.5,3.0); node at (0.5,2.2) <span>*v*(*x*, *y* + *d**y*)</span>; (0.35,3.0) – (2.1,3.0); (1.8,1.8) – (3.2,1.8); (1.8,1.8) – (1.8,3.2);

(1.0,0) arc (0:14:1.0) node (theta) \[below right\] <span>*α*</span>; (0,1.0) arc (90:76:1.0) node (theta) \[above left\] <span>*β*</span>;

(3.1,1.8) – (3.1,2.1); (3.0,2.1) – (3.2,2.1); node at (3.4,1.95) <span>$\\frac{\\partial v}{\\partial x}dx$</span>; (2.1,3.0) – (2.1,3.2); (1.8,3.1) – (2.1,3.1); node at (2,3.3) <span>$\\frac{\\partial u}{\\partial y}dy$</span>;

<span>geometric description of strain</span>

-   The extensional strain in the x-direction (engineering strain) is defined by
    $$\\varepsilon\_x = \\frac{A^\\prime B^\\prime - AB}{AB}$$

-   From geometry, we can write *A*<sup>′</sup>*B*<sup>′</sup> as
    $$\\begin{aligned}
            A^\\prime B^\\prime &= \\sqrt{\\left(dx + \\frac{\\partial u}{\\partial x}dx\\right)^2 + \\left(\\frac{\\partial v}{\\partial x}dx\\right)^2} \\\\
            &= dx \\sqrt{1 + 2\\frac{\\partial u}{\\partial x} + \\left(\\frac{\\partial u}{\\partial x}\\right)^2+ \\left(\\frac{\\partial v}{\\partial x}\\right)^2}
            \\end{aligned}$$

-   For small deformation, we assume $\\frac{\\partial v}{\\partial x}$ is small when compared with $\\frac{\\partial u}{\\partial x}$, which gives
    $$A^\\prime B^\\prime = \\left(1 + \\frac{\\partial u}{\\partial x}\\right)dx$$

<span>geometric description of strain</span>
$$\\begin{aligned}
    \\varepsilon\_x &= \\frac{A^\\prime B^\\prime - AB}{AB} = \\frac{\\left(1 + \\frac{\\partial u}{\\partial x}\\right)dx - dx}{dx} \\\\
    &= \\frac{\\partial u}{\\partial x}
    \\end{aligned}$$

-   The normal strain in the y-direction is found the same way
    $$\\varepsilon\_y = \\frac{\\partial v}{\\partial y}$$

<span>geometric description of strain</span>

(0,0) – (3,0); (0,0) – (0,3); (0.5,0.5) node\[above right\] <span>*A*</span> – (1.5,0.5) node\[above left\] <span>*B*</span> – (1.5,1.5) node\[below left\] <span>*C*</span> – (0.5,1.5) node\[below right\] <span>*D*</span> – (0.5,0.5); node at (1.0,0.65) <span>*d**x*</span>; node at (0.65,1) <span>*d**y*</span>; (1.8,1.8) node\[above right\] <span>*A*<sup>′</sup></span> – (3.0,2.1) node\[above left\] <span>*B*<sup>′</sup></span>– (3.3,3.3) node\[below left\] <span>*C*<sup>′</sup></span> – (2.1,3.0) node\[below right\] <span>*D*<sup>′</sup></span> – (1.8,1.8); (0.5,0.25) – (1.8,0.25); (0.5,0.5) – (0.5,0.1); (1.8,1.8) – (1.8,0.1); node at (1.1,0.1) <span>*u*(*x*, *y*)</span>; (1.5,0.5) – (3.0,0.5); (3.0,2.1) – (3.0,0.35); node at (2.25,0.35) <span>*u*(*x* + *d**x*, *y*)</span>; (0.5,0.5) – (0.1,0.5); (1.8,1.8) – (0.1,1.8); (0.25,1.4) – (0.25,1.8); (0.25,0.9) – (0.25,0.5); node at (0.25,1.1) <span>*v*(*x*, *y*)</span>; (0.5,1.9) – (0.5,1.5); (0.5,2.6) – (0.5,3.0); node at (0.5,2.2) <span>*v*(*x*, *y* + *d**y*)</span>; (0.35,3.0) – (2.1,3.0); (1.8,1.8) – (3.2,1.8); (1.8,1.8) – (1.8,3.2);

(1.0,0) arc (0:14:1.0) node (theta) \[below right\] <span>*α*</span>; (0,1.0) arc (90:76:1.0) node (theta) \[above left\] <span>*β*</span>;

(3.1,1.8) – (3.1,2.1); (3.0,2.1) – (3.2,2.1); node at (3.4,1.95) <span>$\\frac{\\partial v}{\\partial x}dx$</span>; (2.1,3.0) – (2.1,3.2); (1.8,3.1) – (2.1,3.1); node at (2,3.3) <span>$\\frac{\\partial u}{\\partial y}dy$</span>;

<span>geometric description of strain</span>

-   Engineering shear strain is defined as the change in angle between two originally orthogonal directions
    $$\\gamma\_{xy} = \\frac{\\pi}{2} - \\angle D^\\prime A^\\prime B^\\prime = \\alpha + \\beta$$

-   For small strains, *α* ≈ tan*α* and *β* ≈ tan*β*.
    $$\\begin{aligned}
            \\gamma\_{xy} &= \\frac{\\frac{\\partial v}{\\partial x}dx}{dx + \\frac{\\partial u}{\\partial x dx}} + \\frac{\\frac{\\partial u}{\\partial y}dy}{dy + \\frac{\\partial v}{\\partial y dx}}\\\\
            &\\approx \\frac{\\partial u}{\\partial y} + \\frac{\\partial v}{\\partial x}
            \\end{aligned}$$

<span>geometric description of strain</span>

-   The other shear terms can be found in the same way
    $$\\begin{aligned}
            \\gamma\_{xy} &= \\frac{\\partial u}{\\partial y} + \\frac{\\partial v}{\\partial x}\\\\
            \\gamma\_{xz} &= \\frac{\\partial u}{\\partial z} + \\frac{\\partial w}{\\partial x}\\\\
            \\gamma\_{yz} &= \\frac{\\partial v}{\\partial z} + \\frac{\\partial w}{\\partial y}
            \\end{aligned}$$

-   Engineering strain and tensor strain definitions differ only in shear terms
    $$e\_{ij} = \\frac{1}{2} \\left(u\_{i,j} + u\_{j,i}\\right)$$
    $$e\_{xy} = \\frac{1}{2} \\gamma\_{xy}$$

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

