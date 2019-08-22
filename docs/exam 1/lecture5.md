# AE731
## Theory of Elasticity
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering
Septeber 4, 2019

----
## upcoming schedule

-   Sep 4 - Displacement and Strain, Homework 1 Due
-   Sep 9 - Strain Transformation
-   Sep 11 - Displacement and Strain
-   Sep 16 - Exam Review, Homework 2 Due
-   Sep 18 - Exam 1

----
## outline


<!-- vim-markdown-toc GFM -->

* general deformation
* small deformation theory
* strain

<!-- vim-markdown-toc -->

----
## chapter outline

-   General description of deformations
-   Assumptions for small deformations
-   Definition of strain
-   Strain transformation
-   Principal strains
-   Strain compatibility
-   Strain in cylindrical and spherical coordinates

---
# general deformation

----
## general deformation

-   When deformations are large, the deformed and un-deformed shapes can be quite different
-   It can be convenient to refer to material properties in the deformed or un-deformed configuration
-   Lagrangian reference: quantities are in terms of the original (un-deformed) configuration
-   Eulerian reference: quantities are in terms of deformed configuration

----
## material derivatives

-   We refer to the undeformed configuration as *x*<sub>*i*</sub><sup>0</sup> and the deformed configuration as *x*<sub>*i*</sub>
-   If some quantity, *ϕ* is expressed in the undeformed configuration as *ϕ*(*x*<sub>1</sub><sup>0</sup>, *x*<sub>2</sub><sup>0</sup>, *x*<sub>3</sub><sup>0</sup>, *t*) then the material derivative is
- <!-- .element style="list-style-type:none" -->   $$\\frac{d\\phi}{dt} = \\frac{\\partial \\phi}{\\partial t}$$

----
## material derivatives

-   However in Eulerian form $\\bar{\\phi} (x\_1, x\_2, x\_3, t) = \\phi(x\_1^0,x\_2^0,x\_3^0,t)$ the material derivative becomes
- <!-- .element style="list-style-type:none" -->   $$\\frac{d\\bar{\\phi}}{dt} = \\frac{\\partial \\bar{\\phi}}{\\partial t} + \\frac{\\partial \\bar{ \\phi}}{\\partial x\_j}\\frac{d x\_j}{dt}$$

----
## deformation

-   A *deformation* is a comparison of two states. The deformation of a material point is expressed as
$$x\_i = x\_i(x\_1^0, x\_2^0, x\_3^0) \\quad \\text{or} \\quad x\_i^0 = x\_i^0(x\_1, x\_2, x\_3)$$
-   For example, consider the 2D deformation

$$\\begin{Bmatrix}
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
\\end{Bmatrix}$$

----
## deformation

![an illustration of deformation showing a simple square that has been stretched horizontally](..\images\deformation.png)

----
## displacement

<div class="left">
	<ul>
		<li>A displacement is the shortest distance traveled when a particle moves from one location to another </li>
		<li>Displacement is identical in Eulerian and Lagrangian descriptions </li>
		<li style="list-style-type:none">*u*<sub>*i*</sub> = (*x*<sub>*i*</sub> − *x*<sub>*i*</sub><sup>0</sup>) </li>
	</ul>
</div>
<div class="right">
	![an illustration of displacement showing the shortest distance between a point before and after a horizontal stretch](..\images\displacement.png)
</div>

---
# small deformation theory

----
## deformation gradients

![an arbitrary body before and after some arbitrary deformation](..\images\potato-displacement.png)

----
## deformation gradients

-   The position of the two points, *P*<sub>0</sub><sup>′</sup> and *P*<sup>′</sup>, is related by

$$\\begin{aligned}
  P\_0^\\prime &= x\_i (x\_i^0) &\\\\
  P^\\prime &= x\_i + dx\_i &=x\_i(x\_i^0 + dx\_i^0)
\\end{aligned}$$

