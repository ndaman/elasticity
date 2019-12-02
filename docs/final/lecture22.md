# AE731
## Theory of Elasticity
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering<br/>
December 4, 2019

----
## upcoming schedule

-   Dec 4 - Final Review, Homework 8 Due
-   Dec 11 - 3:00 - 4:50 Final Exam

----
## outline

<!-- vim-markdown-toc GFM -->

* exam
* chapter 1
* chapter 2
* chapter 3
* chapter 4
* chapter 5
* chapter 6

<!-- vim-markdown-toc -->

---
# exam

----
## exam

-   5 questions
-   Similar to homework problems (no T/F or multiple choice)
-   One question from Exam 1 material (Ch’s 1-2)
-   One question from Exam 2 material (Ch’s 3-5)

----
## exam

-   Three questions from Ch’s 6-8
    -   Expect one question from chapter 6
    -   One problem with a given Airy stress function
    -   One problem where I ask you to find the Airy stress function
    -   Showing something can solve and solving are not the same, pay attention to directions

----
## chapter 1 topics

-   Index notation
-   Solving tensor equations
-   Coordinate transformation
-   Principal values
-   Principal directions
-   Tensor calculus

----
## chapter 2 topics

-   Deformations 
-   Deformation gradient
-   Strain and rotation
-   Strain transformation
-   Principal strains

----
## chapter 3 topics

-   Traction
-   Stress transformation
-   Principal stress
-   Equilibrium

----
## chapter 4 topics

-   Hooke’s Law
-   Physical meaning of elastic constants
-   Thermal expansion

----
## chapter 5 topics

-   Boundary conditions
-   Compatibility
-   Beltrami-Michell
-   Navier’s Equations
-   Superposition

----
## chapter 6 topics

-   Strain Energy
-   Uniqueness
-   Bounds on elastic constants
-   Virtual work
-   Ritz method

---
# chapter 1

----
## converting to matrix math

-   It is often convenient to write expressions in matrix notation to use MATLAB or graphing calculators
-   We need to be careful how this is done, in index notation left and right multiplication are identical, but this is not the case for matrices
- <!-- .element style="list-style-type:none" -->    
\[*A*\]\[*B*\]=*A*<sub>*ij*</sub>*B*<sub>*jk*</sub>
- <!-- .element style="list-style-type:none" -->    
\[*B*\]\[*A*\]=*B*<sub>*ij*</sub>*A*<sub>*jk*</sub> = *A*<sub>*jk*</sub>*B*<sub>*ij*</sub>

----
## converting to matrix math

-   Some useful relations

$$\\begin{aligned}
	\[A\]\[A\]\[B\] & = A\_{ij} B\_{jk}\\\\
	\[A\]\[B\]^T & = A\_{ij} B\_{kj}\\\\
	\[A\]^T\[B\] & = A\_{ji} B\_{jk}\\\\
	tr(\[A\]\[B\]) & = A\_{ij} B\_{ji}\\\\
	tr(\[A\]\[B\]^T) & = A\_{ij} B\_{ij}
\\end{aligned}$$

----
## converting to matrix

-   Sometimes our expression is more complex (involves more terms)
-   e.g. transformation of a matrix
    *a*<sub>*ij*</sub><sup>′</sup> = *Q*<sub>*ip*</sub>*Q*<sub>*jq*</sub>*a*<sub>*pq*</sub>
    1.  Re-arrange so dummy indexes are adjacent
        *Q*<sub>*ip*</sub>*a*<sub>*pq*</sub>*Q*<sub>*jq*</sub>
    2.  Identify which (if any) tensors are transposed (dummy indexes should be on the inside of adjacent terms without a transpose)
- <!-- .element style="list-style-type:none" -->        
_Q_<sub>*ip*</sub> *a* <sub>*pq*</sub> <span style="color:red">Q <sub>*jq*</sub></span>
- <!-- .element style="list-style-type:none" -->        
\[*Q*\]\[*a*\]\[*Q*\]<sup>*T*</sup>

----
## example

-   Convert the expression in index notation to Matrix notation
    *A*<sub>*ik*</sub>*B*<sub>*jl*</sub>*C*<sub>*ml*</sub>*D*<sub>*mk*</sub>

  1.  <!-- .element class="fragment" -->Re-arrange to so that dummy indexes are in adjacent terms
		-   <!-- .element style="list-style-type:none" class="fragment" -->        
_A_<sub>*ik*</sub>*D*<sub>*mk*</sub>*C*<sub>*ml*</sub>*B*<sub>*jl*</sub>

  2.  <!-- .element class="fragment" -->Identify which terms are transposed
		- <!-- .element style="list-style-type:none" class="fragment" --> 
_A_<sub>*ik*</sub> <span style="color:red">*D*<sub>*mk*</sub></span>*C* <sub>*ml*</sub> <span style="color:red">*B*<sub>*jl*</sub></span>
		- <!-- .element style="list-style-type:none" class="fragment" --> 
\[*A*\]\[*D*\]<sup>*T*</sup>\[*C*\]\[*B*\]<sup>*T*</sup>

----
## principal values

