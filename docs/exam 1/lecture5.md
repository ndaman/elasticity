# AE731
## Theory of Elasticity
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering
31 August, 2021

----
## upcoming schedule

-   Aug 31 - Displacement and Strain
-   Sep 2 - Strain Transformation
-   Sep 3 - Homework 2 Due, Homework 1 Self-Grade Due
-   Sep 7 - Exam 1 Review
-   Sep 9 - Exam 1

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

-   We refer to the undeformed configuration as `$x_i^0$` and the deformed configuration as `$x_i$` 
-   If some quantity, `$\phi$` is expressed in the undeformed configuration as `$\phi (x_1^0, x_2^0, x_3^0, t)$` then the material derivative is

`$$\frac{d\phi}{dt} = \frac{\partial \phi}{\partial t}$$`

----
## material derivatives

-   However in Eulerian form `$\bar{\phi} (x_1, x_2, x_3, t) = \phi(x_1^0,x_2^0,x_3^0,t)$` the material derivative becomes
 
`$$\frac{d\bar{\phi}}{dt} = \frac{\partial \bar{\phi}}{\partial t} + \frac{\partial \bar{ \phi}}{\partial x_j}\frac{d x_j}{dt}$$`

----
## deformation

-   A *deformation* is a comparison of two states. The deformation of a material point is expressed as

`$$x_i = x_i(x_1^0, x_2^0, x_3^0) \quad \text{or} \quad x_i^0 = x_i^0(x_1, x_2, x_3)$$`

-   For example, consider the 2D deformation

`$$\begin{Bmatrix}
		x_1 \\
    x_2
	\end{Bmatrix} =
	\begin{Bmatrix}
		2 x_1^0 \\
    x_2^0
	\end{Bmatrix} \quad \text{or} \quad
	\begin{Bmatrix}
		x_1^0 \\
    x_2^0
	\end{Bmatrix}
		= \begin{Bmatrix}
		\frac{1}{2} x_1 \\
    x_2
\end{Bmatrix}$$`

----
## deformation

![an illustration of deformation showing a simple square that has been stretched horizontally](../images/deformation.png)

----
## displacement

<div class="left">

A displacement is the shortest distance traveled when a particle moves from one location to another</li>
Displacement is identical in Eulerian and Lagrangian descriptions 

`$$u_i = (x_i - x_i^0)$$`

</div>

<div class="right">

![an illustration of displacement showing the shortest distance between a point before and after a horizontal stretch](../images/displacement.png)
  
</div>

---
# small deformation theory

----
## deformation gradients

![an arbitrary body before and after some arbitrary deformation](../images/potato-displacement.png)

----
## deformation gradients

-   The position of the two points, `$P_0^\prime$` and `$P^\prime$`, is related by

`$$\begin{aligned}
  P_0^\prime &= x_i (x_i^0) &\\
  P^\prime &= x_i + dx_i &=x_i(x_i^0 + dx_i^0)
\end{aligned}$$`

-   We can approximate `$x_i(x_i^0, dx_i^0)$` with a Taylor series expansion

`$$\approx x_i (x_i^0) + \frac{\partial x_i^0}{\partial x_j} dxj^0 + \frac{1}{2}\frac{\partial^2x_i}{\partial x_j^0 \partial x_k^0} dx_j^0 dx_k^0 + ...$$`

----
## deformation gradients

-   If the deformation is small, we can neglect higher-order terms of the expansion

`$$P^\prime = x_i + dx_i = x_i (x_i^0) + \frac{\partial x_i^0}{\partial x_j} dxj^0$$`

-   Which gives

`$$dx_i = \frac{\partial x_i^0}{\partial x_j} dx_j^0$$`

----
## deformation gradients

-   In index notation we write displacements as `$u_i$`
-   The deformation gradient can be written in this notation as

`$$F = u_{i,j} = \begin{bmatrix}
  \frac{\partial u_1}{\partial x_1} & \frac{\partial u_1}{\partial x_2} & \frac{\partial u_1}{\partial x_3}\\
  \frac{\partial u_2}{\partial x_1} & \frac{\partial u_2}{\partial x_2} & \frac{\partial u_2}{\partial x_3}\\
  \frac{\partial u_3}{\partial x_1} & \frac{\partial u_3}{\partial x_2} & \frac{\partial u_3}{\partial x_3}
\end{bmatrix}$$`

