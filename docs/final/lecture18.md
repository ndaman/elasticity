# AE731
## Theory of Elasticity
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering
2 November, 2021

----
## upcoming schedule

-   Nov 2 - 2D Problems
-   Nov 4 - Airy Stress
-   Nov 5 - Homework 6 Self-Grade Due
-   Nov 9 - Polar Coordinates
-   Nov 11 - Micromechanics Project Presentation
-   Nov 12 - Homework 7 Due

----
## outline

<!-- vim-markdown-toc GFM -->

* two-dimensional problems
* plane strain
* plane stress
* generalized plane stress

<!-- vim-markdown-toc -->

---
# two-dimensional problems

----
## 2d problems

-   As we learned in Chapter 5, it is often very difficult to solve full problems in 3D
-   Some problems contain symmetry, or particular geometries which allow certain simplifications to be made
-   In this chapter we will consider the following 2D formulations
    -   Plane strain
    -   Plane stress
    -   Generalized plane stress
    -   Antiplane strain

----
## 2d problems

-   Airy stress functions provide a systematic method for solving 2D problems
-   We will also develop Airy stress function solution methods in polar (cylindrical or spherical) coordinates

---
# plane strain

----
## plane strain

-   Plane strain is a state we consider for very long bodies
-   If the body is sufficiently long, then the deformation field can be considered to be a function of *x* and *y* only

`$$\begin{aligned}
	u &= u(x,y)\\
	v &= v(x,y)\\
	w &= 0
\end{aligned}$$`

----
## plane strain

-   We can use the strain-displacement relations to find the corresponding strains from our assumptions on the displacement

`$$\begin{aligned}
	\epsilon_{xx} &= \frac{\partial u}{\partial x}\\
	\epsilon_{yy} &= \frac{\partial v}{\partial y}\\
	\epsilon_{xy} &= \frac{1}{2}\left(\frac{\partial u}{\partial y} + \frac{\partial v}{\partial x}\right)\\
	\epsilon_{zz} &= \epsilon_{xz} = \epsilon_{yz} = 0
\end{aligned}$$`

----
## plane strain

-   We can use Hooke’s law to find the stresses

`$$\begin{aligned}
	\sigma_{xx} &= \lambda(\epsilon_{xx} + \epsilon_{yy}) + 2\mu \epsilon_{xx}\\
	\sigma_{yy} &= \lambda(\epsilon_{xx} + \epsilon_{yy}) + 2\mu \epsilon_{yy}\\
	\sigma_{zz} &= \lambda(\epsilon_{xx} + \epsilon_{yy})\\
	\tau_{xy} &= 2\mu \epsilon_{xy} \\
	\tau_{xz} &= \tau_{yz} = 0
\end{aligned}$$`

----
## plane strain

-   We can use these relationships to reduce the equilibrium equations.
-   Recall that for equilibrium we have

`$$\sigma_{ij,j} + F_i = 0$$`

`$$\tau_{xz} = \tau_{yz} = 0$$`, so those terms will vanish

----
## plane strain

-   Although `$\sigma_{zz} \ne 0$`, it only appears with a derivative of *z*, and it is a function of *x* and *y* only, so `$\sigma_{zz}$` will not appear in any non-trivial equilibrium equation

`$$\begin{aligned}
	\frac{\partial \sigma_{xx}}{\partial x} + \frac{\partial \tau_{xy}}{\partial y} + F_x &= 0\\
	\frac{\partial \tau_{xy}}{\partial x} +\frac{\partial \sigma_{yy}}{\partial y} +  F_y &= 0
\end{aligned}$$`

----
## plane strain

-   We can use the strain-displacement equations and Hooke’s Law to write Navier’s equations for plane strain

`$$\begin{aligned}
	\mu \nabla^2 u + (\lambda + \mu) \frac{\partial}{\partial x} \left(\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y}\right) + F_x &= 0\\
	\mu \nabla^2 v + (\lambda + \mu) \frac{\partial}{\partial y} \left(\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y}\right) + F_x &= 0
\end{aligned}$$`

