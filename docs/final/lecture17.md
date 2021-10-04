# AE731
## Theory of Elasticity
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering
October 19, 2021

----
## upcoming schedule

-   Oct 19 - Exam Return, Virtual Work
-   Oct 21 - Airy Stress Functions
-   Oct 22 - Homework 5 Self-Grade Due
-   Oct 26 - Airy Stress
-   Oct 28 - Airy Stress
-   Oct 29 - Homework 6 Due

----
## outline

<!-- vim-markdown-toc GFM -->

* integral theorems
* virtual work
* ritz method

<!-- vim-markdown-toc -->

---
# integral theorems

----
## clapeyron’s theorem

-   If we return to the uniqueness derivation, the only non-general assumptions were

`$$\begin{aligned}
	\sigma_{ij,j} &= 0\\
	T_i^n &= \sigma_{ij}n_j = 0 \qquad \text{Along traction boundary}\\
	u_i &= 0 \qquad \text{Along displacement boundary} \\
\end{aligned}$$`

----
## clapeyron’s theorem

-   This means that for any elastic body we can say

`$$2\int_V U dV = \int_S \sigma_{ij}n_j u_i dS - \int_V \sigma_{ij,j}u_i dV$$`

----
## clapeyron’s theorem

-   If we consider an elastic body in equilibrium, we can say that

`$$\sigma_{ij,j} = -F_i$$`

-   We also know by Cauchy’s stress theorem that

`$$t_i = \sigma_{ij}n_j$$`

-   Both of these can be substituted to give

`$$2\int_V U dV = \int_S t_i u_i dS + \int_V F_i u_i dV$$`


----
## betti/rayleigh reciprocal theorem

-   We can derive another theorem by returning to

`$$2\int_V U dV = \int_S \sigma_{ij}n_j u_i dS - \int_V \sigma_{ij,j}u_i$$`

-   Consider two different sets of forces and displacements acting on the same body

`$t_i^{(1)}$`, `$F_i^{(1)}$`, `$u_i^{(1)}$` and `$t_i^{(2)}$`, `$F_i^{(2)}$`, `$u_i^{(2)}$`

----
## reciprocal theorem

-   We now consider the work done by the forces in the first system acting through the displacements of the second system

`$$2\int_V UdV = \int_V \sigma_{ij}^{(1)}\epsilon_{ij}^{(2)} = \int_S t_i^{(1)}u_i^{(2)}dS + \int_V F_i^{(1)}u_i^{(2)}dV$$`

-   We can similarly write

`$$\int_V \sigma_{ij}^{(2)}\epsilon_{ij}^{(1)} = \int_S t_i^{(2)}u_i^{(1)}dS + \int_V F_i^{(2)}u_i^{(1)}dV$$`

----
## reciprocal theorem

-   We can now use Hooke’s Law and symmetry to say that

`$$\sigma_{ij}^{(1)}\epsilon_{ij}^{(2)} = C_{ijkl}\epsilon_{kl}^{(1)}\epsilon_{ij}^{(2)} = \epsilon_{kl}^{(1)} \sigma_{kl}^{(2)}$$`

-   If `$\sigma_{ij}^{(1)}\epsilon_{ij}^{(2)} = \sigma_{ij}^{(2)}\epsilon_{ij}^{(1)}$`, then we can also say that the strain energies are equivalent, proving the Betti/Rayleigh Reciprocal Theorem

`$$\int_S t_i^{(1)}u_i^{(2)}dS + \int_V F_i^{(1)} u_i^{(2)}dV = \int_S t_i^{(2)}u_i^{(1)}dS + \int_V F_i^{(2)}u_i^{(1)}dV$$`

----
## integral elasticity

-   The Betti/Rayleigh Reciprocal Theorem is used to derive the Integral Formulation of Elasticity
-   Also known as Somigliana’s Identity
-   Used for Boundary Element Method (BEM) and Boundary Integral Equation methods (BIE), but we will not use it in this class

---
# virtual work

----
## virtual work

-   The solution format we developed in Chapter 5 is known as *Strong Form*, and is not always a convenient solution form
-   We can use energy and work principles to develop additional solution methods
-   *Virtual Displacement* is a fictitious displacement such that the forces acting on the point remain unchanged
-   The work done by these forces is known as *Virtual Work*

----
## virtual work

