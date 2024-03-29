# AE731
## Theory of Elasticity
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering
September 16, 2021

----
## upcoming schedule

-   Sep 16 - Stress Transformation
-   Sep 17 - Homework 2 Self-grade Due
-   Sep 21 - Equilibrium Equations
-   Sep 23 - Material Characterization
-   Sep 24 - Homework 3 Due
-   Sep 28 - Thermoelasticity

----
## outline

<!-- vim-markdown-toc GFM -->

* traction vector and stress tensor
* stress transformation
* principal stresses
* maximum shear stress
* group problems

<!-- vim-markdown-toc -->

---
# traction vector and stress tensor

----
## traction

![traction vector illustration](../images/traction.PNG)

----
## traction

-   The traction vector is defined as

`$$\hat{t}^n(x,\hat{n}) = \lim\limits_{\Delta A \to 0} \frac{\Delta \hat{f}}{\Delta A}$$`

-   By Newton’s third law (action-reaction principle)

`$$\hat{t}^n(x,\hat{n}) = -\hat{t}^n(x,-\hat{n})$$`

----
## traction

![traction illustrated on a cube](../images/traction-cube.png)

----
## traction

-   If we consider the special case where the normal vectors, `$\hat{n}$`, align with the coordinate system (`$\hat{e}_1$`,`$\hat{e}_2$`,`$\hat{e}_3$`)

-   On the 1-face:

`$$\begin{aligned}
	\hat{n}&=\hat{e}_1: &\quad \hat{t}^n = t_i^{(\hat{e}_1)} \hat{e}_i = t_1^{(\hat{e}_1)} \hat{e}_1 + t_2^{(\hat{e}_1)} \hat{e}_2 + t_3^{(\hat{e}_1)} \hat{e}_3
\end{aligned}$$`

-   On the 2-face:

`$$\begin{aligned}
	\hat{n}&=\hat{e}_2: &\quad \hat{t}^n = t_i^{(\hat{e}_2)} \hat{e}_i = t_1^{(\hat{e}_2)} \hat{e}_1 + t_2^{(\hat{e}_2)} \hat{e}_2 + t_3^{(\hat{e}_2)} \hat{e}_3
\end{aligned}$$`

----
## traction

-   And on the 3-face:

`$$\begin{aligned}
	\hat{n}&=\hat{e}_3: &\quad \hat{t}^n = t_i^{(\hat{e}_3)} \hat{e}_i = t_1^{(\hat{e}_3)} \hat{e}_1 + t_2^{(\hat{e}_3)} \hat{e}_2 + t_3^{(\hat{e}_3)} \hat{e}_3
\end{aligned}$$`

----
## stress tensor

-   To simplify the notation, we introduce the stress tensor

`$$\sigma_{ij} = t_j^{(\hat{e}_i)}$$`

![stress tensor illustrated on a cube](../images/stress-cube.png)

----
## traction

-   We can find some interesting information about the traction vector by considering an arbitrary tetrahedron with some traction `$\hat{t}^{(n)}$` applied to the surface

----
## traction

-   If we consider the balance of forces in the `$x_1$`-direction

`$$t_1 dA - \sigma_{11}dA_1 - \sigma_{21}dA_2 - \sigma_{31}dA_3 + b_1 \rho dV = 0$$`

-   The area components are:

`$$\begin{aligned}
	dA_1 &= n_1 dA\\
	dA_2 &= n_2 dA\\
	dA_3 &= n_3 dA\\
\end{aligned}$$`

-   And `$dV = \frac{1}{3}h dA$`.

----
## traction

`$$t_1 dA - \sigma_{11} n_1 dA - \sigma_{21} n_2 dA - \sigma_{31} n_3 dA + b_1 \rho \frac{1}{3}h dA = 0$$`

-   If we let `$h \to 0$` and divide by `$dA$`

`$$t_1 = \sigma_{11}n_1 + \sigma_{21}n_2 + \sigma_{31}n_3$$`

-   We can write this in index notation as

`$$t_1 = \sigma_{i1}n_i$$`

----
## traction

-   We find, similarly

`$$\begin{aligned}
	t_2 &= \sigma_{i2} n_i\\
	t_3 &= \sigma_{i3} n_i\\
\end{aligned}$$`

----
## traction

-   We can further combine these results in index notation as

`$$t_j = \sigma_{ij}n_i$$`

-   This means with knowledge of the nine components of `$\sigma_{ij}$`, we can find the traction vector at any point on any surface

----
## example

