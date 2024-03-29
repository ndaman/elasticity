# AE731
## Theory of Elasticity
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering
September 2, 2021

----
## upcoming schedule

-   Sep 2 - Strain Transformation
-   Sep 3 - Homework 2 Due, Homework 1 Self-Grade Due
-   Sep 7 - Exam 1 Review
-   Sep 9 - Exam 1

----
## outline

<!-- vim-markdown-toc GFM -->

* example
* group problems
* principal strains
* special strain definitions
* strain transformation

<!-- vim-markdown-toc -->

---
# example

----
## example

-   Calculate the deformation gradient, strain tensor, and rotation tensor for the given deformation

`$$\begin{Bmatrix}
	u_1 \\ u_2 \\ u_3
	\end{Bmatrix} = \begin{Bmatrix}
	xy^2z \\ xz \\ z^3
\end{Bmatrix}$$`

----
## example

-   Deformation gradient:
	
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
-   `$u = \int yz dx = xyz + f(y, z)$`
-   `$v= \int 2ydy = y^2 + g(y, z)$`
-   `$w = \int 3z^2 dz = z^3 + h(x, y)$`

----
## example

-   Next we need to find the shear terms

`$$\begin{aligned}
	e_{xy} &= \frac{1}{2}(u_{,y}+v_{,x})\\
	xz &= \frac{1}{2}(xz + f_{,y} + g_{,x})
\end{aligned}$$`

`$$\begin{aligned}
	e_{xz} &= \frac{1}{2}(u_{,z}+w_{,x})\\
	xy &= \frac{1}{2}(xy + f_{,z} + h_{,x})
\end{aligned}$$`

`$$\begin{aligned}
	e_{yz} &= \frac{1}{2}(v_{,z}+w_{,y})\\
	\frac{1}{2}x^2 &= \frac{1}{2}(g_{,z} + h_{,y})
\end{aligned}$$`

----
## example

-   Note that we cannot uniquely solve this (any arbitrary rotation `$\omega$` can be added and will still produce a valid strain)
-   Let `$f(y, z) = 0$`

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

---
# group problems

----
## group 1

-   Sketch the deformed and undeformed shape of a rectangle under the following deformation

`$$\begin{aligned}
	u &= 0.7x + 0.1y\\
	v &= 0.3x + 1.2y
\end{aligned}$$`

----
## group 2

-   For the following deformation, find the deformation gradient, strain, and rotation

`$$\begin{aligned}
	u &= xyz\\
	v &= xy + z\\
	z &= y^2z
\end{aligned}$$`

----
## group 3

-   From the following strain field, find the displacements (you may assume no rotations)

`$$\epsilon_{ij} = \begin{bmatrix}
    y & x + y \\
    x + y & x
\end{bmatrix}$$`

---
# principal strains

----
## principal strains

-   Principal strains are found in exactly the same way as principal values discussed in Chapter 1

`$$\det[e_{ij} - e\delta_{ij}]=0$$`

-   Invariants can also be found in the same fashion as in any other tensor

`$$\begin{aligned}
	\vartheta_1 &= e_1 + e_2 + e_3\\
	\vartheta_2 &= e_1 e_2 + e_2 e_3 + e_3 e_1\\
	\vartheta_3 &= e_1 e_2 e_3
\end{aligned}$$`

----
## principal strains

-   Principal strains and invariants have some important physical meanings
-   `$\vartheta_1$` is called the *cubical dilation*, and is related to the change in volume of the material
-   Note that in the principal direction, there are no shear strains

`$$\begin{bmatrix}
	e_1 & 0 & 0\\
	0 & e_2 & 0 \\
	0 & 0 & e_3
\end{bmatrix}$$`

-   This means that there is only extensional strain in the principal direction (i.e. a cube will remain a rectangular prism, the corners will maintain `$90^\circ$` angles)

----
## volume change

-   Consider a rectangular prism with edges oriented in the principal directions

![A rectangular prism before and after some volumetric stretch](../images/dilatation.png) <!-- .element width="50%" -->

----
## volume change

-   The volume before deformation is `$L = LWH$`
-   The volume after deformation is given by `$V^\prime = L^\prime W^\prime H^\prime$`
-   We can relate the side lengths after deformation to strains

`$$e_1 = \frac{L^\prime - L}{L}$$`

`$$Le_1 + L = L^\prime$$`

-   We can now write the volume as `$V^\prime = L(1+e_1)W(1+e_2)H(1+e_3)$`

----
## volume change

-   After multiplication, the deformed volume is given as
-   `$V^\prime = LWH(1+e_1 + e_2 + e_3 + e_1e_2 + e_2e_3 + e_1e_3 + e_1e_2e_3)$`
-   For small strains, `$e_i << 1$`, therefore `$e_1$`, `$e_2$`, and `$e_3$` will be much larger than `$e_1e_2 + e_2e_3 + e_1e_3 + e_1e_2e_3)$`
-   `$V^\prime = LWH(1+ e_1 + e_2 + e_3)$`