----
## translation

<div class="left">

![a square is originally on the origin but is then translated some distance A from the y axis and B from the x axis](../images/translation.png)

</div>

<div class="right">

- x-displacement

`$$u_1 = x_1^0 + A$$`

- y-displacement

`$$u_2 = x_2^0 + B$$`

</div>

----
## translation

-   Deformation gradient

`$$F = u_{i,j} = \begin{bmatrix}
  \frac{\partial u_1}{\partial x_1} & \frac{\partial u_1}{\partial x_2}\\
\frac{\partial u_2}{\partial x_1} & \frac{\partial u_2}{\partial x_2}   \end{bmatrix}$$`
`$$F = \begin{bmatrix}
  1 & 0 \\
  0 & 1
\end{bmatrix}$$`

----
## rotation

<div class="left">

![a square originally on the origin is rotated about the origin by some angle theta](../images/rotation.png)
</div>

<div class="right">

- x-displacement

`$$ u_1 = x_1^0 \cos \theta - x_2^0 \sin \theta$$`

- y-displacement

`$$ u_2 = x_1^0 \sin \theta + x_2^0 \cos \theta$$`

</div>

----
## rotation

-   Deformation gradient

`$$F = u_{i,j} = \begin{bmatrix}
	\frac{\partial u_1}{\partial x_1} & \frac{\partial u_1}{\partial x_2}\\
\frac{\partial u_2}{\partial x_1} & \frac{\partial u_2}{\partial x_2}   \end{bmatrix}$$`
`$$F = \begin{bmatrix}
	\cos \theta & -\sin \theta \\
  \sin \theta & \cos \theta
\end{bmatrix}$$`

----
## simple shear

<div class="left">

![a square is deformed by moving the top side to the right in a simple shearing motion](../images/simple-shear.png)

</div>

<div class="right">

- x-displacement

`$$u_1 = x_1^0 + \frac{1}{2} x_2^0$$`

- y-displacement

`$$u_2 = x_2^0$$`

</div>

----
## simple shear

-   Deformation gradient

`$$F = u_{i,j} = \begin{bmatrix}
	\frac{\partial u_1}{\partial x_1} & \frac{\partial u_1}{\partial x_2}\\
\frac{\partial u_2}{\partial x_1} & \frac{\partial u_2}{\partial x_2}   \end{bmatrix}$$`
`$$F = \begin{bmatrix}
	1 & \frac{1}{2} \\
  0 & 1
\end{bmatrix}$$`

----
## pure shear

-   Sometimes it is important to eliminate rotations
-   We can design an experiment with a state of pure shear by inducing this deformation

`$$F = \begin{bmatrix}
	1 & \frac{1}{2} \\
  \frac{1}{2} & 1
\end{bmatrix}$$`

-   We can integrate our usual relationship to find `$u_1$` and `$u_2$`

----
## pure shear

`$$\frac{\partial u_1}{\partial x_1} = 1$$`
`$$u_1 = x_1 + f(x_2)$$`
`$$\frac{\partial u_1}{\partial x_2} = \frac{1}{2}$$`
`$$\frac{\partial f}{\partial x_2} = \frac{1}{2}$$`
`$$u_1 = x_1 + \frac{1}{2} x_2$$`

----
## pure shear

`$$\frac{\partial u_2}{\partial x_2} = 1$$`
`$$u_2 = x_2 + g(x_1)$$`
`$$\frac{\partial u_2}{\partial x_1} = \frac{1}{2}$$`
`$$\frac{\partial g}{\partial x_1} = \frac{1}{2}$$`
`$$u_2 = x_2 + \frac{1}{2} x_1$$`

----
## pure shear

![a square before and after a pure shear deformation, with no rotation, as described by our previous equations](../images/pure-shear.png) <!-- .element width="50%" -->

---
# strain

----
## strain definition

-   We can separate the deformation gradient into symmetric and antisymmetric parts

`$$ u_{i,j} = e_{ij} + \omega_{ij}$$`