-   We can approximate *x*<sub>*i*</sub>(*x*<sub>*i*</sub><sup>0</sup> + *dx*<sub>*i*</sub><sup>0</sup>) with a Taylor series expansion
- <!-- .element style="list-style-type:none" -->   $$\\approx x\_i (x\_i^0) + \\frac{\\partial x\_i^0}{\\partial x\_j} dxj^0 + \\frac{1}{2}\\frac{\\partial^2x\_i}{\\partial x\_j^0 \\partial x\_k^0} dx\_j^0 dx\_k^0 + ...$$

----
## deformation gradients

-   If the deformation is small, we can neglect higher-order terms of the expansion
- <!-- .element style="list-style-type:none" -->   $$P^\\prime = x\_i + dx\_i = x\_i (x\_i^0) + \\frac{\\partial x\_i^0}{\\partial x\_j} dxj^0$$
-   Which gives
- <!-- .element style="list-style-type:none" -->   $$dx\_i = \\frac{\\partial x\_i^0}{\\partial x\_j} dx\_j^0$$

----
## deformation gradients

-   In index notation we write displacements as *u*<sub>*i*</sub>
-   The deformation gradient can be written in this notation as

$$F = u\_{i,j} = \\begin{bmatrix}
  \\frac{\\partial u\_1}{\\partial x\_1} & \\frac{\\partial u\_1}{\\partial x\_2} & \\frac{\\partial u\_1}{\\partial x\_3}\\\\
  \\frac{\\partial u\_2}{\\partial x\_1} & \\frac{\\partial u\_2}{\\partial x\_2} & \\frac{\\partial u\_2}{\\partial x\_3}\\\\
  \\frac{\\partial u\_3}{\\partial x\_1} & \\frac{\\partial u\_3}{\\partial x\_2} & \\frac{\\partial u\_3}{\\partial x\_3}
\\end{bmatrix}$$

----
## translation

<div class="left">
	![a square is originally on the origin but is then translated some distance A from the y axis and B from the x axis](..\images\translation.png)
</div>
<div class="right">
	<ul>
		<li>x-displacement</li>
		<li style="list-style-type:none">*u*<sub>1</sub> = *x*<sub>1</sub><sup>0</sup> + *A* </li>
		<li>y-displacement</li>
		<li style="list-style-type:none">*u*<sub>2</sub> = *x*<sub>2</sub><sup>0</sup> + *B* </li>
	</ul>
</div>

----
## translation

-   Deformation gradient

$$F = u\_{i,j} = \\begin{bmatrix}
  \\frac{\\partial u\_1}{\\partial x\_1} & \\frac{\\partial u\_1}{\\partial x\_2}\\\\
\\frac{\\partial u\_2}{\\partial x\_1} & \\frac{\\partial u\_2}{\\partial x\_2}   \\end{bmatrix}$$
$$F = \\begin{bmatrix}
  1 & 0 \\\\ 0 & 1
\\end{bmatrix}$$

----
## rotation

<div class="left">
	![a square originally on the origin is rotated about the origin by some angle theta](..\images\rotation.png)
</div>
<div class="right">
	<ul>
		<li>x-displacement</li>
		<li style="list-style-type:none">*u*<sub>1</sub> = *x*<sub>1</sub><sup>0</sup>cos*θ* − *x*<sub>2</sub><sup>0</sup>sin*θ* </li>
		<li>y-displacement</li>
		<li style="list-style-type:none">*u*<sub>2</sub> = *x*<sub>1</sub><sup>0</sup>sin*θ* + *x*<sub>2</sub><sup>0</sup>cos*θ* </li>
	</ul>
</div>

----
## rotation

-   Deformation gradient

$$F = u\_{i,j} = \\begin{bmatrix}
	\\frac{\\partial u\_1}{\\partial x\_1} & \\frac{\\partial u\_1}{\\partial x\_2}\\\\
\\frac{\\partial u\_2}{\\partial x\_1} & \\frac{\\partial u\_2}{\\partial x\_2}   \\end{bmatrix}$$
$$F = \\begin{bmatrix}
	\\cos \\theta & -\\sin \\theta \\\\ \\sin \\theta & \\cos \\theta
