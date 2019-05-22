----
## upcoming schedule

-   Aug 23 - Coordinate Transformation

-   Aug 28 - Principal Values

-   Aug 30 - Tensor Calculus

-   Sep 4 - Labor Day (No Class)

-   Sep 6 - Homework 1 Due, Displacement and Strain

----
## AIAA event

-   August 25, 2017 at 1:00

-   123 Wallace Hall

-   Dr. Thomas Wayman, Group Head for supersonics division at Gulfstream

Review
======

----
## office hours

-   Tues 2-3

-   Homework will generally be due on Wednesdays

-   Feel free to e-mail me for an appointment outside office hours if the time does not work for you

----
## homework

-   Homework 1 is available on Blackboard if you want to start working on it

-   Due on September 6 (I do not accept late homework)

-   Covers all of Chapter 1, relatively difficult, don’t wait until last minute

-   Study groups help a lot (but submit your own work)

----
## index notation

Free index vs. dummy index

Free index is not repeated (on any term)

Free index takes all values (1,2,3)

e.g. *u*<sub>*i*</sub> = ⟨*u*<sub>1</sub>, *u*<sub>2</sub>, *u*<sub>3</sub>⟩

Free indexes must match across terms in an expression or equation

Dummy index is repeated on at least one term

Dummy index indicates summation over all values

e.g. *σ*<sub>*i**i*</sub> = *σ*<sub>11</sub> + *σ*<sub>22</sub> + *σ*<sub>33</sub>

Index can not be used more than twice in the same term (*A*<sub>*i**j*</sub>*B*<sub>*j**k*</sub>*C*<sub>*k**l*</sub> is good, *A*<sub>*i**j*</sub>*B*<sub>*i**j*</sub>*C*<sub>*i**j*</sub> is not)

----
## substitution

-   When solving tensor equations, we often need to manipulate expressions

-   We need to make sure the correct indexes are used when substituting, for example

-   
    *a*<sub>*i*</sub> = *U*<sub>*i**m*</sub>*b*<sub>*m*</sub>

-   
    *b*<sub>*i*</sub> = *V*<sub>*i**m*</sub>*c*<sub>*m*</sub>

-   To substitute (\[eq:second\]) into (\[eq:first\]), we first need to change indexes

----
## substitution

-   We need to change the free index, *i*, to *m* in (\[eq:second\])

-   Since *m* is already used as the dummy index, we need to change that too

-   
    *b*<sub>*m*</sub> = *V*<sub>*m**j*</sub>*c*<sub>*j*</sub>

-   We can now make the substitution

-   
    *a*<sub>*i*</sub> = *U*<sub>*i**m*</sub>*V*<sub>*m**j*</sub>*c*<sub>*j*</sub>

----
## multiplication

-   We need to be careful with indexes when multiplying expressions

-   
    *p* = *a*<sub>*m*</sub>*b*<sub>*m*</sub>  and  *q* = *c*<sub>*m*</sub>*d*<sub>*m*</sub>

-   We can express, *p**q*, but remember the dummy index cannot be repeated more than once

-   
    *p**q* ≠ *a*<sub>*m*</sub>*b*<sub>*m*</sub>*c*<sub>*m*</sub>*d*<sub>*m*</sub>

-   Instead we must change the dummy index in one of the expressions first

-   
    *p**q* = *a*<sub>*m*</sub>*b*<sub>*m*</sub>*c*<sub>*n*</sub>*d*<sub>*n*</sub>

----
## factoring

-   In the following expression, we would like to factor out *n*, but it has different indexes

-   
    *T*<sub>*i**j*</sub>*n*<sub>*j*</sub> − *λ**n*<sub>*i*</sub> = 0

-   Recall *δ*<sub>*i**j*</sub>*a*<sub>*j*</sub> = *a*<sub>*i*</sub>, we can rewrite *n*<sub>*i*</sub> = *δ*<sub>*i**j*</sub>*n*<sub>*j*</sub>

-   
    *T*<sub>*i**j*</sub>*n*<sub>*j*</sub> − *λ**δ*<sub>*i**j*</sub>*n*<sub>*j*</sub> = 0

-   
    (*T*<sub>*i**j*</sub> − *λ**δ*<sub>*i**j*</sub>)*n*<sub>*j*</sub> = 0