----
## volume change

-   A “dilatation” is defined as the change in volume divided by the original volume

`$$\frac{\Delta V}{V} = \frac{V^\prime - V}{V}$$`

-   Substituting the relationships found earlier

`$$\frac{V^\prime - V}{V} = \frac{LWH(1+e_1+e_2+e_3) - LWH}{LWH}$$`

-   Which simplifies to

`$$e_1 + e_2 + e_3 = \vartheta_1 $$`

---
# special strain definitions

----
## spherical strain

-   This dilatation can be used to find the so-called *spherical strain*

`$$\begin{aligned}
	\tilde{e}_{ij} = \frac{1}{3} e_{kk} \delta_{ij} = \frac{1}{3} \vartheta_1 \delta_{ij}
\end{aligned}$$`

-   The *deviatoric strain* is found by subtracting the spherical strain from the strain tensor

`$$\hat{e}_{ij} = e_{ij} - \frac{1}{3} e_{kk} \delta_{ij}$$`

---
# strain transformation

----
## strain transformation

-   The usual tensor transformation applies to the strain tensor as well
-   `$e_{ij}^\prime = Q_{im}Q_{jn}e_{mn}$`
-   In many instances, however, we are only concerned with the strain within a plane (for example, when using strain gages).

----
## strain transformation

-   For an in-plane rotation (rotation about *z*-axis), we find

`$$Q_{ij} = \begin{bmatrix}
	\cos \theta & \cos (90-\theta) & \cos 90\\
	\cos (90+\theta) & \cos \theta & \cos 90\\
	\cos 90 & \cos 90 & \cos 0\\
	\end{bmatrix} = \begin{bmatrix}
	\cos \theta & \sin \theta & 0\\
	-\sin \theta & \cos \theta & 0\\
	0 & 0 & 1\\
\end{bmatrix}$$`

----
## strain transformation

-   If we multiply this out, for the in-plane strain terms (`$e_x^\prime$`, `$e_y^\prime$`, and `$e_{xy}^\prime$`) we find

`$$\begin{aligned}
	e^\prime_x &= e_x \cos ^2 \theta + e_y \sin^2 \theta + 2 e_{xy} \sin \theta \cos \theta \\
	e^\prime_y &= e_x \sin ^2 \theta + e_y \cos^2 \theta - 2 e_{xy} \sin \theta \cos \theta \\
	e^\prime_{xy} &= -e_x \sin \theta \cos \theta + e_y \sin \theta \cos \theta + e_{xy} (\cos^2 \theta - \sin^2 \theta)
\end{aligned}$$`

----
## strain transformation

-   This is often re-written using the double-angle formulas

`$$\begin{aligned}
	e^\prime_x &= \frac{e_x + e_y}{2} + \frac{e_x - e_y}{2}\cos 2\theta + e_{xy} \sin 2\theta \\
	e^\prime_y &= \frac{e_x + e_y}{2} - \frac{e_x - e_y}{2}\cos 2\theta - e_{xy} \sin 2\theta \\
	e^\prime_{xy} &= \frac{e_y - e_x}{2}\sin 2\theta + e_{xy} \cos 2\theta
\end{aligned}$$`

----
## strain transformation

-   Many times it is easy to measure the axial strain directly with strain gages, but the shear strain cannot be easily measured
-   We can use an extra, off-axis strain gage, together with the strain transformation equations, to calculate the shear strain
-   Many companies already do this with “rosettes” which have strain gages at specified angles built-in

----
## example

![strain gage rosettes example problem](../images/rosette-example.png) <!-- .element width="70%" -->

----
## example

-   Given that `$\epsilon_a = 0.005$`, `$\epsilon_b = -0.002$`, and `$\epsilon_c=0.003$`, find `$e_x$`, `$e_y$` and `$e_{xy}$`.
-   Note that `$e_y = \epsilon_b = -0.002$`
-   Set coordinate system so that `$\epsilon_b = e_x^\prime$`
-   Use equation for `$e_x^\prime$` with `$\theta = 30$`.

`$$e^\prime_x = \frac{e_x + e_y}{2} + \frac{e_x - e_y}{2}\cos 60 + e_{xy} \sin 60$$`

----
## example

-   We have two unknowns in this equation, so we need another
-   We can use the equation for `$e_y^\prime$` with `$\theta=60$` so that `$\epsilon_b = e_x^\prime$`

`$$e^\prime_y = \frac{e_x + e_y}{2} - \frac{e_x - e_y}{2}\cos 120 - e_{xy} \sin 120$$`

----
## example

-   Substituting known values and simplifying:

`$$\begin{aligned}
	0.01 + 0.002 - 0.002 \cos 60 &= e_x (1+\cos 60) + e_{xy} \sin 60 \\
	0.006 + 0.002 + 0.002 \cos 120 &= e_x (1-\cos 120) - e_{xy} \sin 120
\end{aligned}$$`

-   And solving we find `$e_x = 0.006$`, `$e_y = -0.002$`, and `$e_{xy}=0.00231$`