-   Consider a block of material with a uniformly distributed force acting on the 1-face. Find the tractions on an arbitrary interior plane

![traction cut on some arbitrary plane](../images/traction-cut.png)

----
## example

-   First we consider a vertical cut on the interior 1-face (`$n_i = \langle 1, 0, 0 \rangle$`)
-   Next we represent the force *P* as a vector, `$p_i = \langle P, 0, 0 \rangle$`
-   Balancing forces yields

`$t_i A - p_i = 0$`

-   We find `$t_1 = \frac{P}{A} = \sigma_{11}$`, `$t_2 = 0 = \sigma_{12}$` and `$t_3 = 0 = \sigma_{13}$`

----
## example

-   No force is applied in the other directions, so it is trivial to find the rest of the stress tensor

`$$\sigma_{ij} = \begin{bmatrix}
	P/A & 0 & 0\\
	0 & 0 & 0\\
	0 & 0 & 0
\end{bmatrix}$$`

----
## example

-   We can now consider any arbitrary angle of interior cut.
-   The normal for a cut as shown in the diagram will be `$n_i = \langle cos \theta, \sin \theta, 0 \rangle$`.
-   We can again use `$t_j = \sigma_{ij}n_i$` to find `$t_j$` for any angle

`$$\begin{aligned}
	t_1 &= \frac{P}{A} \cos \theta \\
	t_2 &= 0\\
	t_3 &= 0
\end{aligned}$$`

---
# stress transformation

----
## stress transformation

-   Stress transformation equations are identical to the strain transformation equations
-   Both stress and strain are tensor, and transform in the same fashion
-   Rotation about z-axis gives

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
## stress transformation

-   We recall that

`$$\sigma_{ij}^\prime = Q_{im}Q_{jn}\sigma_{mn}$$`

-   Which gives

`$$\begin{aligned}
	\sigma^\prime_x &= \sigma_x \cos ^2 \theta + \sigma_y \sin^2 \theta + 2 \tau_{xy} \sin \theta \cos \theta \\
	\sigma^\prime_y &= \sigma_x \sin ^2 \theta + \sigma_y \cos^2 \theta - 2 \tau_{xy} \sin \theta \cos \theta \\
	\tau^\prime_{xy} &= -\sigma_x \sin \theta \cos \theta + \sigma_y \sin \theta \cos \theta + \tau_{xy} (\cos^2 \theta - \sin^2 \theta)
\end{aligned}$$`

----
## stress transformation

-   As with the strain transformation equations, these are often re-written using the double-angle formulae.

`$$\begin{aligned}
	\sigma^\prime_x &= \frac{\sigma_x + \sigma_y}{2} + \frac{\sigma_x - \sigma_y}{2}\cos 2\theta + \tau_{xy} \sin 2\theta \\
	\sigma^\prime_y &= \frac{\sigma_x + \sigma_y}{2} - \frac{\sigma_x - \sigma_y}{2}\cos 2\theta - \tau_{xy} \sin 2\theta \\
	\tau^\prime_{xy} &= \frac{\sigma_y - \sigma_x}{2}\sin 2\theta + \tau_{xy} \cos 2\theta
\end{aligned}$$`

---
# principal stresses

----
## principal stresses

-   Principal stresses can be found in the same fashion as principal values and principal strains

`$$\det [\sigma_{ij} - \sigma_{kk} \delta_{ij}]=0$$`

----
## tractions

<div class="left"> <!-- .element width="65%" -->
	
-   We can use what we know about principal values to find some interesting things about the tractions
-   Consider the traction vector on an arbitrary internal face, and decompose into Normal and Shear components.

</div>

<div class="right"> <!-- .element width="35%" -->
	
![arbitrary body with arbitrary loading applied](../images/potato.PNG)

</div>

----
## tractions

-   The normal component can be found using the dot product

`$$N = \hat{T}^n \cdot \hat{n}$$`

-   The shear component can be found using the Pythagorean theorem

`$$S^2 = |\hat{T}^n|^2 - N^2$$`

----
## tractions

-   We now use the stress tensor in the principal direction to simplify the calculations

`$$\begin{aligned}
	N &= \hat{T}^n \cdot \hat{n}\\
	&= T^n_i n_i \\
	&= \sigma_{ji} n_j n_i\\
	&= \sigma_1 n_1^2 + \sigma_2 n_2^2 + \sigma_3 n_3^2
\end{aligned}$$`

----
## tractions

-   We also know that