----
## contraction

-   *T*<sub>*i**i*</sub> is the contraction of *T*<sub>*i**j*</sub>

-   This can often be a useful tool in solving tensor equations

-   
    *T*<sub>*i**j*</sub> = *λ**Δ**δ*<sub>*i**j*</sub> + 2*μ**E*<sub>*i**j*</sub>

-   
    *T*<sub>*i**i*</sub> = *λ**Δ**δ*<sub>*i**i*</sub> + 2*μ**E*<sub>*i**i*</sub>

----
## example

-   Solve the equation below for *U*<sub>*k*</sub> in terms of *P*<sub>*i*</sub> and *a*<sub>*i*</sub>.
    $$\\mu \\left\[ \\delta\_{kj} a\_i a\_i + \\frac{1}{1-2\\nu} a\_k a\_j \\right\] U\_k = P\_j$$

-   Multiply both sides by *a*<sub>*j*</sub>
    $$\\mu \\left\[ a\_j \\delta\_{kj} a\_i a\_i + \\frac{1}{1-2\\nu} a\_k a\_j a\_j \\right\] U\_k = P\_j a\_j$$

-   The dummy indexes can be changed
    $$\\mu \\left\[ a\_j \\delta\_{kj} a\_i a\_i + \\frac{1}{1-2\\nu} a\_k a\_i a\_i \\right\] U\_k = P\_j a\_j$$

----
## example

-   *a*<sub>*j*</sub>*δ*<sub>*k**j*</sub> = *a*<sub>*k*</sub>
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

-   Symmetry: *a*<sub>*i**j*</sub> = *a*<sub>*j**i*</sub>

-   Anti-symmetry: *a*<sub>*i**j*</sub> = −*a*<sub>*j**i*</sub>

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
## example Symmetric portion
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

group problems
==============

----
## group 1 Identify the dummy and free indexes in each of the following expressions. Indicate the tensor order of the expression. If index notation is used incorrectly, identify why it is used incorrectly and propose a correction.

1.  *a*<sub>*i*</sub>*b*<sub>*j*</sub>*c*<sub>*k*</sub> + *d*<sub>*i**j**k*</sub>

2.  *a*<sub>*i**i*</sub>*b*<sub>*k*</sub> + *c*<sub>*k**k*</sub>*d*<sub>*j*</sub>

3.  *C*<sub>*i**j**k**l*</sub>*ϵ*<sub>*k**l*</sub>

----
## group 2 Is it possible to factor *n*<sub>*i*</sub> from the following equation? If so, factor it.
*T*<sub>*i**j*</sub>*n*<sub>*j*</sub> − *λ**n*<sub>*i*</sub> = 0

----
## group 3 Find the symmetric, *S*<sub>*i**j*</sub>, and anti-symmetric, *A*<sub>*i**j*</sub>, portions of *T*<sub>*i**j*</sub>. Verify that *S*<sub>*i**j*</sub> + *A*<sub>*i**j*</sub> = *T*<sub>*i**j*</sub>
$$T\_{ij} = \\begin{bmatrix}
      1 & 0 & 3\\\\
      0 & 1 & 2\\\\
      3 & 0 & 3
  \\end{bmatrix}$$

Coordinate Transformation
=========================

----
## coordinate transformation in two dimensions

(0,3) node (yaxis) \[above\] ----
## *x*<sub>2</sub></span> |- (3,0) node (xaxis) \[right\] <span>*x*<sub>1</sub></span>; (0,0) – (-2.12,2.12) node (yprime) \[above left\] <span>*x*<sub>2</sub><sup>′</sup></span>; (0,0) – (2.12,2.12) node (xprime) \[above right\] <span>*x*<sub>1</sub><sup>′</sup></span>; (0,0) – (1.5,1.5) node (v) \[above left\] <span>*v*;

----
## coordinate transformation in two dimensions

-   The vector, *v*, remains fixed, but we transform our coordinate system

-   In the new coordinate system, the *x*<sub>2</sub><sup>′</sup> portion of *v* is zero.

-   To transform the coordinate system, we first define some unit vectors.