\\end{bmatrix}$$

----
## simple shear

<div class="left">
	![a square is deformed by moving the top side to the right in a simple shearing motion](..\images\simple-shear.png)
</div>
<div class="right">
	<ul>
		<li>x-displacement</li>
		<li style="list-style-type:none">$$u\_1 = x\_1^0 + \\frac{1}{2} x\_2^0$$ </li>
		<li>y-displacement</li>
		<li style="list-style-type:none">*u*<sub>2</sub> = *x*<sub>2</sub><sup>0</sup> </li>
	</ul>
</div>

----
## simple shear

-   Deformation gradient

$$F = u\_{i,j} = \\begin{bmatrix}
	\\frac{\\partial u\_1}{\\partial x\_1} & \\frac{\\partial u\_1}{\\partial x\_2}\\\\
\\frac{\\partial u\_2}{\\partial x\_1} & \\frac{\\partial u\_2}{\\partial x\_2}   \\end{bmatrix}$$
$$F = \\begin{bmatrix}
	1 & \\frac{1}{2} \\\\ 0 & 1
\\end{bmatrix}$$

----
## pure shear

-   Sometimes it is important to eliminate rotations
-   We can design an experiment with a state of pure shear by inducing this deformation

$$F = \\begin{bmatrix}
	1 & \\frac{1}{2} \\\\ \\frac{1}{2} & 1
\\end{bmatrix}$$

-   We can integrate our usual relationship to find *u*<sub>1</sub> and *u*<sub>2</sub>

----
## pure shear

- <!-- .element style="list-style-type:none" -->$$\\frac{\\partial u\_1}{\\partial x\_1} = 1$$
- <!-- .element style="list-style-type:none" -->$$u_1 = x_1 + f(x_2)$$
- <!-- .element style="list-style-type:none" -->$$\\frac{\\partial u\_1}{\\partial x\_2} = \\frac{1}{2}$$
- <!-- .element style="list-style-type:none" -->$$\\frac{\\partial f}{\\partial x\_2} = \\frac{1}{2}$$
- <!-- .element style="list-style-type:none" -->$$u\_1 = x\_1 + \\frac{1}{2} x\_2$$

----
## pure shear

- <!-- .element style="list-style-type:none" -->$$\\frac{\\partial u\_2}{\\partial x\_2} = 1$$
- <!-- .element style="list-style-type:none" -->$$u_2 = x_2 + g(x_1)$$
- <!-- .element style="list-style-type:none" -->$$\\frac{\\partial u\_2}{\\partial x\_1} = \\frac{1}{2}$$
- <!-- .element style="list-style-type:none" -->$$\\frac{\\partial g}{\\partial x\_1} = \\frac{1}{2}$$
- <!-- .element style="list-style-type:none" -->$$u\_2 = x\_2 + \\frac{1}{2} x\_1$$

----
## pure shear

![a square before and after a pure shear deformation, with no rotation, as described by our previous equations](..\images\pure-shear.png) <!-- .element width="50%" -->

---
# strain

----
## strain definition

-   We can separate the deformation gradient into symmetric and antisymmetric parts
- <!-- .element style="list-style-type:none" -->   *u*<sub>*i*, *j*</sub> = *e*<sub>*ij*</sub> + *ω*<sub>*ij*</sub>
-   Where
$$\\begin{aligned}
	e\_{ij} &= \\frac{1}{2}(u\_{i,j} + u\_{j,i})\\\\
	\\omega\_{ij} &= \\frac{1}{2}(u\_{i,j} - u\_{j,i})
\\end{aligned}$$
-   *e*<sub>*ij*</sub> is known as the strain tensor
-   *ω*<sub>*ij*</sub> is known as the rotation tensor

----
## geometric description