`$$\begin{aligned}
	|\hat{T}^n|^2 &= \hat{T}^n \cdot \hat{T}^n\\
	&= T_i^n T_i^n \\
	&= \sigma_{ji} n_j \sigma_{ki} n_k\\
	&= \sigma_1^2 n_1^2 + \sigma_2^2 n_2^2 + \sigma_3^2 n_3^2
\end{aligned}$$`

----
## mohr’s circle

-   If we constrain the normal vector to be a unit vector we can formulate the following inequalities

`$$\begin{aligned}
	S^2 + (N-\sigma_2)(N-\sigma_3) &\ge 0\\
	S^2 + (N-\sigma_3)(N-\sigma_1) &\le 0\\
	S^2 + (N-\sigma_1)(N-\sigma_2) &\ge 0\\
\end{aligned}$$`

-   These inequalities form what is known as Mohr’s circle

----
## mohr’s circle

![mohr's circle](../images/mohr.PNG) <!-- .element width="60%" -->

---
# maximum shear stress

----
## maximum shear stress

-   From Mohr’s circle, we can find the maximum shear stress in terms of the principal stresses

`$$S_{max} = (\sigma_1 - \sigma_3)/2$$`

----
## maximum shear stress

-   For plane stress problems, we can also use the stress transformation equations to find the maximum shear stress
-   We desire to maximize this equation:

`$$\tau^\prime_{xy} = \frac{\sigma_y - \sigma_x}{2}\sin 2\theta + \tau_{xy} \cos 2\theta$$`

----
## maximum shear stress

-   Taking the derivative with respect to `$\theta$` gives

`$$\frac{\partial}{\partial \theta} (\tau^\prime_{xy}) = (\sigma_y-\sigma_x)\cos 2\theta - 2\tau_{xy} \sin 2\theta = 0$$`

-   Which we can use to find `$2\theta$`

`$$2\theta = \tan ^{-1} \left(\frac{(\sigma_y-\sigma_x)}{2\tau_{xy}}\right)$$`

----
## maximum shear stress

-   Substituting back into the original equation gives

`$$\tau^\prime_{max} = \frac{\sigma_y - \sigma_x}{2}\sin \left[\tan ^{-1} \left(\frac{(\sigma_y-\sigma_x)}{2\tau_{xy}}\right)\right] + \tau_{xy} \cos \left[\tan ^{-1} \left(\frac{(\sigma_y-\sigma_x)}{2\tau_{xy}}\right)\right]$$`

-   Note that

`$$\begin{aligned}
	\sin (\tan ^{-1} (x)) &= \frac{x}{\sqrt{1+x^2}}\\
	\cos (\tan ^{-1} (x)) &= \frac{1}{\sqrt{1+x^2}}\\
\end{aligned}$$`

----
## maximum shear stress

-   We note that

`$$\sqrt{1+ \left(\frac{\sigma_y - \sigma_x}{2 \tau_{xy}}\right)^2} = \frac{\sqrt{(\sigma_y-\sigma_x)^2+4\tau_{xy}^2}}{2\tau_{xy}}$$`

-   And thus we find

`$$\tau_{max} = \frac{(\sigma_y-\sigma_x)^2}{2 \sqrt{(\sigma_y-\sigma_x)^2+4\tau_{xy}^2}} + \frac{4\tau_{xy}^2}{2 \sqrt{(\sigma_y-\sigma_x)^2+4\tau_{xy}^2}}$$`

----
## maximum shear stress

-   Adding the terms and simplifying, we find

`$$\tau_{max} = \sqrt{\left(\frac{\sigma_y-\sigma_x}{2}\right)^2+\tau_{xy}^2}$$`

---
# group problems

----
## group one

<div class="left">

-   The stress state in a rectangle under biaxial loading is

`$$\sigma_{ij} = \begin{bmatrix} X & 0 & 0\\
	0 & Y & 0\\
0 & 0 & 0\end{bmatrix}$$`


</div>

<div class="right">
	
-   Find the traction vector, as well as the normal and shearing stresses on some oblique plane, *S*

</div>

![group problem 1](../images/group-3-1.png) <!-- .element width="40%" -->

----
## group two

<div class="left">
	
-   For the figure shown, what must the traction be on the other faces for the stress to be uniform and in equilibrium?

</div>

<div class="right">
	
![group problem 2](../images/group-3-2.png)

</div>

----
## group three

<div class="left">
	
-   For the figure shown, find the (uniform) stress tensor. What must the traction be on the last face?

</div>

<div class="right">
	
![group problem 3](../images/group-3-3.png)

</div>