-   In the 2D coordinate transformation example, we were able to eliminate one value from a vector using coordinate transformation
-   For second-order tensors, we desire to find the “principal values” where all non-diagonal terms are zero
-   The direction determined by the unit vector, *n*<sub>*j*</sub>, is said to be the *principal direction* or *eigenvector* of the symmetric second-order tensor, *a*<sub>*ij*</sub> if there exists a parameter, *λ*, such that

_a_<sub>*ij*</sub>*n*<sub>*j*</sub> = *λn*<sub>*i*</sub>

-   Where *λ* is called the *principal value* or *eigenvalue* of the tensor

----
## principal values

-   We can re-write the equation

(*a*<sub>*ij*</sub> − *λδ*<sub>*ij*</sub>)*n*<sub>*j*</sub> = 0

-   This system of equations has a non-trivial solution if and only if det\[*a*<sub>*ij*</sub> − *λδ*<sub>*ij*</sub>\]=0
-   This equation is known as the characteristic equation, and we solve it to find the principal values of a tensor

----
## principal directions

-   Find principal directions of:

$$e\_{ij} = \\begin{bmatrix}
	2 & -1 & 0\\\\
	-1 & -3 & 1\\\\
	0 & 1 & 6
\\end{bmatrix}$$

-   Principal values are 6.113, 2.184, -3.296
-   Start by substituting value for *e*<sub>*ij*</sub> − *λδ*<sub>*ij*</sub>

$$\\begin{bmatrix}
	-4.113 & -1 & 0\\\\
	-1 & -9.113 & 1\\\\
	0 & 1 & -0.113
\\end{bmatrix} \\begin{Bmatrix}
	n\_1 \\\\ n\_2 \\\\n\_3
\\end{Bmatrix} = \\begin{Bmatrix}
	0 \\\\ 0 \\\\ 0
\\end{Bmatrix}$$

----
## principal directions

-   In this problem row-reduction is not absolutely necessary (we could just substitute a value for *n*<sub>1</sub>, *n*<sub>2</sub>, or *n*<sub>3</sub> and solve for the others)
-   To row-reduce, we want to eliminate variables from an equation
-   We can eliminate *n*<sub>2</sub> from row 2 by adding 9.113 row 3 to row 2

$$\\begin{aligned}
	(2) &= \\begin{bmatrix}
	-1 & -9.113 & 1
\\end{bmatrix}\\\\
	9.113 (3) &= \\begin{bmatrix}
	0 &9.113 &-1.030
\\end{bmatrix}\\\\
	(2)\_{new} &= \\begin{bmatrix}
	-1 & 0 & -0.030
\\end{bmatrix}
\\end{aligned}$$

----
## principal directions

-   This gives

$$\\begin{bmatrix}
	-4.113 & -1 & 0\\\\
	-1 & 0 & -0.030\\\\
	0 & 1 & -0.113
\\end{bmatrix} \\begin{Bmatrix}
	n\_1 \\\\ n\_2 \\\\n\_3
\\end{Bmatrix} = \\begin{Bmatrix}
	0 \\\\ 0 \\\\ 0
\\end{Bmatrix}$$

-   We can easily eliminate *n*<sub>2</sub> from (1) by adding (3) to (1)

$$\\begin{aligned}
	(1) &= \\begin{bmatrix}
	-4.113 & -1 & 0
\\end{bmatrix}\\\\
	(3) &= \\begin{bmatrix}
	0 & 1 & -0.113
\\end{bmatrix}\\\\
	(1)\_{new} &= \\begin{bmatrix}
	-4.113 & 0 & -0.113
\\end{bmatrix}
\\end{aligned}$$

----
## principal directions

-   This gives

$$\\begin{bmatrix}
	-4.113 & 0 & -0.113\\\\
	-1 & 0 & -0.030\\\\
	0 & 1 & -0.113
\\end{bmatrix} \\begin{Bmatrix}
	n\_1 \\\\ n\_2 \\\\n\_3
\\end{Bmatrix} = \\begin{Bmatrix}
	0 \\\\ 0 \\\\ 0
\\end{Bmatrix}$$

----
## principal directions

-   We can now eliminate *n*<sub>1</sub> from (1) by multiplying (2) by -4.113 and adding

$$\\begin{aligned}
	(1) &= \\begin{bmatrix}
	-4.113 & 0 & -0.113
\\end{bmatrix}\\\\
	-4.113(2) &= \\begin{bmatrix}
	4.113 & 0 & 0.122
\\end{bmatrix}\\\\
	(1)\_{new} &= \\begin{bmatrix}
	0 & 0 & 0.009
\\end{bmatrix}
\\end{aligned}$$

----
## principal directions

-   We are left with

$$\\begin{bmatrix}
	0 & 0 & 0.009\\\\
	-1 & 0 & -0.030\\\\
	0 & 1 & -0.113
\\end{bmatrix} \\begin{Bmatrix}
	n\_1 \\\\ n\_2 \\\\n\_3
\\end{Bmatrix} = \\begin{Bmatrix}
	0 \\\\ 0 \\\\ 0
\\end{Bmatrix}$$

----
## principal directions