----
## compatibility

`$$\begin{aligned}
	\frac{\partial^2 \epsilon_x}{\partial y^2} + \frac{\partial^2 \epsilon_y}{\partial x^2} &= 2\frac{\partial^2 \epsilon_{xy}}{\partial x \partial y}\\
	\frac{\partial^2 \epsilon_y}{\partial z^2} + \frac{\partial^2 \epsilon_z}{\partial y^2} &= 2\frac{\partial^2 \epsilon_{yz}}{\partial y \partial z}\\
	\frac{\partial^2 \epsilon_z}{\partial x^2} + \frac{\partial^2 \epsilon_x}{\partial z^2} &= 2\frac{\partial^2 \epsilon_{zx}}{\partial z \partial x}\\
	\frac{\partial^2 \epsilon_x}{\partial y \partial z} &= \frac{\partial}{\partial x} \left(-\frac{\partial \epsilon_{yz}}{\partial x} + \frac{\partial \epsilon_{zx}}{\partial y} + \frac{\partial \epsilon_{xy}}{\partial z}\right)\\
	\frac{\partial^2 \epsilon_y}{\partial z \partial x} &= \frac{\partial}{\partial y} \left(-\frac{\partial \epsilon_{zx}}{\partial y} + \frac{\partial \epsilon_{xy}}{\partial z} + \frac{\partial \epsilon_{yz}}{\partial x}\right)\\
	\frac{\partial^2 \epsilon_z}{\partial x \partial y} &= \frac{\partial}{\partial z} \left(-\frac{\partial \epsilon_{xy}}{\partial z} + \frac{\partial \epsilon_{yz}}{\partial x} + \frac{\partial \epsilon_{zx}}{\partial y}\right)
\end{aligned}$$`

----
## plane strain

-   The only non-trivial term from the compatibility equations is

`$$\frac{\partial^2 \epsilon_x}{\partial y^2} + \frac{\partial^2 \epsilon_y}{\partial x^2} = 2\frac{\partial^2 \epsilon_{xy}}{\partial x \partial y}$$`

-   This can also be written in terms of stress (Beltrami-Mitchell)

`$$\nabla^2(\sigma_x + \sigma_y) = -\frac{1}{1-\nu}\left(\frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y}\right)$$`

----
## plane strain

-   Plane strain is exact for a body of infinite length, but can also be useful for real shapes of finite length
-   Consider a long body with fixed and frictionless ends.
-   The boundary conditions for this case are

`$$\begin{aligned}
	w(x,y,\pm L) &= 0\\
	\tau_{xz}(x,y,\pm L) &= 0\\
	\tau_{yz}(x,y,\pm L) &= 0
\end{aligned}$$`

---
# plane stress

----
## plane stress

-   If the thickness of a body is small compared to the other dimensions, we assume that there can not be much variation in any of the stress components in that direction
-   The assumptions for plane stress can be summarized as

`$$\begin{aligned}
	\sigma_x &= \sigma_x(x,y)\\
	\sigma_y &= \sigma_y(x,y)\\
	\tau_{xy} &= \tau_{xy}(x,y)\\
	\sigma_z &= \tau_{xz} = \tau_{yz} = 0
\end{aligned}$$`

----
## plane stress

-   To maintain these assumptions, there can be no body forces in the *z*-direction and no applied tractions in the *z*-direction.
-   Other body forces must be independent of *z*, or distributed symmetrically such that the average may be used.

----
## plane stress

-   We can use Hooke’s law to find the corresponding values of strain

`$$\begin{aligned}
	\epsilon_x &= \frac{1}{E}(\sigma_x - \nu \sigma_y)\\
	\epsilon_y &= \frac{1}{E}(\sigma_y - \nu \sigma_x)\\
	\epsilon_z &= -\frac{\nu}{E}(\sigma_x + \sigma_y)\\
	\epsilon_{xy} &= \frac{1+\nu}{E}\tau_{xy}\\
	\epsilon_{xz} &= \epsilon_{yz} = 0
\end{aligned}$$`