-   Where

`$$\begin{aligned}
	e_{ij} &= \frac{1}{2}(u_{i,j} + u_{j,i})\\
	\omega_{ij} &= \frac{1}{2}(u_{i,j} - u_{j,i})
\end{aligned}$$`
-   `$e_{ij}$` is known as the strain tensor
-   `$\omega_{ij}$` is known as the rotation tensor

----
## geometric description

-   Engineering strain

`$$e^E = \frac{\Delta L}{L_0}$$`

-   True strain

`$$e^T = \frac{\Delta L}{L_0 + \Delta L}$$`

-   Logarithmic strain

`$$e^L = \int_{L_0}^L e^T = \int_{L_0}^L \frac{dl}{l} = \ln \left(\frac{L}{L_0}\right)$$`

----
## geometric description

-   Large strain: `$\Delta L = L_0$`

`$$\begin{aligned}
  e^E &= 1.00\\
  e^T &= 0.50\\
  e^L &= 0.69
\end{aligned}$$`

-   Small strain: `$\Delta L = 0.05 L_0$`

`$$\begin{aligned}
  e^E &= 0.050\\
  e^T &= 0.048\\
  e^L &= 0.049
\end{aligned}$$`

----
## geometric description

![cube undergoes an arbitrary translation and deformation, which is used to describe strain](../images/geometric-strain.png) <!-- .element width="50%" -->

----
## geometric description

-   The extensional strain in the x-direction (engineering strain) is defined by

`$$\varepsilon_x = \frac{A^\prime B^\prime - AB}{AB}$$`

-   From geometry, we can write `$A^\prime B^\prime$` as

`$$\begin{aligned}
	A^\prime B^\prime &= \sqrt{\left(dx + \frac{\partial u}{\partial x}dx\right)^2 + \left(\frac{\partial v}{\partial x}dx\right)^2} \\
	&= dx \sqrt{1 + 2\frac{\partial u}{\partial x} + \left(\frac{\partial u}{\partial x}\right)^2+ \left(\frac{\partial v}{\partial x}\right)^2}
\end{aligned}$$`

----
## geometric description

-   For small deformation, we assume `$\frac{\partial v}{\partial x}$` is small when compared with `$\frac{\partial u}{\partial x}$`, which gives

`$$A^\prime B^\prime = \left(1 + \frac{\partial u}{\partial x}\right)dx$$`

----
## geometric description

`$$\begin{aligned}
	\varepsilon_x &= \frac{A^\prime B^\prime - AB}{AB} = \frac{\left(1 + \frac{\partial u}{\partial x}\right)dx - dx}{dx} \\
	&= \frac{\partial u}{\partial x}
\end{aligned}$$`

-   The normal strain in the y-direction is found the same way

`$$\varepsilon_y = \frac{\partial v}{\partial y}$$`

----
## geometric description

-   Engineering shear strain is defined as the change in angle between two originally orthogonal directions

`$$\gamma_{xy} = \frac{\pi}{2} - \angle D^\prime A^\prime B^\prime = \alpha + \beta$$`

-   For small strains, `$\alpha \approx \tan \alpha$` and  `$\beta \approx \tan \beta$`.

`$$\begin{aligned}
	\gamma_{xy} &= \frac{\frac{\partial v}{\partial x}dx}{dx + \frac{\partial u}{\partial x}dx} + \frac{\frac{\partial u}{\partial y}dy}{dy + \frac{\partial v}{\partial y }dy}\\
	&\approx \frac{\partial u}{\partial y} + \frac{\partial v}{\partial x}
\end{aligned}$$`

----
## geometric description

-   The other shear terms can be found in the same way

`$$\begin{aligned}
	\gamma_{xy} &= \frac{\partial u}{\partial y} + \frac{\partial v}{\partial x}\\
	\gamma_{xz} &= \frac{\partial u}{\partial z} + \frac{\partial w}{\partial x}\\
	\gamma_{yz} &= \frac{\partial v}{\partial z} + \frac{\partial w}{\partial y}
\end{aligned}$$`

----
## geometric description

-   Engineering strain and tensor strain definitions differ only in shear terms