-   We know in these types of problems we should eliminate one equation entirely
-   0.009 ≈ 0, so we have eliminated (1)
-   If we let *n*<sub>3</sub> = 1, we find *n*<sub>2</sub> = 0.113 and *n*<sub>1</sub> = −0.03
-   To normalize, we find the magnitude: $\\sqrt{1^2 + 0.113^2 + .03^2} = 1.007$

_n_<sup>1</sup> = ⟨ − 0.030, 0.112, 0.993⟩

----
## partial derivatives

-   We usually omit the (*x*<sub>*i*</sub>), but most variables we deal with are functions of *x*<sub>*i*</sub>
-   These are referred to as field variables. e.g.

$$\\begin{aligned}{2}
	a &= a(x\_1, x\_2, x\_3) & &= a(x\_i) \\\\
	a\_i &= a\_i(x\_1, x\_2, x\_3) & &= a\_i(x\_i) \\\\
	a\_{ij} &= a\_{ij}(x\_1, x\_2, x\_3) & &= a\_{ij}(x\_i) 
\\end{aligned}$$

----
## partial derivatives

-   We can use comma notation to simplify taking partial derivatives of field variables

$$\\begin{aligned}
	a\_{,i} &= \\frac{\\partial}{\\partial x\_i} a \\\\
	a\_{i,j} &= \\frac{\\partial}{\\partial x\_j} a\_i \\\\
	a\_{ij,k} &= \\frac{\\partial}{\\partial x\_k} a\_{ij} \\\\
\\end{aligned}$$

---
# chapter 2

----
## deformation

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


----
## displacement

-   Displacement is the shortest distance traveled when a particle moves from one location to another
-   It is identical in Eulerian and Lagrangian descriptions

$$\\begin{aligned}
	u\_i &= (x\_i - x\_i^0)\\\\
\\begin{Bmatrix}
	u \\\\ v \\\\ w
\\end{Bmatrix} &= \\begin{Bmatrix}
	x - x^0\\\\
	y - y^0\\\\
	z - z^0
\\end{Bmatrix}
\\end{aligned}$$

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
## strain definition

-   We can separate the deformation gradient into symmetric and antisymmetric parts

_u_<sub>*i*, *j*</sub> = *e*<sub>*ij*</sub> + *ω*<sub>*ij*</sub>

-   Where

$$\\begin{aligned}
    e\_{ij} &= \\frac{1}{2}(u\_{i,j} + u\_{j,i})\\\\
    \\omega\_{ij} &= \\frac{1}{2}(u\_{i,j} - u\_{j,i})
\\end{aligned}$$

-   *e*<sub>*ij*</sub> is known as the strain tensor
-   *ω*<sub>*ij*</sub> is known as the rotation tensor

----
## strain transformation

-   The usual tensor transformation applies to the strain tensor as well

_e_<sub>*ij*</sub><sup>′</sup> = *Q*<sub>*im*</sub>*Q*<sub>*jn*</sub>*e*<sub>*mn*</sub>

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

----
## strain transformation

-   If we multiply this out, for the in-plane strain terms (*e*<sub>*x*</sub><sup>′</sup>, *e*<sub>*x*</sub><sup>′</sup>, and *e*<sub>*xy*</sub><sup>′</sup>) we find

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

----
## strain transformation

-   Many times it is easy to measure the axial strain directly with strain gages, but the shear strain cannot be easily measured
-   We can use an extra, off-axis strain gage, together with the strain transformation equations, to calculate the shear strain
-   Many companies already do this with “rosettes” which have strain gages at specified angles built-in

----
## example


----
## example

-   Given that *ϵ*<sub>*a*</sub> = 0.005, *ϵ*<sub>*b*</sub> = −0.002 and *ϵ*<sub>*c*</sub> = 0.003, find *e*<sub>*x*</sub>, *e*<sub>*y*</sub>, and *e*<sub>*xy*</sub>.
-   Note that *e*<sub>*y*</sub> = *ϵ*<sub>*b*</sub> = −0.002
-   Set coordinate system so that *ϵ*<sub>*b*</sub> = *e*<sub>*x*</sub><sup>′</sup>.
-   Use equation for *e*<sub>*x*</sub><sup>′</sup> with *θ* = 30.

$$\\alert{e^\\prime\_x} = \\frac{e\_x + \\alert{e\_y}}{2} + \\frac{e\_x - \\alert{e\_y}}{2}\\cos 60 + e\_{xy} \\sin 60$$

----
## example

-   We have two unknowns in this equation, so we need another
-   We can use the equation for *e*<sub>*y*</sub><sup>′</sup> with *θ* = 60 so that *ϵ*<sub>*b*</sub> = *e*<sub>*x*</sub><sup>′</sup>

$$\\alert{e^\\prime\_y} = \\frac{e\_x + \\alert{e\_y}}{2} - \\frac{e\_x - \\alert{e\_y}}{2}\\cos 120 - e\_{xy} \\sin 120$$

-   Substituting known values and simplifying:

$$\\begin{aligned}
	0.01 + 0.002 - 0.002 \\cos 60 &= e\_x (1+\\cos 60) + e\_{xy} \\sin 60 \\\\
	0.006 + 0.002 + 0.002 \\cos 120 &= e\_x (1-\\cos 120) - e\_{xy} \\sin 120 
