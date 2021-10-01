# AE731
## Theory of Elasticity
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering
September 30, 2021

----
## upcoming schedule

-   Sep 30 - Problem Formulation
-   Oct 5 - Strain Energy
-   Oct 7 - Exam 2 Review
-   Oct 8 - Homework 4 Self-grade Due, Homework 5 Due
-   (Oct 12) - Fall Break (No Class)
-   Oct 14 - Exam 2 

----
## outline

<!-- vim-markdown-toc GFM -->

* review
* displacement formulation
* principle of superposition
* saint-venant’s principle
* examples

<!-- vim-markdown-toc -->

---
# review

----
## field equations

`$$\begin{aligned}
	\epsilon_{ij} &= \frac{1}{2}(u_{i,j} + u_{j,i}) &\text{Strain-Displacement} \\
	\sigma_{ij,j} + F_i &= 0 &\text{Equilibrium} \\
	\sigma_{ij} &= \lambda \epsilon_{kk}\delta_{ij} + 2\mu \epsilon_{ij} &\text{Constitutive (Hooke's Law)}\\
	\epsilon_{ij} &= \frac{1+\nu}{E}\sigma_{ij} - \frac{\nu}{E}\sigma_{kk} \delta_{ij} &
\end{aligned}$$`

----
## field equations

-   There are 15 unique field equations to solve for the 15 unknowns
-   3 displacements `$(u_i)$`, 6 unique strain tensor terms (`$\epsilon_{ij}$`) and 6 unique stress tensor terms (`$\sigma_{ij}$`)
-   These equations also depend on a knowledge of the material behavior (`$\lambda, \mu$`) and body forces (usually gravity or zero)

----
## compatibility equations

-   If continuous, single-valued displacements are specified, differentiation will result in well-behaved strain field
-   The inverse relationship, integration of a strain field to find displacement, may not always be true
-   There are cases where we can integrate a strain field to find a set of discontinuous displacements

----
## compatibility equations

`$$\begin{aligned}
	\frac{\partial^2 \epsilon_x}{\partial y^2} + \frac{\partial^2 \epsilon_y}{\partial x^2} &= 2\frac{\partial^2 \epsilon_{xy}}{\partial x \partial y}\\
	\frac{\partial^2 \epsilon_y}{\partial z^2} + \frac{\partial^2 \epsilon_z}{\partial y^2} &= 2\frac{\partial^2 \epsilon_{yz}}{\partial y \partial z}\\
	\frac{\partial^2 \epsilon_z}{\partial x^2} + \frac{\partial^2 \epsilon_x}{\partial z^2} &= 2\frac{\partial^2 \epsilon_{zx}}{\partial z \partial x}\\
	\frac{\partial^2 \epsilon_x}{\partial y \partial z} &= \frac{\partial}{\partial x} \left(-\frac{\partial \epsilon_{yz}}{\partial x} + \frac{\partial \epsilon_{zx}}{\partial y} + \frac{\partial \epsilon_{xy}}{\partial z}\right)\\
	\frac{\partial^2 \epsilon_y}{\partial z \partial x} &= \frac{\partial}{\partial y} \left(-\frac{\partial \epsilon_{zx}}{\partial y} + \frac{\partial \epsilon_{xy}}{\partial z} + \frac{\partial \epsilon_{yz}}{\partial x}\right)\\
	\frac{\partial^2 \epsilon_z}{\partial x \partial y} &= \frac{\partial}{\partial z} \left(-\frac{\partial \epsilon_{xy}}{\partial z} + \frac{\partial \epsilon_{yz}}{\partial x} + \frac{\partial \epsilon_{zx}}{\partial y}\right)
\end{aligned}$$`

----
## beltrami-michell 