-   If we consider the elastic boundary-value problem, with tractions applied over the boundary `$S_t$` and displacements applied over the boundary `$S_u$`.
-   Virtual displacements denoted by `$\delta u_i$` and are arbitrary, but cannot violate the displacement boundary condition, thus `$\delta u_i = 0$` on `$S_u$`.

----
## virtual work 

-   Virtual work done by surface and body forces can be written as

`$$\delta W = \int_{S_t} t_i \delta u_i dS + \int_V F_i \delta u_i dV$$`

-   Since the virtual displacement is zero over `$S_u$`, we can replace `$S_t$` with `$S$` in the integral.

`$$\delta W = \int_{S} t_i \delta u_i dS + \int_V F_i \delta u_i dV$$`

----
## virtual work

`$$\begin{aligned}
	\delta W &= \int_{S} T_i^n \delta u_i dS + \int_V F_i \delta u_i dV\\
	&= \int_{S} \sigma_{ij}n_j \delta u_i dS + \int_V F_i \delta u_i dV\\
	&= \int_V (\sigma_{ij}\delta u_i)_{,j} dV + \int_V F_i \delta u_i dV\\
	&= \int_V (\sigma_{ij,j}\delta u_i + \sigma_{ij}\delta u_{i,j}) dV + \int_V F_i \delta u_i dV\\
	&= \int_V (-F_i\delta u_i + \sigma_{ij}(\delta \epsilon_{ij} + \delta\omega_{ij})) dV + \int_V F_i \delta u_i dV\\
	&= \int_V \sigma_{ij}\delta \epsilon_{ij} dV
\end{aligned}$$`

----
## virtual work

-   We can follow the procedure from the uniqueness derivation in reverse
-   Notice that this gives the usual strain energy relationship, but without the factor of one-half.
-   This is because stress is constant during virtual displacement

----
## virtual work

-   The virtual strain energy follows the same relationships developed previously, namely

`$$\int_V \delta U = \int_S t_i \delta u_i dS + \int_V F_i \delta u_i dV$$`

-   Because the external forces are unchanged during the virtual displacement, the `$\delta$` operator can be placed outside the integrals.
-   We can also move all terms to the same side of the equation to write

`$$\delta\left(\int_V U - \int_S t_i u_i dS - \int_V F_i u_i dV\right)$$`

----
## virtual work

-   Or, written in terms of virtual work

`$$\delta(U_T - W) = 0$$`

----
## virtual work

-   The total potential energy of an elastic solid is `$U_T-W$`, and must be zero for a virtual displacement
-   These results are completely general, and apply to both linear and non-linear materials
-   Special theories for rods, beams, plates, and shells use this principle
-   Finite elements is also developed using virtual work
-   We can even use virtual work to re-derive the continuum results we found previously

----
## virtual work

-   If we start with this form

`$$\int_V \sigma_{ij} \delta \epsilon_{ij} dV - \int_S t_i \delta u_i dS - \int_V F_i \delta u_i dV = 0$$`

-   We can replace the first term by writing it as

`$$\sigma_{ij} \delta \epsilon_{ij} = \sigma_{ij} \delta u_{i,j} = (\sigma_{ij} \delta u_i)_{,j} - \sigma_{ij,j} \delta u_i$$`

-   Which leads to

`$$\int_V [(\sigma_{ij}\delta u_i)_{,j} - \sigma_{ij,j}\delta u_i] dV - \int_S T_i^n \delta u_i dS - \int_V F_i \delta u_i dV = 0$$`

----
## virtual work

-   We can use the divergence theorem to say that

`$$\int_V (\sigma_{ij}\delta u_i)_{,j} dV = \int_S \sigma_{ij} n_j \delta u_i dS$$`

-   This gives

`$$\int_V [\sigma_{ij,j} + F_i]\delta u_i dV + \int_S (T_i^n - \sigma_{ij} n_j)\delta u_i dS = 0$$`

----
## virtual work

-   This will be satisfied if

`$$\sigma_{ij,j} + F_i = 0 \text{(equilibrium)}$$`

-   And either

`$$\delta u_i = 0 \text{(displacement boundary)}$$`

-   Or

`$$t_i = \sigma_{ij}n_j \text{(traction boundary)}$$`

---
# ritz method

----
## ritz method