\\end{aligned}$$

-   And solving we find *e*<sub>*x*</sub> = 0.006, *e*<sub>*y*</sub> = −0.002, and *e*<sub>*xy*</sub> = 0.00231.

---
# chapter 3

----
## derivations

-   Cauchy’s stress theorem
-   Max shear stress for plane stress
-   Mohr’s circle

----
## stress tensor

<div class="left">

-   To simplify the notation, we introduce the stress tensor

$$\\sigma\_{ij} = t\_j^{(\\hat{e}\_i)}$$

</div>

<div class="right">
	
![stress tensor illustrated on a cube](../images/stress-cube.png)

</div>

----
## traction

<div class="left">
	
-   We can find some interesting information about the traction vector by considering an arbitrary tetrahedron with some traction $\\hat{t}^{(n)}$ applied to the surface

</div>

<div class="right">
	
![An arbitrary tetrahedron with some traction applied on the surface](../images/traction-equilibrium.png)

</div>

----
## traction

-   If we consider the balance of forces in the *x*<sub>1</sub>-direction

_t_<sub>1</sub>*dA* − *σ*<sub>11</sub>*dA*<sub>1</sub> − *σ*<sub>21</sub>*dA*<sub>2</sub> − *σ*<sub>31</sub>*dA*<sub>3</sub> + *b*<sub>1</sub>*ρdV* = 0

-   The area components are:

$$\\begin{aligned}
	dA\_1 &= n\_1 dA\\\\
	dA\_2 &= n\_2 dA\\\\
	dA\_3 &= n\_3 dA\\\\
\\end{aligned}$$

-   And $dV = \\frac{1}{3}h dA$.

----
## traction

$$t\_1 dA - \\sigma\_{11} n\_1 dA - \\sigma\_{21} n\_2 dA - \\sigma\_{31} n\_3 dA + b\_1 \\rho \\frac{1}{3}h dA = 0$$

-   If we let *h* → 0 and divide by *dA*

_t_<sub>1</sub> = *σ*<sub>11</sub>*n*<sub>1</sub> + *σ*<sub>21</sub>*n*<sub>2</sub> + *σ*<sub>31</sub>*n*<sub>3</sub>

-   We can write this in index notation as

_t_<sub>1</sub> = *σ*<sub>*i*1</sub>*n*<sub>*i*</sub>

----
## traction

-   We find, similarly

$$\\begin{aligned}
	t\_2 &= \\sigma\_{i2} n\_i\\\\
	t\_3 &= \\sigma\_{i3} n\_i\\\\
\\end{aligned}$$

----
## traction

-   We can further combine these results in index notation as

_t_<sub>*j*</sub> = *σ*<sub>*ij*</sub>*n*<sub>*i*</sub>

-   This means with knowledge of the nine components of *σ*<sub>*ij*</sub>, we can find the traction vector at any point on any surface

----
## maximum shear stress

-   For plane stress problems, we can also use the stress transformation equations to find the maximum shear stress
-   We desire to maximize this equation:

$$\\tau^\\prime\_{xy} = \\frac{\\sigma\_y - \\sigma\_x}{2}\\sin 2\\theta + \\tau\_{xy} \\cos 2\\theta$$

----
## maximum shear stress

-   Taking the derivative with respect to *θ* gives

$$\\frac{\\partial}{\\partial \\theta} (\\tau^\\prime\_{xy}) = (\\sigma\_y-\\sigma\_x)\\cos 2\\theta - 2\\tau\_{xy} \\sin 2\\theta = 0$$

-   Which we can use to find 2*θ*

$$2\\theta = \\tan ^{-1} \\left(\\frac{(\\sigma\_y-\\sigma\_x)}{2\\tau\_{xy}}\\right)$$

----
## maximum shear stress

-   Substituting back into the original equation gives

$$\\tau^\\prime\_{max} = \\frac{\\sigma\_y - \\sigma\_x}{2}\\sin \\left\[\\tan ^{-1} \\left(\\frac{(\\sigma\_y-\\sigma\_x)}{2\\tau\_{xy}}\\right)\\right\] + \\tau\_{xy} \\cos \\left\[\\tan ^{-1} \\left(\\frac{(\\sigma\_y-\\sigma\_x)}{2\\tau\_{xy}}\\right)\\right\]$$

-   Note that

$$\\begin{aligned}
	\\sin (\\tan ^{-1} (x)) &= \\frac{x}{\\sqrt{1+x^2}}\\\\
	\\cos (\\tan ^{-1} (x)) &= \\frac{1}{\\sqrt{1+x^2}}\\\\
\\end{aligned}$$

----
## maximum shear stress

-   We note that

$$\\sqrt{1+ \\left(\\frac{\\sigma\_y - \\sigma\_x}{2 \\tau\_{xy}}\\right)^2} = \\frac{\\sqrt{(\\sigma\_y-\\sigma\_x)^2+4\\tau\_{xy}^2}}{2\\tau\_{xy}}$$

-   And thus we find