-   Engineering strain
- <!-- .element style="list-style-type:none" -->   $$e^E = \\frac{\\Delta L}{L\_0}$$
-   True strain
- <!-- .element style="list-style-type:none" -->   $$e^T = \\frac{\\Delta L}{L\_0 + \\Delta L}$$
-   Logarithmic strain
- <!-- .element style="list-style-type:none" -->   $$e^L = \\int\_{L\_0}^L e^T = \\int\_{L\_0}^L \\frac{dl}{l} = \\ln \\left(\\frac{L}{L\_0}\\right)$$

----
## geometric description

-   Large strain: *ΔL* = *L*<sub>0</sub>

$$\\begin{aligned}
  e^E &= 1.00\\\\
  e^T &= 0.50\\\\
  e^L &= 0.69
\\end{aligned}$$

-   Small strain: *ΔL* = 0.05*L*<sub>0</sub>

$$\\begin{aligned}
  e^E &= 0.050\\\\
  e^T &= 0.048\\\\
  e^L &= 0.049
\\end{aligned}$$

----
## geometric description

![cube undergoes an arbitrary translation and deformation, which is used to describe strain](..\images\geometric-strain.png) <!-- .element width="50%" -->

----
## geometric description

-   The extensional strain in the x-direction (engineering strain) is defined by
- <!-- .element style="list-style-type:none" -->   $$\\varepsilon\_x = \\frac{A^\\prime B^\\prime - AB}{AB}$$
-   From geometry, we can write *A*<sup>′</sup>*B*<sup>′</sup> as

$$\\begin{aligned}
	A^\\prime B^\\prime &= \\sqrt{\\left(dx + \\frac{\\partial u}{\\partial x}dx\\right)^2 + \\left(\\frac{\\partial v}{\\partial x}dx\\right)^2} \\\\
	&= dx \\sqrt{1 + 2\\frac{\\partial u}{\\partial x} + \\left(\\frac{\\partial u}{\\partial x}\\right)^2+ \\left(\\frac{\\partial v}{\\partial x}\\right)^2}
\\end{aligned}$$

----
## geometric description

-   For small deformation, we assume $\\frac{\\partial v}{\\partial x}$ is small when compared with $\\frac{\\partial u}{\\partial x}$, which gives
- <!-- .element style="list-style-type:none" -->   $$A^\\prime B^\\prime = \\left(1 + \\frac{\\partial u}{\\partial x}\\right)dx$$

----
## geometric description

$$\\begin{aligned}
	\\varepsilon\_x &= \\frac{A^\\prime B^\\prime - AB}{AB} = \\frac{\\left(1 + \\frac{\\partial u}{\\partial x}\\right)dx - dx}{dx} \\\\
	&= \\frac{\\partial u}{\\partial x}
\\end{aligned}$$

-   The normal strain in the y-direction is found the same way
- <!-- .element style="list-style-type:none" -->   $$\\varepsilon\_y = \\frac{\\partial v}{\\partial y}$$

----
## geometric description

-   Engineering shear strain is defined as the change in angle between two originally orthogonal directions
- <!-- .element style="list-style-type:none" -->   $$\\gamma\_{xy} = \\frac{\\pi}{2} - \\angle D^\\prime A^\\prime B^\\prime = \\alpha + \\beta$$
-   For small strains, *α* ≈ tan*α* and *β* ≈ tan*β*.

$$\\begin{aligned}
	\\gamma\_{xy} &= \\frac{\\frac{\\partial v}{\\partial x}dx}{dx + \\frac{\\partial u}{\\partial x dx}} + \\frac{\\frac{\\partial u}{\\partial y}dy}{dy + \\frac{\\partial v}{\\partial y dx}}\\\\
	&\\approx \\frac{\\partial u}{\\partial y} + \\frac{\\partial v}{\\partial x}
\\end{aligned}$$

----
## geometric description

-   The other shear terms can be found in the same way