-   $\\hat{e}\_1$ is a unit vector in the direction of *x*<sub>1</sub>, while $\\hat{e}\_1^\\prime$ is a unit vector in the direction of *x*<sub>1</sub><sup>′</sup>

----
## coordinate transformation in two dimensions

(0,3) node (yaxis) \[above\] ----
## *x*<sub>2</sub></span> |- (3,0) node (xaxis) \[right\] <span>*x*<sub>1</sub></span>; (0,1) node (j) \[above right\] <span>$\\hat{e}\_2$</span> |- (1,0) node (i) \[below right\] <span>$\\hat{e}\_1$</span>; (0,0) – (-2.12,2.12) node (yprime) \[above left\] <span>*x*<sub>2</sub><sup>′</sup></span>; (0,0) – (2.12,2.12) node (xprime) \[above right\] <span>*x*<sub>1</sub><sup>′</sup></span>; (0,0) – (-.707,.707) node (jprime) \[above right\] <span>$\\hat{e}\_2^\\prime$</span>; (0,0) – (.707,.707) node (iprime) \[right\] <span>$\\hat{e}\_1^\\prime$</span>; (0,0) – (1.5,1.5) node (v) \[above left\] <span>*v*</span>; (0.5,0) arc (0:45:0.5) node (theta) \[below right = -0.1cm and 0.3cm\] <span>*θ*;

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

-   We define *Q*<sub>*i**j*</sub> as the cosine of the angle between the *x*<sub>*i*</sub><sup>′</sup> axis and the *x*<sub>*j*</sub> axis.

-   This is also referred to as the “direction cosine”
    *Q*<sub>*i**j*</sub> = cos(*x*<sub>*i*</sub><sup>′</sup>, *x*<sub>*j*</sub>)

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

-   We can transform any-order tensor using *Q*<sub>*i**j*</sub>

-   Vectors (first-order tensors): *v*<sub>*i*</sub><sup>′</sup> = *Q*<sub>*i**j*</sub>*v*<sub>*j*</sub>

-   Matrices (second-order tensors): *σ*<sub>*m**n*</sub><sup>′</sup> = *Q*<sub>*m**i*</sub>*Q*<sub>*n**j*</sub>*σ*<sub>*i**j*</sub>

-   Fourth-order tensors: *C*<sub>*i**j**k**l*</sub><sup>′</sup> = *Q*<sub>*i**m*</sub>*Q*<sub>*j**n*</sub>*Q*<sub>*k**o*</sub>*Q*<sub>*l**p*</sub>*C*<sub>*m**n**o**p*</sub>

----
## general coordinate transformation

-   We can similarly use *Q*<sub>*i**j*</sub> to find tensors in the original coordinate system

-   Vectors (first-order tensors): *v*<sub>*i*</sub> = *Q*<sub>*j**i*</sub>*v*<sub>*j*</sub><sup>′</sup>

-   Matrices (second-order tensors): *σ*<sub>*m**n*</sub> = *Q*<sub>*i**m*</sub>*Q*<sub>*j**n*</sub>*σ*<sub>*i**j*</sub><sup>′</sup>

-   Fourth-order tensors: *C*<sub>*i**j**k**l*</sub> = *Q*<sub>*m**i*</sub>*Q*<sub>*n**j*</sub>*Q*<sub>*o**k*</sub>*Q*<sub>*p**l*</sub>*C*<sub>*m**n**o**p*</sub><sup>′</sup>

----
## general coordinate transformation

-   We can derive some interesting properties of the transformation tensor, *Q*<sub>*i**j*</sub>

-   We know that *v*<sub>*i*</sub> = *Q*<sub>*j**i*</sub>*v*<sub>*j*</sub><sup>′</sup> and that *v*<sub>*i*</sub><sup>′</sup> = *Q*<sub>*i**j*</sub>*v*<sub>*j*</sub>

-   If we substitute (changing the appropriate indexes) we find:

-   *v*<sub>*i*</sub> = *Q*<sub>*j**i*</sub>*Q*<sub>*j**k*</sub>*v*<sub>*k*</sub>

-   We can now use the Kronecker Delta to substitute *v*<sub>*i*</sub> = *δ*<sub>*i**k*</sub>*v*<sub>*k*</sub> which gives