----
## strain-displacement

`$$\begin{aligned}
	\epsilon_{x} &= \frac{\partial u}{\partial x}\\
	\epsilon_{y} &= \frac{\partial v}{\partial y}\\
	\epsilon_{z} &= \frac{\partial w}{\partial z}\\
	\epsilon_{xy} &= \frac{1}{2}\left(\frac{\partial u}{\partial y} + \frac{\partial v}{\partial x}\right)\\
	\epsilon_{yz} &= \frac{1}{2}\left(\frac{\partial v}{\partial z} + \frac{\partial w}{\partial y}\right) = 0\\
	\epsilon_{xz} &= \frac{1}{2}\left(\frac{\partial u}{\partial z} + \frac{\partial w}{\partial x}\right) = 0\\
\end{aligned}$$`

----
## plane stress

-   Since strain in the *z*-direction is not zero, *w* becomes a linear function of *z*
-   We also find that *u* and *v* will also be functions of *z*
-   These effects are normally neglected, leading to an approximation in the formulation
-   This is why we cannot use the full 3D compatibility equations to assess compatibility of a body with an assumed state of plane stress

----
## plane stress

-   The equilibrium equations reduce the same form in plane stress as they did for plane strain

`$$\begin{aligned}
	\frac{\partial \sigma_{xx}}{\partial x} + \frac{\partial \tau_{xy}}{\partial y} + F_x &= 0\\
	\frac{\partial \tau_{xy}}{\partial x} +\frac{\partial \sigma_{yy}}{\partial y} +  F_y &= 0
\end{aligned}$$`

-   But the Navier equations in terms of displacement do not reduce to exactly the same form

`$$\begin{aligned}
	\mu \nabla^2 u + \frac{E}{2(1-\nu)} \frac{\partial}{\partial x} \left(\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y}\right) + F_x &= 0\\
	\mu \nabla^2 v + \frac{E}{2(1-\nu)} \frac{\partial}{\partial y} \left(\frac{\partial u}{\partial x} + \frac{\partial v}{\partial y}\right) + F_y &= 0
\end{aligned}$$`

----
## navier equations

-   The factor in the plane strain Navier equations is

`$$(\lambda + \mu)$$`

-   We can convert this to `$E$`, `$\nu$` to better compare with the plane stress equation

----
## navier equations

`$$\begin{aligned}
	\lambda + \mu &= \frac{\nu E}{(1+\nu)(1-2\nu)} + \frac{E}{2(1+\nu)}\\
	&= \frac{2\nu E}{2(1+\nu)(1-2\nu)} + \frac{E(1-2\nu)}{2(1+\nu)(1-2\nu)}\\
	&= \frac{2\nu E + E - 2\nu E}{2(1+\nu)(1-2\nu)}\\
	&= \frac{E}{2(1+\nu)(1-2\nu)}
\end{aligned}$$`

----
## compatibility

-   Due to the approximations we made earlier, we neglect all compatibility equations with `$\epsilon_z$`, even though these may not be zero

`$$\frac{\partial^2 \epsilon_x}{\partial y^2} + \frac{\partial^2 \epsilon_y}{\partial x^2} = 2 \frac{\partial^2 \epsilon_{xy}}{\partial x \partial y}$$`

-   or in terms of stress

`$$\nabla^2 (\sigma_{xx} + \sigma_{yy}) = -(1+\nu)\left(\frac{\partial F_x}{\partial x} + \frac{\partial F_y}{\partial y}\right)$$`

----
## conversion

-   While plane strain and plane stress give similar results, they are not identical
-   We can convert between plane strain and plane stress by replacing *E* and `$\nu$`


|                              |              *E*              |       `$\nu$`       |
|:----------------------------:|:-----------------------------:|:-------------------:|
| Plane stress to plane strain |     `$\frac{E}{1-\nu^2}$`     | `$\frac{v}{1-\nu}$` |
| Plane strain to plane stress | `$\frac{E(1+2\nu)}{1+\nu^2}$` | `$\frac{v}{1+\nu}$` |