`$$\begin{aligned}
	(1+\nu) \nabla^2 \sigma_x + \frac{\partial^2}{\partial x^2} (\sigma_x + \sigma_y + \sigma_z) &= 0\\
	(1+\nu) \nabla^2 \sigma_y + \frac{\partial^2}{\partial y^2} (\sigma_x + \sigma_y + \sigma_z) &= 0\\
	(1+\nu) \nabla^2 \sigma_z + \frac{\partial^2}{\partial z^2} (\sigma_x + \sigma_y + \sigma_z) &= 0\\
	(1+\nu) \nabla^2 \tau_{xy} + \frac{\partial^2}{\partial x \partial y} (\sigma_x + \sigma_y + \sigma_z) &= 0\\
	(1+\nu) \nabla^2 \tau_{yz} + \frac{\partial^2}{\partial y \partial z} (\sigma_x + \sigma_y + \sigma_z) &= 0\\
	(1+\nu) \nabla^2 \tau_{zx} + \frac{\partial^2}{\partial z \partial x} (\sigma_x + \sigma_y + \sigma_z) &= 0\\
\end{aligned}$$`

----
## stress formulation

-   For traction problems (i.e. traction is defined on all surfaces) it is convenient to re-formulate field equations in terms of stress only
-   Since displacements are eliminated, we will need to use the compatibility equations to ensure a continuous displacement field
-   It is desirable for this formulation to write the compatibility equations in terms of stress

----
## boundary conditions

![boundary conditions illustration](../images/bcs.PNG)

----
## symmetric boundaries

![symmetric boundaries illustration](../images/symmetric.PNG)

----
## boundaries

-   In many systems, the boundaries are parallel to the coordinate system, but this is not always the case

![illustration of boundary conditions not parallel to coordinate system](../images/noncoordinate.PNG) <!-- .element width="50%" -->

----
## solution procedure

-   Solution procedure for stress/traction problems:
	-   Assume stress function
	-   Must be capable of meeting boundary conditions (linear, quadratic, etc.)
	-   Enforce equilibrium
	-   Check compatibility
	-   Enforce boundary conditions

---
# displacement formulation

----
## displacement formulation

-   Just as we posed all field equations in terms of stress for traction problems, it is convenient to pose all the field equations in terms of displacement when dealing with displacement boundary conditions
-   We can use the strain-displacement relations in Hooke’s law to find

`$$\sigma_{ij} = \lambda u_{k,k} \delta + \mu (u_{i,j} + u_{j,i})$$`

----
## navier’s equations

-   We can substitute this relationship into the equilibrium equations to find

`$$\mu u_{i,kk} + (\lambda + \mu)u_{k,ki} + F_i = 0$$`

-   This is known as *Navier’s* or *Lamé’s equations* and is sometimes written in vector form as


`$$\mu \nabla^2 \mathbf{u} + (\lambda + \mu) \nabla(\nabla \cdot \mathbf{u}) + \mathbf{F} = 0$$`

----
## solutions

-   General solutions to Navier’s equations are very difficult to obtain (as with the stress solution)
-   Later in the course, we will learn about *stress functions* and *displacement potential functions*
-   These functions provide a starting point to simplify solving this complicated partial differential equations

----
## example

-   Determine when the following quadratic displacement field will be in equilibrium

`$$\begin{aligned}
	u &= a_1 x^2 + b_1 y^2 + c_1 xy + d_1 x + e_1 y + f_1\\
	v &= a_2 x^2 + b_2 y^2 + c_2 xy + d_2 x + e_2 y + f_2\\
	w &= a_3 x^2 + b_3 y^2 + c_3 xy + d_3 x + e_3 y + f_3\\
\end{aligned}$$`

----
## example

-   We use the equilibrium equations in displacement

`$$\mu u_{i,kk} + (\lambda + \mu)u_{k,ki} + F_i = 0$$`

-   If we consider `$u_{i,kk}$`, we find

`$$\begin{aligned}
	u_{1,kk} &= 2a_1 + 2b_1\\
	u_{2,kk} &= 2a_2 + 2b_2\\
	u_{3,kk} &= 2a_3 + 2b_3
\end{aligned}$$`

----
## example

-   The next term is more difficult, so first let us note that `$u_{k,ki} = (u_{k,k})_{,i}$`
-   This gives

`$$u_{k,ki} = (2a_1x + c_1y + d_1 + 2b_2y + c_2x + e_2 + 0)_{,i}$$`