`$$e_{ij} = \frac{1}{2} \left(u_{i,j} + u_{j,i}\right)$$`
`$$e_{xy} = \frac{1}{2} \gamma_{xy}$$`

----
## example

-   Calculate the deformation gradient, strain tensor, and rotation tensor for the given deformation

`$$\begin{Bmatrix}
	u_1 \\
  u_2 \\
  u_3
	\end{Bmatrix} = \begin{Bmatrix}
	xy^2z \\
  xz \\
  z^3
\end{Bmatrix}$$`

- Deformation gradient:

`$$F = u_{i,j} = \begin{bmatrix}
	y^2 z & 2 xyz & xy^2\\
	z & 0 & x\\
	0 & 0 & 3z^2
\end{bmatrix}$$`

----
## example

-   Strain tensor

`$$e_{ij} = \frac{1}{2}(u_{i,j} + u_{j,i})$$`

`$$e_{ij} = \begin{bmatrix}
	y^2 z & xyz + \frac{1}{2}z & \frac{1}{2}xy^2\\
	xyz + \frac{1}{2}z & 0 & \frac{1}{2}x\\
	\frac{1}{2}xy^2 & \frac{1}{2}x & 3z^2
\end{bmatrix}$$`

----
## example

-   Rotation tensor

`$$\omega_{ij} = \frac{1}{2}(u_{i,j} - u_{j,i})$$`

`$$\omega_{ij} = \begin{bmatrix}
	0 & xyz - \frac{1}{2}z & \frac{1}{2}xy^2\\
	-xyz + \frac{1}{2}z & 0 & \frac{1}{2}x\\
	-\frac{1}{2}xy^2 & -\frac{1}{2}x & 0
\end{bmatrix}$$`

----
## example

-   As we did with the deformation gradient, we can integrate the strain tensor to find the deformation (symmetric portion)

`$$e_{ij} = \begin{bmatrix}
	yz & xz & xy\\
	xz & 2y & \frac{1}{2}x^2\\
	xy & \frac{1}{2}x^2 & 3z^2
\end{bmatrix}$$`

----
## example

-   We start by integrating the diagonal terms

`$$u = \int yz dx = xyz + f(y,z)$$`
`$$v = \int 2y dy = y^2 + g(x, z)$$`
`$$w = \int 3z^2 dz = z^3 + h(x,y)$$`

----
## example

-   Next we need to find the shear terms

<div class="left">

`$$\begin{aligned}
	e_{xy} &= \frac{1}{2}(u_{,y}+v_{,x})\\
	xz &= \frac{1}{2}(xz + f_{,y} + g_{,x})
\end{aligned}$$`
`$$\begin{aligned}
	e_{xz} &= \frac{1}{2}(u_{,z}+w_{,x})\\
	xy &= \frac{1}{2}(xy + f_{,z} + h_{,x})
\end{aligned}$$`

</div>

<div class="right">

`$$\begin{aligned}
	e_{yz} &= \frac{1}{2}(v_{,z}+w_{,y})\\
	\frac{1}{2}x^2 &= \frac{1}{2}(g_{,z} + h_{,y})
\end{aligned}$$`
</div>

----
## example

-   Note that we cannot uniquely solve this (any arbitrary rotation `$\omega$` can be added and will still produce a valid strain)
-   Let `$f(y,z)=0$`

`$$\begin{aligned}
	g_{,x} &= xz\\
	g(x,z) &= \frac{1}{2}x^2 z
\end{aligned}$$`
`$$\begin{aligned}
	h_{,x} &= xy \\
	h(x,z) &= \frac{1}{2}x^2 y
\end{aligned}$$`

----
## example

`$$\begin{aligned}
	\frac{1}{2}x^2 &= \frac{1}{2} \left(g_{,z} + h_{,y}\right)\\
	\frac{1}{2}x^2 &= \frac{1}{2} \left(\frac{1}{2}x^2 + \frac{1}{2}x^2\right)
\end{aligned}$$`
`$$\begin{aligned}
	u &= xyz\\
	v &= y^2 + \frac{1}{2}x^2z\\
	w &= z^3 + \frac{1}{2}x^2y
\end{aligned}$$`