-   *δ*<sub>*i**k*</sub>*v*<sub>*k*</sub> = *Q*<sub>*j**i*</sub>*Q*<sub>*j**k*</sub>*v*<sub>*k*</sub>

Examples
========

----
## example

(0,0,0) – (3,0,0) node\[below left\] ----
## *x*<sub>1</sub></span>; (0,0,0) – (0,3,0) node\[right\] <span>*x*<sub>2</sub></span>; (0,0,0) – (0,0,3) node\[above\] <span>*x*<sub>3</sub>;

-   Find *Q*<sub>*i**j*</sub><sup>1</sup> for rotation of 60<sup>∘</sup> about *x*<sub>2</sub>

-   Find *Q*<sub>*i**j*</sub><sup>2</sup> for rotation of 30<sup>∘</sup> about *x*<sub>3</sub><sup>′</sup>

-   Find *e*<sub>*i*</sub><sup>′′</sup> after both rotations

----
## example

(0,0,0) – (3,0,0) node\[below left\] ----
## *x*<sub>1</sub></span>; (0,0,0) – (0,3,0) node\[right\] <span>*x*<sub>2</sub>, *x*<sub>2</sub><sup>′</sup></span>; (0,0,0) – (0,0,3) node\[above\] <span>*x*<sub>3</sub></span>; (0,0,0) – (2.6,0,1.5) node\[above\] <span>*x*<sub>3</sub><sup>′</sup></span>; (0,0,0) – (1.5,0,-2.6) node\[below left\] <span>*x*<sub>1</sub><sup>′</sup></span>; <span>above left</span><span>*θ*<sub>1</sub></span> <span>below left</span><span>*θ*<sub>1</sub>

----
## example

(0,0,0) – (3,0,0) node\[below left\] ----
## *x*<sub>1</sub></span>; (0,0,0) – (0,3,0) node\[right\] <span>*x*<sub>2</sub>, *x*<sub>2</sub><sup>′</sup></span>; (0,0,0) – (0,0,3) node\[above\] <span>*x*<sub>3</sub></span>; (0,0,0) – (2.6,0,1.5) node\[above\] <span>*x*<sub>3</sub><sup>′</sup>, *x*<sub>3</sub><sup>′′</sup></span>; (0,0,0) – (1.5,0,-2.6) node\[below left\] <span>*x*<sub>1</sub><sup>′</sup></span>; <span>above left</span><span>*θ*<sub>1</sub></span> <span>below left</span><span>*θ*<sub>1</sub></span>; ; (0,0,0) – (2.6,1.5,0) node\[below right\] <span>*x*<sub>1</sub><sup>′′</sup></span>; (0,0,0) – (-1.5,2.6,0) node\[below right\] <span>*x*<sub>2</sub><sup>′′</sup>; ; ;

----
## example

-   *Q*<sub>*i**j*</sub><sup>1</sup> = cos(*x*<sub>*i*</sub><sup>′</sup>, *x*<sub>*j*</sub>)

-   *Q*<sub>*i**j*</sub><sup>2</sup> = cos(*x*<sub>*i*</sub><sup>′′</sup>, *x*<sub>*j*</sub><sup>′</sup>)
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

-   We now use *Q*<sub>*i**j*</sub> to find $\\hat{e}\_i^\\prime$ and $\\hat{e}\_i^{\\prime \\prime}$

-   First, we need to write $\\hat{e}\_i$ in a manner more consistent with index notation

-   We will indicate axis direction with a superscript, e.g. $\\hat{e}\_1 = e\_i^1$

-   *e*<sub>*i*</sub><sup>′</sup> = *Q*<sub>*i**j*</sub><sup>1</sup>*e*<sub>*j*</sub>

-   *e*<sub>*i*</sub><sup>′′</sup> = *Q*<sub>*i**j*</sub><sup>2</sup>*e*<sub>*j*</sub><sup>′</sup>

-   How do we find *e*<sub>*i*</sub><sup>′′</sup> in terms of *e*<sub>*i*</sub>?

-   *e*<sub>*i*</sub><sup>′′</sup> = *Q*<sub>*i**j*</sub><sup>2</sup>*Q*<sub>*j**k*</sub><sup>1</sup>*e*<sub>*k*</sub>