-   We can now differentiate this to find

`$$\begin{aligned}
	u_{k,k1} &= 2a_1 + c_2\\
	u_{k,k2} &= c_1 + 2b_2\\
	u_{k,k3} &= 0
\end{aligned}$$`

----
## example

-   Finally, we can obtain the equilibrium equations as

`$$\begin{aligned}
	\mu(2a_1 + 2b_1) + (\lambda+\mu)(2a_1 + c_2) + F_x &= 0\\
	\mu(2a_2 + 2b_2) + (\lambda+\mu)(c_1 + 2b_2) + F_y &= 0\\
	\mu(2a_3 + 2b_3) + (\lambda+\mu)(0) + F_z &= 0
\end{aligned}$$`

---
# principle of superposition

----
## superposition

-   Any problem governed by linear equations can be superposed
-   By the principle of superposition if

`$$\sigma_{ij}^{(1)} , \epsilon_{ij}^{(1)}, u_i^{(1)}$$`

are the solution to an elasticity problem with body forces `$F_i^{(1)}$` and surface tractions `$t_i^{(1)}$` and

`$$\sigma_{ij}^{(2)} , \epsilon_{ij}^{(2)}, u_i^{(2)}$$`

are the solution to an elasticity problem with body forces `$F_i^{(2)}$` and surface tractions `$t_i^{(2)}$`, then

`$$\sigma_{ij}^{(1)} + \sigma_{ij}^{(2)}, \epsilon_{ij}^{(1)} + \epsilon_{ij}^{(2)}, u_i^{(1)} + u_i^{(2)}$$`

are the solution to that problem with body forces `$F_i^{(1)} + F_i^{(2)}$` and surface tractions `$t_i^{(1)} + t_i^{(2)}$`

----
## superposition

-   Superposition is a very useful tool in real elasticity problems
-   A large number of basic elasticity solutions have already been solved, these can be looked up
-   Basic problems often do not have direct real-world applications
-   Many real-world problems can be broken down into the sum of multiple basic problems

----
## principle of superposition

![superposition](../images/superposition1.PNG)

---
# saint-venant’s principle

----
## saint-venant’s principle

<div class="left">
	
-   The stress, strain, and displacement fields caused by statically equivalent forces are approximately the same far away from the load points

</div>

<div class="right">
	
![equivalent boundary conditions illustrated](../images/saint-venant.PNG)

</div>


----
## saint-venant’s principle

-   Often the stress/strain field we are concerned with is far away from the load point
-   In this case we can use a statically equivalent load
-   We apply the load in whatever way makes the problem easiest

---
# examples

----
## baseball

-   Consider a baseball with an incompressible rubber core
-   Model the stress field due to some external pressure, `$p$` given the governing equation is

`$$\frac{\partial}{\partial r} \left( \frac{1}{r^2} \frac{\partial }{\partial r}(r^2 u_r)\right) = 0$$`

----
## hollow cylinder

-   Consider a long, hollow cylinder with pressure applied on both the inner and outer faces
-   Find the stress field given the governing equation

`$$\frac{\partial}{\partial r} \left( \frac{1}{r} \frac{\partial}{\partial r} (ru_r)\right) = 0$$`

---
# group problems

----
## problem one - thermoelasticity

As a first-order model of the problem of freezing water in a glass bottle, we treat water as a thermoelastic solid and the glass as a fixed boundary.
Find the stress and strain field in the water as a function of the elastic properties ($E,\nu$) and the coefficient of thermal expansion ($\alpha$).

----
## problem two - inverse solution

Consider the stress field

`$$ \sigma = \begin{bmatrix} Ay & 0 & 0 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{bmatrix}  $$`

Show that this is a valid solution to an elasticity problem.
What problem does it solve?

----
## problem three - semi-inverse

To solve the problem of torsion in prismatic bars we consider the displacement field

`$$ u = -\alpha y z, \qquad v = -\alpha x z, \qquad w = w(x,y) $$`

Solve this problem using the boundary conditions for a solid square cross-section.