$$\\tau\_{max} = \\frac{(\\sigma\_y-\\sigma\_x)^2}{2 \\sqrt{(\\sigma\_y-\\sigma\_x)^2+4\\tau\_{xy}^2}} + \\frac{4\\tau\_{xy}^2}{2 \\sqrt{(\\sigma\_y-\\sigma\_x)^2+4\\tau\_{xy}^2}}$$

----
## maximum shear stress

-   Adding the terms and simplifying, we find

$$\\tau\_{max} = \\sqrt{\\left(\\frac{\\sigma\_y-\\sigma\_x}{2}\\right)^2+\\tau\_{xy}^2}$$

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

$$N = \\hat{T}^n \\cdot \\hat{n}$$

-   The shear component can be found using the Pythagorean theorem

$$S^2 = |\\hat{T}^n|^2 - N^2$$

----
## tractions

-   We now use the stress tensor in the principal direction to simplify the calculations

$$\\begin{aligned}
	N &= \\hat{T}^n \\cdot \\hat{n}\\\\
	&= T^n\_i n\_i \\\\
	&= \\sigma\_{ji} n\_j n\_i\\\\
	&= \\sigma\_1 n\_1^2 + \\sigma\_2 n\_2^2 + \\sigma\_3 n\_3^2
\\end{aligned}$$

----
## tractions

-   We also know that

$$\\begin{aligned}
	|\\hat{T}^n|^2 &= \\hat{T}^n \\cdot \\hat{T}^n\\\\
	&= T\_i^n T\_i^n \\\\
	&= \\sigma\_{ji} n\_j \\sigma\_{ki} n\_k\\\\
	&= \\sigma\_1^2 n\_1^2 + \\sigma\_2^2 n\_2^2 + \\sigma\_3^2 n\_3^2
\\end{aligned}$$

----
## mohr’s circle

-   If we constrain the normal vector to be a unit vector we can formulate the following inequalities

$$\\begin{aligned}
	S^2 + (N-\\sigma\_2)(N-\\sigma\_3) &\\ge 0\\\\
	S^2 + (N-\\sigma\_3)(N-\\sigma\_1) &\\le 0\\\\
	S^2 + (N-\\sigma\_1)(N-\\sigma\_2) &\\ge 0\\\\
\\end{aligned}$$

-   These inequalities form what is known as Mohr’s circle

----
## mohr’s circle

