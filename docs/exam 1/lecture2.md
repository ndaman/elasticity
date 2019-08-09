# AE731
## Theory of Elasticity
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering
August 21, 2019

----
## upcoming schedule

-   Aug 21 - Coordinate Transformation
-   Aug 26 - Principal Values
-   Aug 28 - Tensor Calculus
-   Sep 2 - Labor Day
-   Sep 4 - Displacement and Strain, Homework 1 Due

----
## outline

<!-- vim-markdown-toc GFM -->

* review
* group problems
* coordinate transformation
* examples

<!-- vim-markdown-toc -->

---
# review

----
## office hours

-   TBD
-   Homework will generally be due on Wednesdays
-   Feel free to e-mail me for an appointment outside office hours if the time does not work for you

----
## homework

-   Homework 1 is available on Blackboard and [course website](https://ndaman.github.io/elasticity/#/) if you want to start working on it
-   Due on September 4 (I do not accept late homework)
-   Covers all of Chapter 1, relatively difficult, don’t wait until last minute
-   Study groups help a lot (but submit your own work)

----
## index notation

Free index vs. dummy index

<div class="left">
  <ul>
  	<li>is not repeated on any term</li>
		<li>takes all values (1,2,3)</li>
		<li>e.g. *u*<sub>*i*</sub> = ⟨*u*<sub>1</sub>, *u*<sub>2</sub>, *u*<sub>3</sub>⟩ </li>
		<li>must match across terms in an express or equation</li>
  </ul>
</div>

<div class="right">
	<ul>
		<li>is repeated on at least one term</li>
		<li>indicates summation over all values</li>
		<li>e.g. *σ*<sub>*ii*</sub> = *σ*<sub>11</sub> + *σ*<sub>22</sub> + *σ*<sub>33</sub> </li>
		<li>can not be used more than twice in the same term (*A*<sub>*ij*</sub>*B*<sub>*jk*</sub>*C*<sub>*kl*</sub> is good, *A*<sub>*ij*</sub>*B*<sub>*ij*</sub>*C*<sub>*ij*</sub> is not) </li>
	</ul>
	
</div>


----
## substitution

-   When solving tensor equations, we often need to manipulate expressions
-   We need to make sure the correct indexes are used when substituting, for example
-   *a*<sub>*i*</sub> = *U*<sub>*im*</sub>*b*<sub>*m*</sub>
-   *b*<sub>*i*</sub> = *V*<sub>*im*</sub>*c*<sub>*m*</sub>
-   To substitute the second into the first, we need to change indexes

----
## substitution

-   We need to change the free index, *i*, to *m* in the second equation
-   Since *m* is already used as the dummy index, we need to change that too
-   *b*<sub>*m*</sub> = *V*<sub>*mj*</sub>*c*<sub>*j*</sub>
-   We can now make the substitution
-   *a*<sub>*i*</sub> = *U*<sub>*im*</sub>*V*<sub>*mj*</sub>*c*<sub>*j*</sub>

----
## multiplication

-   We need to be careful with indexes when multiplying expressions
-   *p* = *a*<sub>*m*</sub>*b*<sub>*m*</sub>  and  *q* = *c*<sub>*m*</sub>*d*<sub>*m*</sub>
-   We can express, *pq*, but remember the dummy index cannot be repeated more than once
-   *pq* ≠ *a*<sub>*m*</sub>*b*<sub>*m*</sub>*c*<sub>*m*</sub>*d*<sub>*m*</sub>
-   Instead we must change the dummy index in one of the expressions first
-   *pq* = *a*<sub>*m*</sub>*b*<sub>*m*</sub>*c*<sub>*n*</sub>*d*<sub>*n*</sub>

----
## factoring

-   In the following expression, we would like to factor out *n*, but it has different indexes
-   *T*<sub>*ij*</sub>*n*<sub>*j*</sub> − *λn*<sub>*i*</sub> = 0
-   Recall *δ*<sub>*ij*</sub>*a*<sub>*j*</sub> = *a*<sub>*i*</sub>, we can rewrite *n*<sub>*i*</sub> = *δ*<sub>*ij*</sub>*n*<sub>*j*</sub>
-   *T*<sub>*ij*</sub>*n*<sub>*j*</sub> − *λδ*<sub>*ij*</sub>*n*<sub>*j*</sub> = 0
-   (*T*<sub>*ij*</sub> − *λδ*<sub>*ij*</sub>)*n*<sub>*j*</sub> = 0

----
## contraction

-   *T*<sub>*ii*</sub> is the contraction of *T*<sub>*ij*</sub>
-   This can often be a useful tool in solving tensor equations
-   *T*<sub>*ij*</sub> = *λΔδ*<sub>*ij*</sub> + 2*μE*<sub>*ij*</sub>
-		*T*<sub>*ii*</sub> = *λΔδ*<sub>*ii*</sub> + 2*μE*<sub>*ii*</sub>

----
## example

-   Solve the equation below for *U*<sub>*k*</sub> in terms of *P*<sub>*i*</sub> and *a*<sub>*i*</sub>.
-   $$\\mu \\left\[ \\delta\_{kj} a\_i a\_i + \\frac{1}{1-2\\nu} a\_k a\_j \\right\] U\_k = P\_j$$
-   Multiply both sides by *a*<sub>*j*</sub>
-		$$\\mu \\left\[ a\_j \\delta\_{kj} a\_i a\_i + \\frac{1}{1-2\\nu} a\_k a\_j a\_j \\right\] U\_k = P\_j a\_j$$
-   The dummy indexes can be changed
-		$$\\mu \\left\[ a\_j \\delta\_{kj} a\_i a\_i + \\frac{1}{1-2\\nu} a\_k a\_i a\_i \\right\] U\_k = P\_j a\_j$$

----
## example

-   *a*<sub>*j*</sub>*δ*<sub>*kj*</sub> = *a*<sub>*k*</sub>

$$\\mu U\_k \\left\[ a\_k a\_i a\_i + \\frac{1}{1-2\\nu} a\_k a\_i a\_i \\right\] = P\_j a\_j$$

-   Factoring

$$\\mu U\_k a\_k a\_i a\_i \\left\[ 1 + \\frac{1}{1-2\\nu} \\right\] = P\_j a\_j$$

-   Simplifying

$$\\mu U\_k a\_k a\_i a\_i \\left\[ \\frac{2(1-\\nu)}{1-2\\nu} \\right\] = P\_j a\_j$$

----
## example

-   Solve for *U*<sub>*k*</sub>*a*<sub>*k*</sub>

$$U\_k a\_k = \\frac{P\_j a\_j(1-2\\nu)}{2\\mu a\_i a\_i (1-\\nu) }$$

-   This is a scalar equation, we need to find *U*<sub>*j*</sub>, but we substitute this back into the original equation.

-   First, expand the original equation

$$\\mu U\_k \\delta\_{kj} a\_i a\_i + \\mu U\_k \\frac{1}{1-2\\nu} a\_k a\_j = P\_j$$

----
## example

-   After substitution, we find

$$\\mu U\_j a\_i a\_i + \\mu \\frac{1}{1-2\\nu} \\frac{P\_j a\_j(1-2\\nu)}{2\\mu a\_i a\_i (1-\\nu) } a\_j = P\_j$$

-   The index *j* is repeated too many times, so we need to change *P*<sub>*j*</sub>*a*<sub>*j*</sub> to a different index

$$\\mu U\_j a\_i a\_i + \\frac{P\_k a\_k}{2 a\_i a\_i (1-\\nu) } a\_j = P\_j$$

-   We can now solve for *U*<sub>*j*</sub>

$$U\_j  = \\frac{1}{\\mu a\_i a\_i} \\left\[P\_j - \\frac{P\_k a\_k}{2 a\_i a\_i (1-\\nu) } a\_j\\right\]$$

----
## symmetry

-   Two types of symmetry: symmetry and antisymmetry

-   Symmetry: *a*<sub>*ij*</sub> = *a*<sub>*ji*</sub>

-   Anti-symmetry: *a*<sub>*ij*</sub> = −*a*<sub>*ji*</sub>

----
## symmetry

-   We can break any tensor up into symmetric and anti-symmetric portions

-   $a\_{ij} = \\frac{1}{2} (a\_{ij} + a\_{ji}) + \\frac{1}{2} (a\_{ij} - a\_{ji})$

----
## example

-   Find symmetric and anti-symmetric portions of

$$\\begin{bmatrix}
1 & 4 & 3\\\\
2 & 1 & 5\\\\
4 & 3 & 6
\\end{bmatrix}$$

----
## example symmetric portion

$$a\_{(ij)} = \\frac{1}{2}(a\_{ij} + a\_{ji})$$

$$a\_{(ij)} = \\frac{1}{2} \\left (
\\begin{bmatrix}
1 & 4 & 3\\\\
2 & 1 & 5\\\\
4 & 3 & 6
\\end{bmatrix}+
\\begin{bmatrix}
1 & 2 & 4\\\\
4 & 1 & 3\\\\
3 & 5 & 6
\\end{bmatrix}\\right)
= \\begin{bmatrix}
1 & 3 & 3.5\\\\
3 & 1 & 4\\\\
3.5 & 4 & 6
\\end{bmatrix}$$

----
## example Anti-symmetric portion

$$a\_{(ij)} = \\frac{1}{2}(a\_{ij} - a\_{ji})$$

$$a\_{(ij)} = \\frac{1}{2} \\left (
\\begin{bmatrix}
1 & 4 & 3\\\\
2 & 1 & 5\\\\
4 & 3 & 6
\\end{bmatrix}-
\\begin{bmatrix}
1 & 2 & 4\\\\
4 & 1 & 3\\\\
3 & 5 & 6
\\end{bmatrix}\\right)
= \\begin{bmatrix}
0 & 1 & -0.5\\\\
-1 & 0 & 1\\\\
0.5 & -1 & 0
\\end{bmatrix}$$

---
# group problems

----
## group 1 

Identify the dummy and free indexes in each of the following expressions. Indicate the tensor order of the expression. If index notation is used incorrectly, identify why it is used incorrectly and propose a correction.

1.  *a*<sub>*i*</sub>*b*<sub>*j*</sub>*c*<sub>*k*</sub> + *d*<sub>*ijk*</sub>
2.  *a*<sub>*ii*</sub>*b*<sub>*k*</sub> + *c*<sub>*kk*</sub>*d*<sub>*j*</sub>
3.  *C*<sub>*ijkl*</sub>*ϵ*<sub>*kl*</sub>

----
## group 2 

Is it possible to factor *n*<sub>*i*</sub> from the following equation? If so, factor it.

*T*<sub>*ij*</sub>*n*<sub>*j*</sub> − *λn*<sub>*i*</sub> = 0

----
## group 3 

Find the symmetric, *S*<sub>*ij*</sub>, and anti-symmetric, *A*<sub>*ij*</sub>, portions of *T*<sub>*ij*</sub>. 
Verify that *S*<sub>*ij*</sub> + *A*<sub>*ij*</sub> = *T*<sub>*ij*</sub>

$$T\_{ij} = \\begin{bmatrix}
      1 & 0 & 3\\\\
      0 & 1 & 2\\\\
      3 & 0 & 3
  \\end{bmatrix}$$

---
# coordinate transformation

----
## coordinate transformation in two dimensions

TODO: figure

----
## coordinate transformation in two dimensions

-   The vector, *v*, remains fixed, but we transform our coordinate system
-   In the new coordinate system, the *x*<sub>2</sub><sup>′</sup> portion of *v* is zero.
-   To transform the coordinate system, we first define some unit vectors.
-   $\\hat{e}\_1$ is a unit vector in the direction of *x*<sub>1</sub>, while $\\hat{e}\_1^\\prime$ is a unit vector in the direction of *x*<sub>1</sub><sup>′</sup>

----
## coordinate transformation in two dimensions

TODO: figure

----
## coordinate transformation in two dimensions

-   For this example, let us assume *v* = ⟨2, 2⟩ and *θ* = 45<sup>∘</sup>
-   We can write the transformed unit vectors, $\\hat{e}\_1^\\prime$ and $\\hat{e}\_2^\\prime$ in terms of $\\hat{e}\_1$, $\\hat{e}\_2$ and the angle of rotation, *θ*.

$$\\begin{aligned}
\\hat{e}\_1^\\prime &= \\langle \\hat{e}\_1 \\cos \\theta , \\hat{e}\_2 \\sin \\theta\\rangle\\\\
\\hat{e}\_2^\\prime &= \\langle -\\hat{e}\_1 \\sin \\theta , \\hat{e}\_2 \\cos \\theta \\rangle\\end{aligned}$$

----
## coordinate transformation in two dimensions

-   We can write the vector, *v*, in terms of the unit vectors describing our axis system
-   $v = v\_1 \\hat{e}\_1 + v\_2 \\hat{e}\_2$
-   (note: $\\hat{e}\_1=\\langle 1, 0 \\rangle$ and $\\hat{e}\_2 = \\langle 0,1 \\rangle$)
-   *v* = ⟨2, 2⟩=2⟨1, 0⟩+2⟨0, 1⟩

----
## coordinate transformation in two dimensions

-   When expressed in the transformed coordinate system, we refer to *v*<sup>′</sup>
-   *v*<sup>′</sup> = ⟨*v*<sub>1</sub>cos*θ* + *v*<sub>2</sub>sin*θ*, −*v*<sub>1</sub>sin*θ* + *v*<sub>2</sub>cos*θ*⟩
-   $v^\\prime = \\langle 2\\sqrt{2}, 0 \\rangle$
-   We can recover the original vector from the transformed coordinates:
-   $v = v\_1^\\prime \\hat{e}\_1^\\prime + v\_2^\\prime \\hat{e}\_2^\\prime$
-   (note: $\\hat{e}\_1^\\prime=\\langle \\frac{\\sqrt{2}}{2},\\frac{\\sqrt{2}}{2} \\rangle$ and $\\hat{e}\_2^\\prime = \\langle -\\frac{\\sqrt{2}}{2},\\frac{\\sqrt{2}}{2} \\rangle$)
-   $v = 2\\sqrt{2}\\langle \\frac{\\sqrt{2}}{2},\\frac{\\sqrt{2}}{2} \\rangle, 0 \\langle -\\frac{\\sqrt{2}}{2},\\frac{\\sqrt{2}}{2} \\rangle = \\langle 2, 2 \\rangle$

----
## general coordinate transformation

-   Coordinate transformation can become much more complicated in three dimensions, and with higher-order tensors
-   It is convenient to define a general form of the coordinate transformation in index notation
-   We define *Q*<sub>*ij*</sub> as the cosine of the angle between the *x*<sub>*i*</sub><sup>′</sup> axis and the *x*<sub>*j*</sub> axis.
-   This is also referred to as the “direction cosine”
    *Q*<sub>*ij*</sub> = cos(*x*<sub>*i*</sub><sup>′</sup>, *x*<sub>*j*</sub>)

----
## general coordinate transformation

-   We can use this form on our 2D transformation example

$$\\begin{aligned}
Q\_{ij} &= \\cos (x\_i^\\prime, x\_j)\\\\ &= \\begin{bmatrix}
\\cos (x\_1^\\prime, x\_1) & \\cos (x\_1^\\prime, x\_2)\\\\
\\cos (x\_2^\\prime, x\_1) & \\cos (x\_2^\\prime, x\_2)
\\end{bmatrix}\\\\ &= \\begin{bmatrix}
\\cos \\theta & \\cos (90-\\theta)\\\\
\\cos (90+\\theta) & \\cos \\theta
\\end{bmatrix} \\\\ &= \\begin{bmatrix}
\\cos \\theta & \\sin \\theta \\\\
-\\sin \\theta & \\cos \\theta
\\end{bmatrix}\\end{aligned}$$

----
## general coordinate transformation

-   We can transform any-order tensor using *Q*<sub>*ij*</sub>
-   Vectors (first-order tensors): *v*<sub>*i*</sub><sup>′</sup> = *Q*<sub>*ij*</sub>*v*<sub>*j*</sub>
-   Matrices (second-order tensors): *σ*<sub>*mn*</sub><sup>′</sup> = *Q*<sub>*mi*</sub>*Q*<sub>*nj*</sub>*σ*<sub>*ij*</sub>
-   Fourth-order tensors: *C*<sub>*ijkl*</sub><sup>′</sup> = *Q*<sub>*im*</sub>*Q*<sub>*jn*</sub>*Q*<sub>*ko*</sub>*Q*<sub>*lp*</sub>*C*<sub>*mnop*</sub>

----
## general coordinate transformation

-   We can similarly use *Q*<sub>*ij*</sub> to find tensors in the original coordinate system
-   Vectors (first-order tensors): *v*<sub>*i*</sub> = *Q*<sub>*ji*</sub>*v*<sub>*j*</sub><sup>′</sup>
-   Matrices (second-order tensors): *σ*<sub>*mn*</sub> = *Q*<sub>*im*</sub>*Q*<sub>*jn*</sub>*σ*<sub>*ij*</sub><sup>′</sup>
-   Fourth-order tensors: *C*<sub>*ijkl*</sub> = *Q*<sub>*mi*</sub>*Q*<sub>*nj*</sub>*Q*<sub>*ok*</sub>*Q*<sub>*pl*</sub>*C*<sub>*mnop*</sub><sup>′</sup>

----
## general coordinate transformation

-   We can derive some interesting properties of the transformation tensor, *Q*<sub>*ij*</sub>
-   We know that *v*<sub>*i*</sub> = *Q*<sub>*ji*</sub>*v*<sub>*j*</sub><sup>′</sup> and that *v*<sub>*i*</sub><sup>′</sup> = *Q*<sub>*ij*</sub>*v*<sub>*j*</sub>
-   If we substitute (changing the appropriate indexes) we find:
-   *v*<sub>*i*</sub> = *Q*<sub>*ji*</sub>*Q*<sub>*jk*</sub>*v*<sub>*k*</sub>
-   We can now use the Kronecker Delta to substitute *v*<sub>*i*</sub> = *δ*<sub>*ik*</sub>*v*<sub>*k*</sub> which gives
-   *δ*<sub>*ik*</sub>*v*<sub>*k*</sub> = *Q*<sub>*ji*</sub>*Q*<sub>*jk*</sub>*v*<sub>*k*</sub>

---
# examples

----
## example

TODO: Figure

-   Find *Q*<sub>*ij*</sub><sup>1</sup> for rotation of 60<sup>∘</sup> about *x*<sub>2</sub>
-   Find *Q*<sub>*ij*</sub><sup>2</sup> for rotation of 30<sup>∘</sup> about *x*<sub>3</sub><sup>′</sup>
-   Find *e*<sub>*i*</sub><sup>′′</sup> after both rotations

----
## example

TODO: Figure

----
## example

TODO: figure

----
## example

-   *Q*<sub>*ij*</sub><sup>1</sup> = cos(*x*<sub>*i*</sub><sup>′</sup>, *x*<sub>*j*</sub>)
-   *Q*<sub>*ij*</sub><sup>2</sup> = cos(*x*<sub>*i*</sub><sup>′′</sup>, *x*<sub>*j*</sub><sup>′</sup>)

$$Q\_{ij}^1 = \\begin{bmatrix}
\\cos 60 & \\cos 90 & \\cos 150\\\\
\\cos 90 & \\cos 0 & \\cos 90\\\\
\\cos 30 & \\cos 90 & \\cos 60
\\end{bmatrix}$$
$$Q\_{ij}^2 = \\begin{bmatrix}
\\cos 30 & \\cos 60 & \\cos 90\\\\
\\cos 120 & \\cos 30 & \\cos 90\\\\
\\cos 90 & \\cos 90 & \\cos 0
\\end{bmatrix}$$

----
## example

-   We now use *Q*<sub>*ij*</sub> to find $\\hat{e}\_i^\\prime$ and $\\hat{e}\_i^{\\prime \\prime}$
-   First, we need to write $\\hat{e}\_i$ in a manner more consistent with index notation
-   We will indicate axis direction with a superscript, e.g. $\\hat{e}\_1 = e\_i^1$
-   *e*<sub>*i*</sub><sup>′</sup> = *Q*<sub>*ij*</sub><sup>1</sup>*e*<sub>*j*</sub>
-   *e*<sub>*i*</sub><sup>′′</sup> = *Q*<sub>*ij*</sub><sup>2</sup>*e*<sub>*j*</sub><sup>′</sup>
-   How do we find *e*<sub>*i*</sub><sup>′′</sup> in terms of *e*<sub>*i*</sub>?
-   *e*<sub>*i*</sub><sup>′′</sup> = *Q*<sub>*ij*</sub><sup>2</sup>*Q*<sub>*jk*</sub><sup>1</sup>*e*<sub>*k*</sub>