-   When `$\nu = 0$`, plane strain and plane stress give identical results

---
# generalized plane stress

----
## generalized plane stress

-   Some approximations introduced inconsistencies in the plane stress formulation
-   Generalized plane stress is based on averaging the field quantities through the thickness

`$$\bar{\psi} = \frac{1}{2h} \int_{-h}^{h}\psi (x,y,z) dz$$`

----
## generalized 

-   We again assume that the thickness, `$2h$`, is much smaller than the other dimensions
-   We also assume that tractions on the surfaces `$z = \pm h$` are zero
-   Edge loadings must have no *z* component and are independent of *z*
-   Body forces also cannot have a *z* component and must be independent of *z* or symmetrically distributed through the thickness
-   This gives *w* as a linear function of *z* which means

`$$w(x,y,z) = -w(x,y,-z)$$`

----
## average field variables

`$$\begin{aligned}
	\bar{u} &= \bar{u}(x,y)\\
	\bar{v} &= \bar{v}(x,y)\\
	\bar{w} &= \bar{w}(x,y)\\
	\bar{\sigma_z} &= \bar{\tau_{xz}} = \bar{\tau_{yz}} = 0\\
	\bar{\sigma_x} &= \lambda^*(\bar{\epsilon_x}+\bar{\epsilon_y}) + 2\mu \bar{\epsilon_x}\\
	\bar{\sigma_y} &= \lambda^*(\bar{\epsilon_x}+\bar{\epsilon_y}) + 2\mu \bar{\epsilon_y}\\
	\bar{\tau_{xy}} &= 2\mu \bar{\epsilon_{xy}}\\
	\bar{\epsilon_z} &= - \frac{\lambda}{\lambda + 2\mu} (\bar{\epsilon_x}+ \bar{\epsilon_y})
\end{aligned}$$`

-   Where `$\lambda^* = \frac{2\lambda \mu}{\lambda + 2\mu}$`

----
## generalized plane stress

-   We can also write the equilibrium equations in terms of the averaged values

`$$\begin{aligned}
	\frac{\partial \bar{\sigma_x}}{\partial x} + \frac{\partial \bar{\tau_{xy}}}{\partial x} + \bar{F}_x &= 0\\
	\frac{\partial \bar{\tau_{xy}}}{\partial x} + \frac{\partial \bar{\sigma_{y}}}{\partial y} + \bar{F}_y &= 0
\end{aligned}$$`

----
## generalized plane stress

-   Or in terms of displacements

`$$\begin{aligned}
	\mu \nabla^2 \bar{u} + (\lambda^* + \mu) \frac{\partial}{\partial x} \left(\frac{\partial \bar{u}}{\partial x} + \frac{\partial \bar{v}}{\partial y}\right) + \bar{F}_x &= 0\\
	\mu \nabla^2 \bar{u} + (\lambda^* + \mu) \frac{\partial}{\partial y} \left(\frac{\partial \bar{u}}{\partial x} + \frac{\partial \bar{v}}{\partial y}\right) + \bar{F}_y &= 0
\end{aligned}$$`

----
## compatibility

-   The compatibility relations reduce to

`$$\nabla^2 (\bar{\sigma_x} + \bar{\sigma_y}) = - \frac{2(\lambda^* + \mu)}{\lambda^* + 2\mu} \left(\frac{\partial \bar{F}_x}{\partial x} + \frac{\partial \bar{F}_y}{\partial y}\right)$$`

----
## compatibility

-   When we write the coefficient `$\frac{2(\lambda^* + \mu)}{\lambda^* + 2\mu}$` in terms of *E* and `$\nu$`, we find

`$$\frac{2(\lambda^* + \mu)}{\lambda^* + 2\mu} = 1 + \nu$$`

-   Which means this is an identical result to the simple plane stress derivation
-   Thus the generalized plane stress method is not particularly useful

----
## beam example

![beam bending example](../images/figure_1.png)