![mohr's circle](../images/mohr.PNG) <!-- .element width="60%" -->

---
# chapter 4

----
## hooke’s law

-   Can be written in terms of strain

$$\\epsilon\_{ij} = \\frac{1+\\nu}{E}\\sigma\_{ij} - \\frac{\\nu}{E}\\sigma\_{kk} \\delta\_{ij}$$

-   Or stress

_σ_<sub>*ij*</sub> = *λϵ*<sub>*kk*</sub>*δ*<sub>*ij*</sub> + 2*μϵ*<sub>*ij*</sub>

----
## isotropic materials

| | *λ*= | *μ* = *G*= | *E*= | *ν*= | *K*= |
|-:|---:|----------:|-------:|-----:|-----:|
|  *λ*, *μ*|                                     |                                  |  $\\frac{\\mu(3\\lambda + 2\\mu)}{\\lambda + \\mu}$|  $\\frac{\\lambda}{2(\\lambda + \\mu)}$|  $\\frac{3\\lambda + 2\\mu}{3}$|
|  *G*, *E*|              $\\frac{G(2G-E)}{E-3G}$|                                  |                                                    |                      $\\frac{E-2G}{2G}$|            $\\frac{GE}{3(3G-E}$|
|  *G*, *ν*|            $\\frac{2G\\nu}{1-2\\nu}$|                                  |                                       2*G*(1 + *G*)|                                        |       $\\frac{2G(1+G)}{3(1-2G}$|
|  *E*, *ν*|  $\\frac{\\nu E}{(1+\\nu)(1-2\\nu)}$|            $\\frac{E}{2(1+\\nu)}$|                                                    |                                        |          $\\frac{E}{3(1-2\\nu}$|
|  *K*, *E*|             $\\frac{3K(3K-E)}{9K-E}$|               $\\frac{3EK}{9K-E}$|                                                    |                      $\\frac{3K-E}{6K}$|                                |
|  *ν*, *K*|             $\\frac{3K\\nu}{1+\\nu}$|  $\\frac{3K(1-2\\nu)}{2(1+\\nu)}$|                                      3*K*(1 − 2*ν*)|                                        |                                |

----
## physical meaning

-   Young’s modulus
-   Poisson’s ratio
-   Shear modulus
-   Bulk modulus

----
## thermoelasticity

-   Separate strain into mechanical and thermal components

_ϵ_<sub>*ij*</sub> = *ϵ*<sub>*ij*</sub><sup>(*M*)</sup> + *ϵ*<sub>*ij*</sub><sup>(*T*)</sup>

-   For isotropic materials:

_ϵ_<sub>*ij*</sub><sup>(*T*)</sup> = *α*(*T* − *T*<sub>0</sub>)*δ*<sub>*ij*</sub>

----
## thermoelasticity

-   We can combine this with Hooke’s Law to find

$$\\epsilon\_{ij} = \\frac{1+\\nu}{E}\\sigma\_{ij} -\\frac{\\nu}{E}\\sigma\_{kk}\\delta\_{ij} + \\alpha (T-T\_0)\\delta\_{ij}$$

-   Or formulated in terms of stress (and Lamé constants)

_σ_<sub>*ij*</sub> = *λϵ*<sub>*kk*</sub>*δ*<sub>*ij*</sub> + 2*μϵ*<sub>*ij*</sub> − (3*λ* + 2*μ*)*α*(*T* − *T*<sub>0</sub>)*δ*<sub>*ij*</sub>

---
# chapter 5

----
## boundary conditions

-   Traction
-   Displacement
-   Mixed

----
## compatibility equations

-   If continuous, single-valued displacements are specified, differentiation will result in well-behaved strain field
-   The inverse relationship, integration of a strain field to find displacement, may not always be true
-   There are cases where we can integrate a strain field to find a set of discontinuous displacements

----
## compatibility equations

-   The compatibility equations enforce continuity of displacements to prevent this from occurring
-   To enforce this condition we consider the strain-displacement relations:

$$\\epsilon\_{ij} = \\frac{1}{2}(u\_{i,j} + u\_{j,i})$$

-   and differentiate with respect to *x*<sub>*k*</sub> and *x*<sub>*l*</sub>

$$\\epsilon\_{ij,kl} = \\frac{1}{2}(u\_{i,jkl} + u\_{j,ikl})$$

-   Or

2*ϵ*<sub>*ij*, *kl*</sub> = *u*<sub>*i*, *jkl*</sub> + *u*<sub>*j*, *ikl*</sub>

----
## compatibility equations

-   We can eliminate the displacement terms from the equation by interchanging the indexes to generate new equations

$$\\begin{aligned}
	2\\epsilon\_{ik,jl} &= u\_{i,jkl} + u\_{k,ijl} \\\\
	2\\epsilon\_{jl,ik} &= u\_{j,ikl} + u\_{l,ijk}
\\end{aligned}$$

-   Solving for *u*<sub>*i*, *jkl*</sub> and *u*<sub>*j*, *ikl*</sub>

$$\\begin{aligned}
	u\_{i,jkl} &= 2\\epsilon\_{ik,jl} - u\_{k,ijl} \\\\
	u\_{j,ikl} &= 2\\epsilon\_{jl,ik} - u\_{l,ijk}
\\end{aligned}$$

----
## compatibility equations

-   Substituting these values into the equations gives

2*ϵ*<sub>*ij*, *kl*</sub> = 2*ϵ*<sub>*ik*, *jl*</sub> − *u*<sub>*k*, *ijl*</sub> + 2*ϵ*<sub>*jl*, *ik*</sub> − *u*<sub>*l*, *ijk*</sub>

-   We now consider one more change of index equation

2*ϵ*<sub>*kl*, *ij*</sub> = *u*<sub>*k*, *ijl*</sub> + *u*<sub>*l*, *ijk*</sub>

-   and substituting this result gives

2*ϵ*<sub>*ij*, *kl*</sub> = 2*ϵ*<sub>*ik*, *jl*</sub> + 2*ϵ*<sub>*jl*, *ik*</sub> − 2*ϵ*<sub>*kl*, *ij*</sub>

-   Or, simplified

*ϵ*<sub>*ij*, *kl*</sub> + *ϵ*<sub>*kl*, *ij*</sub> − *ϵ*<sub>*ik*, *jl*</sub> − *ϵ*<sub>*jl*, *ik*</sub> = 0

----
## beltrami-michell

-   When working with stress functions, it is convenient to check compatibility of the stress function directly
-   Using Hooke’s Law, we can formulate compatibility in terms of stress
-   These are known as the Beltrami-Michell equations

----
## navier’s equations

-   Similarly, we can write the equilibrium equations in terms of displacement
-   This is convenient when dealing with displacement boundary conditions
-   Known as Navier’s equations

---
# chapter 6

----
## uniqueness

-   In Chapter 5 we never proved if any solution was unique
-   Let us assume that there exist two solutions to a given boundary value problem
-   The difference of the two solutions is given as

$$\\begin{aligned}
	\\sigma\_{ij} &= \\sigma\_{ij}^{(1)} - \\sigma\_{ij}^{(2)}\\\\
	\\epsilon\_{ij} &= \\epsilon\_{ij}^{(1)} - \\epsilon\_{ij}^{(2)}\\\\
	u\_i &= u\_i^{(1)} - u\_i^{(2)}
\\end{aligned}$$

----
## uniqueness

-   Because both solutions will have the same body force, the difference solution must satisfy the equilibrium equation

_σ_<sub>*ij*, *j*</sub> = 0

-   We also know that the difference must give

_T_<sub>*i*</sub><sup>*n*</sup> = *σ*<sub>*ij*</sub>*n*<sub>*j*</sub> = 0

On the traction boundary and

_u_<sub>*i*</sub> = 0

On the displacement boundary

----
## uniqueness

-   Using the definition of strain energy, we can write

$$\\begin{aligned}
	2 \\int\_V U dV &= \\int\_V \\sigma\_{ij} \\epsilon\_{ij} dV = \\int\_V \\sigma\_{ij}(u\_{i,j}-\\omega\_{ij}) dV\\\\
	&= \\int\_V \\sigma\_{ij}u\_{i,j} = \\int\_V (\\sigma\_{ij}u\_i)\_{,j} dV - \\int\_V \\sigma\_{ij,j}u\_i dV\\\\
	&= \\int\_S \\sigma\_{ij}n\_j u\_i dS - \\int\_V \\sigma\_{ij,j}u\_i dV
\\end{aligned}$$

----
## uniqueness

-   Note that a symmetric matrix times an antisymmetric matrix =0
-   We know that *σ*<sub>*ij*</sub>*n*<sub>*j*</sub> = 0 on surfaces where tractions are defined and that *u*<sub>*i*</sub> = 0 on the other surfaces, so the first integral goes to zero
-   We also know by equilibrium that *σ*<sub>*ij*, *j*</sub> = 0, so the second integral will also be 0

----
## uniqueness

-   If the strain energy of the difference between two solutions is zero, then we know that
	-   The stress field of the difference is zero
	-   The strain field of the difference is zero
	-   The displacement field of the difference is zero

-   Therefore the two solutions are the same solution, and the solution is unique

----
## uniaxial tension

-   We can establish bounds on physical constants by recalling that the strain energy must always be positive and considering certain states of stress

-   Uniaxial tension gives the stress state

$$\\sigma\_{ij} = \\begin{bmatrix}
	\\sigma & 0 & 0 \\\\
	0 & 0 & 0\\\\
	0 & 0 & 0
\\end{bmatrix}$$

-   Find the strain energy and use it to place bounds on the modulus of Elasticity, *E*

----
## simple shear

-   If we consider uniform simple shear

$$\\sigma\_{ij} = \\begin{bmatrix}
	0 & \\tau & 0 \\\\
	\\tau & 0 & 0\\\\
	0 & 0 & 0
\\end{bmatrix}$$

-   Find the strain energy and use it to place bounds on Poisson’s Ratio

----
## hydrostatic pressure

-   We can also consider hydrostatic pressure

$$\\sigma\_{ij} = \\begin{bmatrix}
	-p & 0 & 0 \\\\
	0 & -p & 0\\\\
	0 & 0 & -p
\\end{bmatrix}$$

-   Find the strain energy and use it to place bounds on the hydrostatic pressure

----
## virtual work

-   The solution format we developed in Chapter 5 is known as *Strong Form*, and is not always a convenient solution form
-   We can use energy and work principles to develop additional solution methods
-   *Virtual Displacement* is a fictitious displacement such that the forces acting on the point remain unchanged
-   The work done by these forces is known as *Virtual Work*

----
## virtual work

-   If we consider the elastic boundary-value problem, with tractions applied over the boundary *S*<sub>*t*</sub> and displacements applied over the boundary *S*<sub>*u*</sub>.
-   Virtual displacements denoted by *δu*<sub>*i*</sub> and are arbitrary, but cannot violate the displacement boundary condition, thus *δu*<sub>*i*</sub> = 0 on *S*<sub>*u*</sub>.

----
## virtual work 

-   Virtual work done by surface and body forces can be written as

_δW_ = ∫<sub>*S*<sub>*t*</sub></sub>*T*<sub>*i*</sub><sup>*n*</sup>*δu*<sub>*i*</sub>*dS* + ∫<sub>*V*</sub>*F*<sub>*i*</sub>*δu*<sub>*i*</sub>*dV*

-   Since the virtual displacement is zero over *S*<sub>*u*</sub>, we can replace *S*<sub>*t*</sub> with *S* in the integral.

_δW_ = ∫<sub>*S*</sub>*T*<sub>*i*</sub><sup>*n*</sup>*δu*<sub>*i*</sub>*dS* + ∫<sub>*V*</sub>*F*<sub>*i*</sub>*δu*<sub>*i*</sub>*dV*

----
## virtual work

$$\\begin{aligned}
	\\delta W &= \\int\_{S} T\_i^n \\delta u\_i dS + \\int\_V F\_i \\delta u\_i dV\\\\
	&= \\int\_{S} \\sigma\_{ij}n\_j \\delta u\_i dS + \\int\_V F\_i \\delta u\_i dV\\\\
	&= \\int\_V (\\sigma\_{ij}\\delta u\_i)\_{,j} dV + \\int\_V F\_i \\delta u\_i dV\\\\
	&= \\int\_V (\\sigma\_{ij,j}\\delta u\_i + \\sigma\_{ij}\\delta u\_{i,j}) dV + \\int\_V F\_i \\delta u\_i dV\\\\
	&= \\int\_V (-F\_i\\delta u\_i + \\sigma\_{ij}(\\delta \\epsilon\_{ij} + \\delta\\omega\_{ij})) dV + \\int\_V F\_i \\delta u\_i dV\\\\
	&= \\int\_V \\sigma\_{ij}\\delta \\epsilon\_{ij} dV
\\end{aligned}$$

----
## virtual work

-   We can follow the procedure from the uniqueness derivation in reverse
-   Notice that this gives the usual strain energy relationship, but without the factor of one-half.
-   This is because stress is constant during virtual displacement

----
## virtual work

-   The virtual strain energy follows the same relationships developed previously, namely

∫<sub>*V*</sub>*δU* = ∫<sub>*S*</sub>*T*<sub>*i*</sub><sup>*n*</sup>*δu*<sub>*i*</sub> + ∫<sub>*V*</sub>*F*<sub>*i*</sub>*δu*<sub>*i*</sub>*dV*

-   Because the external forces are unchanged during the virtual displacement, the *δ* operator can be placed outside the integrals.
-   We can also move all terms to the same side of the equation to write

_δ_(∫<sub>*V*</sub>*U*−∫<sub>*S*</sub>*T*<sub>*i*</sub><sup>*n*</sup>*u*<sub>*i*</sub>−∫<sub>*V*</sub>*F*<sub>*i*</sub>*u*<sub>*i*</sub>*dV*) = 0

----
## virtual work

-   Or, written in terms of virtual work

_δ_(*U*<sub>*T*</sub> − *W*)=0

----
## virtual work

-   The total potential energy of an elastic solid is (*U*<sub>*T*</sub> − *W*), and must be zero for a virtual displacement
-   These results are completely general, and apply to both linear and non-linear materials
-   Special theories for rods, beams, plates, and shells use this principle
-   Finite elements is also developed using virtual work
-   We can even use virtual work to re-derive the continuum results we found previously

----
## virtual work

-   If we start with this form

∫<sub>*V*</sub>*σ*<sub>*ij*</sub>*δϵ*<sub>*ij*</sub>*dV* − ∫<sub>*S*</sub>*T*<sub>*i*</sub><sup>*n*</sup>*δu*<sub>*i*</sub>*dS* − ∫<sub>*V*</sub>*F*<sub>*i*</sub>*δu*<sub>*i*</sub>*dV* = 0

-   We can replace the first term by writing it as

_σ_<sub>*ij*</sub>*δϵ*<sub>*ij*</sub> = *σ*<sub>*ij*</sub>*δu*<sub>*i*, *j*</sub> = (*σ*<sub>*ij*</sub>*δu*<sub>*i*</sub>)<sub>,*j*</sub> − *σ*<sub>*ij*, *j*</sub>*δu*<sub>*i*</sub>

-   Which leads to

∫<sub>*V*</sub>\[(*σ*<sub>*ij*</sub>*δu*<sub>*i*</sub>)<sub>,*j*</sub> − *σ*<sub>*ij*, *j*</sub>*δu*<sub>*i*</sub>\]*dV* − ∫<sub>*S*</sub>*T*<sub>*i*</sub><sup>*n*</sup>*δu*<sub>*i*</sub>*dS* − ∫<sub>*V*</sub>*F*<sub>*i*</sub>*δu*<sub>*i*</sub>*dV* = 0

----
## virtual work

-   We can use the divergence theorem to say that

∫<sub>*V*</sub>(*σ*<sub>*ij*</sub>*δu*<sub>*i*</sub>)<sub>,*j*</sub>*dV* = ∫<sub>*S*</sub>*σ*<sub>*ij*</sub>*n*<sub>*j*</sub>*δu*<sub>*i*</sub>*dS*

-   This gives

∫<sub>*V*</sub>\[*σ*<sub>*ij*, *j*</sub> + *F*<sub>*i*</sub>\]*δu*<sub>*i*</sub>*dV* + ∫<sub>*S*</sub>(*T*<sub>*i*</sub><sup>*n*</sup> − *σ*<sub>*ij*</sub>*n*<sub>*j*</sub>)*δu*<sub>*i*</sub>*dS* = 0

----
## virtual work

-   This will be satisfied if

_σ_<sub>*ij*, *j*</sub> + *F*<sub>*i*</sub> = 0  (equilibrium)

-   And either

_δu_<sub>*i*</sub> = 0  (displacement boundary)

-   Or

_T_<sub>*i*</sub><sup>*n*</sup> = *σ*<sub>*ij*</sub>*n*<sub>*j*</sub>(traction boundary)

----
## ritz method

-   While we have showed previously how virtual work can be used to develop analytic solutions, it is also convenient for approximate solutions
-   The Rayleigh-Ritz Method is an important approximate technique based on this method
-   In this method, trial functions are used as approximate solutions which satisfy the boundary conditions, but not necessarily the differential equations.

----
## ritz method

-   For the elasticity displacement formulation, trial functions take the form

$$\\begin{aligned}
	u &= u\_0 + \\sum\_{j=1}^{N}a\_ju\_j\\\\
	v &= v\_0 + \\sum\_{j=1}^{N}b\_jv\_j\\\\
	w &= w\_0 + \\sum\_{j=1}^{N}c\_jw\_j\\\\
\\end{aligned}$$

----
## ritz method

-   Where the unknown constants are chosen to minimize the total potential energy.

$$\\begin{aligned}
	\\frac{\\partial \\Pi}{\\partial a\_j} &= 0\\\\
	\\frac{\\partial \\Pi}{\\partial b\_j} &= 0\\\\
	\\frac{\\partial \\Pi}{\\partial c\_j} &= 0\\\\
\\end{aligned}$$