-   While we have showed previously how virtual work can be used to develop analytic solutions, it is also convenient for approximate solutions
-   The Rayleigh-Ritz Method is an important approximation technique based on this method
-   In this method, trial functions are used as approximate solutions which satisfy the boundary conditions, but not necessarily the differential equations.

----
## ritz method

-   For the elasticity displacement formulation, trial functions take the form

`$$\begin{aligned}
	u &= u_0 + \sum_{j=1}^{N}a_ju_j\\
	v &= v_0 + \sum_{j=1}^{N}b_jv_j\\
	w &= w_0 + \sum_{j=1}^{N}c_jw_j\\
\end{aligned}$$`

----
## ritz method

-   Where the unknown constants are chosen to minimize the total potential energy.

`$$\begin{aligned}
	\frac{\partial \Pi}{\partial a_j} &= 0\\
	\frac{\partial \Pi}{\partial b_j} &= 0\\
	\frac{\partial \Pi}{\partial c_j} &= 0\\
\end{aligned}$$`

----
## example

![an end-loaded cantilever beam](../images/end-load-cantilever.png)

----
## example

-   We recall that the total potential energy is

`$$\Pi = U_T - W$$`

-   In a simple (Euler-Bernoulli) beam, we assume that the stress is a function of the vertical displacement, *w* and the cross-sectional area
-   All stress terms other than `$\sigma_{11}$` are zero

----
## example

-   The strain energy density is

`$$U = \frac{\sigma_{11}^2}{2E} = \frac{M^2 y^2}{2EI^2} = \frac{E}{2}\left(\frac{d^2 w}{dx^2}\right)^2 y^2$$`

-   We integrate over the volume to find the total strain energy in the beam

`$$\begin{aligned}
	U_T &= \int_0^L \left[\iint_A \frac{E}{2}\left(\frac{d^2 w}{dx^2}\right)^2 y^2 dA \right] dx\\
	&= \int_0^L \frac{EI}{2}\left(\frac{d^2 w}{dx^2}\right)^2 dx
\end{aligned}$$`

----
## example

-   The work done by external forces is quite simple in this case

`$$W = Pw(L)$$`

-   We now consider a trial function for *w*, let us consider a polynomial function

`$$w = a_0 + a_1 \left(\frac{x}{L}\right) + a_2 \left(\frac{x}{L}\right)^2$$`

----
## example

-   We first ensure the trial solution satisfies the essential boundary conditions

`$$\begin{aligned}
	w(0) &= 0\\
	0 &= a_0 + a_1 \left(\frac{0}{L}\right) + a_2 \left(\frac{0}{L}\right)^2
\end{aligned}$$`

----
## example

-   And

`$$\begin{aligned}
	\frac{d w(0)}{dx} &= 0\\
	0 &= a_1 \left(\frac{1}{L}\right) + 2 a_2 \left(\frac{0}{L}\right)
\end{aligned}$$`

----
## example

-   This gives `$a_0 = a_1 = 0$`
-   `$a_2$` is to be determined
-   The total potential energy is

`$$\Pi = U_t - W = \int_0^L \frac{EI}{2}\left(\frac{d^2 w}{dx^2}\right)^2 dx - Pw(L)$$`

-   After differentiation and substitution, we find

`$$\Pi = \frac{EI}{2} \int_0^L \left(\frac{2a_2}{L^2}\right)^2 dx - Pa_2$$`

----
## example

-   We minimize the potential energy by letting `$\frac{\partial \Pi}{\partial a_j} = 0$`

`$$\begin{aligned}
	\Pi &= \frac{2EI a_2^2}{L^3} - Pa_2\\
	\frac{\partial \Pi}{\partial a_2} &= \frac{4EIa_2}{L^3} - P = 0\\
	a_2 &= \frac{PL^3}{4EI}
\end{aligned}$$`

----
## example

-   Thus our approximate solution is

`$$w = \frac{PL}{4EI}x^2$$`

----
## example

-   A simple cantilever beam of this form can be solved for exactly
-   The exact solution is

`$$w = \frac{Px^2}{6EI}(3L-x)$$`

----
## example

![comparison of ritz displacement solution to exact solution](../images/ritz1.png)

----
## example

-   If we considered one more term in our trial, we would have recovered the exact solution
-   In this case, more terms would be redundant
-   We could have also considered a trigonometric function
-   A worked example with more terms considered is [here](https://mybinder.org/v2/gh/ndaman/live-examples/master?filepath=example/ritz.ipynb)