$$\\begin{aligned}
	\\gamma\_{xy} &= \\frac{\\partial u}{\\partial y} + \\frac{\\partial v}{\\partial x}\\\\
	\\gamma\_{xz} &= \\frac{\\partial u}{\\partial z} + \\frac{\\partial w}{\\partial x}\\\\
	\\gamma\_{yz} &= \\frac{\\partial v}{\\partial z} + \\frac{\\partial w}{\\partial y}
\\end{aligned}$$

----
## geometric description

-   Engineering strain and tensor strain definitions differ only in shear terms
- <!-- .element style="list-style-type:none" -->   $$e\_{ij} = \\frac{1}{2} \\left(u\_{i,j} + u\_{j,i}\\right)$$
- <!-- .element style="list-style-type:none" -->   $$e\_{xy} = \\frac{1}{2} \\gamma\_{xy}$$

----
## example

-   Calculate the deformation gradient, strain tensor, and rotation tensor for the given deformation

$$\\begin{Bmatrix}
	u\_1 \\\\ u\_2 \\\\ u\_3
	\\end{Bmatrix} = \\begin{Bmatrix}
	xy^2z \\\\ xz \\\\ z^3
\\end{Bmatrix}$$

<div class="fragment">
	<ul>
		<li>Deformation gradient:</li>
	</ul>
$$F = u\_{i,j} = \\begin{bmatrix}
	y^2 z & 2 xyz & xy^2\\\\
	z & 0 & x\\\\
	0 & 0 & 3z^2
\\end{bmatrix}$$
</div>

----
## example

-   Strain tensor
- <!-- .element style="list-style-type:none" -->   $$e\_{ij} = \\frac{1}{2}(u\_{i,j} + u\_{j,i})$$

$$e\_{ij} = \\begin{bmatrix}
	y^2 z & xyz + \\frac{1}{2}z & \\frac{1}{2}xy^2\\\\
	xyz + \\frac{1}{2}z & 0 & \\frac{1}{2}x\\\\
	\\frac{1}{2}xy^2 & \\frac{1}{2}x & 3z^2
\\end{bmatrix}$$

----
## example

-   Rotation tensor
- <!-- .element style="list-style-type:none" -->   $$\\omega\_{ij} = \\frac{1}{2}(u\_{i,j} - u\_{j,i})$$

$$\\omega\_{ij} = \\begin{bmatrix}
	0 & xyz - \\frac{1}{2}z & \\frac{1}{2}xy^2\\\\
	-xyz + \\frac{1}{2}z & 0 & \\frac{1}{2}x\\\\
	-\\frac{1}{2}xy^2 & -\\frac{1}{2}x & 0
\\end{bmatrix}$$

----
## example

-   As we did with the deformation gradient, we can integrate the strain tensor to find the deformation (symmetric portion)

$$e\_{ij} = \\begin{bmatrix}
	yz & xz & xy\\\\
	xz & 2y & \\frac{1}{2}x^2\\\\
	xy & \\frac{1}{2}x^2 & 3z^2
\\end{bmatrix}$$

-   We start by integrating the diagonal terms
- <!-- .element style="list-style-type:none" -->   *u* = ∫*yzdx* = *xyz* + *f*(*y*, *z*)
- <!-- .element style="list-style-type:none" -->   *v* = ∫2*ydy* = *y*<sup>2</sup> + *g*(*x*, *z*)
- <!-- .element style="list-style-type:none" -->   *w* = ∫3*z*<sup>2</sup>*dz* = *z*<sup>3</sup> + *h*(*x*, *y*)

----
## example

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

----
## example

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

----
## example

$$\\begin{aligned}
	\\frac{1}{2}x^2 &= \\frac{1}{2} \\left(g\_{,z} + h\_{,y}\\right)\\\\
	\\frac{1}{2}x^2 &= \\frac{1}{2} \\left(\\frac{1}{2}x^2 + \\frac{1}{2}x^2\\right)
\\end{aligned}$$
$$\\begin{aligned}
	u &= xyz\\\\
	v &= y^2 + \\frac{1}{2}x^2z\\\\
	w &= z^3 + \\frac{1}{2}x^2y
\\end{aligned}$$

