# AE731
## Theory of Elasticity
Dr. Nicholas Smith<br/>
Wichita State University, Department of Aerospace Engineering
August 19, 2019

----
## upcoming schedule

-   Aug 19 - Intro to Elasticity
-   Aug 21 - Coordinate Transformation
-   Aug 26 - Principal Values
-   Aug 28 - Tensor Calculus

----
## outline

<!-- vim-markdown-toc GFM -->

* introduction
* syllabus and schedule
* calculus of tensors
* examples

<!-- vim-markdown-toc -->

---
# introduction

----
## about me

![family picture](../images/IMG_5266_edit.jpg) <!-- .element width="75%" -->

----
## education
  - B.S. in Mechanical Engineering from Brigham Young University
    - Worked with ATK to develop tab-less gripping system for tensile testing composite tow specimens
    - Needed to align the specimen, as well as grip it without causing a stress concentration

----
## education
  - M.S. and Ph.D. from School of Aeronautics and Astronautics at Purdue University
    - Worked with Boeing to simulate mold flows
    - First ever mold simulation with anisotropic viscosity

----
## research
![picture of chopped carbon fiber prepreg](../images/Formosa_Chopped_Carbon_Fiber_CSc_bw.jpg)

----
## research
![picture of lamborghini symbol made from compression molded chopped carbon fiber](../images/lamborghini-chopped-fiber-badges-rough.jpg)

----
## research

  <div class='left'>
![picture illustrating the fused deposition modeling 3D printing process, where plastic filament is melted and deposited next to other filament, and fuses together](../images/3D-printing.png)
  </div>

  <div class='right'>
  <ul>
  <li> Composites are being used in 3D printing now </li>
  <li> Printing patterns are optimized for isotropic materials </li>
  <li> Sometimes composites hurt more than they help when not utilized properly </li>
  </div>

----
## research

<div class="left">
	<ul>
		<li>Thermoplastic composites offer many advantages over thermoset</li>
		<li>Production speed, recyclability</li>
		<li>Also have challenges, such as bonding/welding</li>
	</ul>
</div>
<div class="right">

![thermoplastic welding](../images/Welding-thermoplastic-composites.jpg)

</div>


----
## classes

-   AE 731 Elasticity Theory (odd years in fall)
-   AE 737 Mechanics of Damage Tolerance (every year in spring)
-   AE 837 Advanced Mechanics of Damage Tolerance (odd years in fall)
-   AE 760AA Micromechanics and Multiscale Modeling (odd years in spring)
-   AE 831 Continuum Mechanics (even years in fall)

----
## introductions

-   Name
-   Student status (Undergrad, Masters, Ph.D)
-   Full time or part time student?
-   One interesting thing to remember you by

---
# syllabus and schedule

----
## course website

-   All class materials will be posted on the [class website](https://ndaman.github.io/elasticity/#/)
-   I will also make an effort to post to Blackboard, but it takes a little more effort, so you may need to remind me
-   The website uses the same format as my presentations, so treat it like slides (navigate with arrow keys)

----
## course textbook

-   Martin H. Saad, *Elasticity: Theory, Application, and Numerics*
-   Any version is sufficient
-   Homework will be given in handouts
-   Textbook will be closely followed in class and is a very highly regarded elasticity text
-   Includes useful MATLAB tutorials, as well as some more specialized topics we will not have time to cover in this course, but may be useful to your research

----
## office hours

-   I will e-mail everyone in the course a Doodle link we can use to find the optimal office hours
-   Let me know if you do not receive the e-mail, you may need to update your information in Blackboard
-   Take advantage of office hours, this is time that I have already set aside for you
-   If the regular office hours do not work for your schedule, send me an e-mail and we can work out a time to meet

----
## tentative outline

-   Chapter 1 - Calculus of tensors
    -   19 Aug - 28 Aug (4 lectures)
-   Chapter 2 - Kinematics
    -   4 Sep - 11 Sep (3 lectures)
-   Exam 1 (covers Chapter 1-2)
    -   18 Sep

----
## tentative outline

-   Chapter 3 - Stress
    -   23 Sep - 30 Sep (3 lectures)
-   Chapter 4 - Constitutive equations
    -   2 Oct - 9 Oct (3 lectures)
-   Chapter 5 - Solution strategies
    -   16 Oct - 23 Oct (3 lectures)
-   Exam 2 (Chapters 3-5)
    -   30 Oct

----
## tentative outline

<div class="left">
<ul>
	<li>Ch 6 - Energy principles</li>
	<ul>
		<li>4 Nov - 11 Nov (3 lectures)</li>
	</ul>
	<li>Ch 7-8 - 2D problems</li>
	<ul>
		<li>13 Nov - 20 Nov (3 lectures)</li>
	</ul>
	<li>Ch 10 - Complex variables</li>
	<ul>
		<li>2 Dec - 4 Dec</li>
	</ul>
</ul>
</div>
<div class="right">
	<ul>
		<li>Special topics</li>
		<ul>
			<li>No homework</li>
			<li>Not on final exam</li>
			<li>Anisotropic elasticity</li>
			<li>Heterogeneous materials</li>
			<li>Numerical applications (finite elements)</li>
		</ul>
	</ul>
</div>

----
## final exam

-   Wednesday 11 December
-   3:00 - 4:50 pm
-   Cannot take final exam at any other time, make travel plans accordingly
-   Comprehensive

----
## grades

-   Grade breakdown
    -   Homework 15%
    -   Exam 1 25%
    -   Exam 2 25%
    -   Final Exam 35%
-   Follow a traditional grading scale

----
## class expectations

-   Consider the cost (to you or others) of your being in class
-   I ask that you refrain from distracting behaviors during class
-   When you have something more important than class to take care of it, please take care of it outside of class

---
# calculus of tensors

----
## scalars

-   Scalar
    -   single value (at a point)
    -   e.g. temperature, density

----
## vectors

-   Vector
    -   expressed in terms of coordinate system
    -   one-dimensional array
    -   e.g. displacement

----
## matrices

-   Matrix
    -   two-dimensional array
    -   e.g. stress, strain

----
## scalars, vectors, matrices

*ρ* = 25

*u* = ⟨*x*, *y*⟩

$$\[\\sigma\] = \\begin{bmatrix}
\\sigma\_{xx} & \\sigma\_{xy} \\\\
\\sigma\_{yx} & \\sigma\_{yy}
\\end{bmatrix}$$

----
## scalars, vectors, matrices

<div class="left">
	<ul>
		<li>In two dimensions</li>
		<ul>
      <li>Scalars have 1 term</li>				
			<li>Vectors have 2 terms</li>
			<li>Matrices have 4 terms</li>
		</ul>
	</ul>	
</div>
<div class="right">
	<ul>
		<li>In three dimensions</li>
		<ul>
			<li>Scalars have 1 term</li>
			<li>Vectors have 3 terms</li>
			<li>Matrices have 9 terms</li>
		</ul>
	</ul>
</div>

----
## tensors

-   Formal definition for tensors later in the course
-   Scalar = 0-order tensor
-   Vector = 1st-order tensor
-   Matrix = 2nd-order tensor

----
## tensors

-   We will also use higher-order tensors in this course
-   High-order tensors are difficult to write
-   It can even be difficult to distinguish vectors, scalars, and matrices in some notations
-   Index notation is used to address these problems

----
## index notation

-   Use subscripts to indicate when a variable has multiple values
-   *ρ* has no subscript, and thus it must be a scalar
-   *u*<sub>*i*</sub> has one subscript, *i*, indicating it has multiple values
-   “Multiple” means the number of coordinate system axes, unless otherwise specified.
-   *u*<sub>*i*</sub> = ⟨*u*<sub>1</sub>, *u*<sub>2</sub>, *u*<sub>3</sub>⟩

----
## index notation

-   *σ*<sub>*ij*</sub> has two subscripts, *i* and *j*, meaning it spans the coordinate system in two directions.
-   $\\sigma\_{ij} = \\begin{bmatrix}
    \\sigma\_{11} & \\sigma\_{12}\\\\
    \\sigma\_{21} & \\sigma\_{22}
    \\end{bmatrix}$

-   We can use this notation for any order of tensor
-   In 3D, we need a fourth-order tensor to define material stiffness, we write this in index notation as
-   *C*<sub>*ijkl*</sub>

----
## addition

-   We can do arithmetic in index notation
-   *a*<sub>*i*</sub> + *b*<sub>*i*</sub> = ⟨*a*<sub>1</sub> + *b*<sub>1</sub>, *a*<sub>2</sub> + *b*<sub>2</sub>⟩
-   We can also use a different index in the two variables to create a matrix
-   $c\_{ij} = a\_i + b\_j = \\begin{bmatrix}
    a\_1 + b\_1 & a\_1 + b\_2 \\\\
    a\_2 + b\_1 & a\_2 + b\_2
    \\end{bmatrix}$

----
## multiplication

-   We can multiply a scalar by a vector
-   *λa*<sub>*i*</sub> = ⟨*λa*<sub>1</sub>, *λa*<sub>2</sub>⟩
-   Or multiply two vectors
-   $c\_{ij} = a\_i b\_j = \\begin{bmatrix}
    a\_1 b\_1 & a\_1 b\_2 \\\\
    a\_2 b\_1 & a\_2 b\_2
    \\end{bmatrix}$

----
## math laws

-   The usual laws (commutative, associative, distributive) still apply
-   *a*<sub>*i*</sub> + *b*<sub>*i*</sub> = *b*<sub>*i*</sub> + *a*<sub>*i*</sub>
-   *a*<sub>*ij*</sub>*b*<sub>*k*</sub> = *b*<sub>*k*</sub>*a*<sub>*ij*</sub>
-   *a*<sub>*i*</sub> + (*b*<sub>*i*</sub> + *c*<sub>*i*</sub>)=(*a*<sub>*i*</sub> + *b*<sub>*i*</sub>)+*c*<sub>*i*</sub>
-   *a*<sub>*i*</sub>(*b*<sub>*jk*</sub>*c*<sub>*l*</sub>)=(*a*<sub>*i*</sub>*b*<sub>*jk*</sub>)*c*<sub>*l*</sub>
-   *a*<sub>*ij*</sub>(*b*<sub>*k*</sub> + *c*<sub>*k*</sub>)=*a*<sub>*ij*</sub>*b*<sub>*k*</sub> + *a*<sub>*ij*</sub>*c*<sub>*k*</sub>

----
## equality

-   What does this mean? <!-- .element class="fragment" -->
    -  <!-- .element class="fragment" -->  
_a_<sub>*i*</sub> = *b*<sub>*i*</sub> 
    -  <!-- .element class="fragment" --> 
_a_<sub>1</sub> = *b*<sub>1</sub>, *a*<sub>2</sub> = *b*<sub>2</sub>, etc. 
-   What about this? <!-- .element class="fragment" --> 
    -  <!-- .element class="fragment" --> 
_a_<sub>*i*</sub> = *b*<sub>*j*</sub> 
    -  <!-- .element class="fragment" -->  Doesn’t make sense, incorrect use of index notation 

----
## dummy index

-   When an index is repeated in the same term, it is referred to as a “dummy index”
-   The dummy index indicates summation over all axes
-   e.g. *a*<sub>*ii*</sub> = *a*<sub>11</sub> + *a*<sub>22</sub> + *a*<sub>33</sub>
-   Note: summation on a matrix will reduce to a scalar, summation on higher order tensors will reduce the order by 2

----
## dummy index

-   The dummy index can be triggered by any repeated index in a .
-   Summation or not?
    -   *a*<sub>*i*</sub> + *b*<sub>*ij*</sub>*c*<sub>*j*</sub>
    -   *a*<sub>*ij*</sub> + *b*<sub>*ij*</sub>
    -   *a*<sub>*ij*</sub> + *b*<sub>*ij*</sub>*c*<sub>*j*</sub>

----
## matrix multiplication

-   How can we write matrix multiplication in index notation?

-   $\\begin{bmatrix}
    a\_{11} & a\_{12} \\\\
    a\_{21} & a\_{22}
    \\end{bmatrix}
    \\begin{bmatrix}
    b\_{11} & b\_{12} \\\\
    b\_{21} & b\_{22}
    \\end{bmatrix} =
    \\begin{bmatrix}
    c\_{11} & c\_{12} \\\\
    c\_{21} & c\_{22}
    \\end{bmatrix}$

-   <!-- .element class="fragment"-->
_c_<sub>11</sub> = *a*<sub>11</sub>*b*<sub>11</sub> + *a*<sub>12</sub>*b*<sub>21</sub>
-   <!-- .element class="fragment"-->
_c_<sub>12</sub> = *a*<sub>11</sub>*b*<sub>21</sub> + *a*<sub>12</sub>*b*<sub>22</sub>
-   <!-- .element class="fragment" -->
_c_<sub>*ij*</sub> = *a*<sub>*ik*</sub>*b*<sub>*kj*</sub>

----
## symmetry

-   Symmetry can be a very powerful tool in Elasticity
-   Here we define some useful forms of symmetry in index notation
-   Symmetric
    -   *a*<sub>*ij...z*</sub> = *a*<sub>*z...ji*</sub>
    -   *a*<sub>*ij...m...n...z*</sub> = *a*<sub>*ij...n...m...z*</sub>

----
## anti-symmetry
-   Anti-symmetric (skew symmetric)
    -   *a*<sub>*ij...z*</sub> = −*a*<sub>*z...ji*</sub>
    -   *a*<sub>*ij...m...n...z*</sub> = −*a*<sub>*ij...n...m...z*</sub>

----
## symmetry

-   Useful identity
    -   If *a*<sub>*ij...m...n...k*</sub> is symmetric in *mn* and *b*<sub>*pq...m...n...r*</sub> is antisymmetric in *mn*, then the product is zero
    -   *a*<sub>*ij...m...n...k*</sub>*b*<sub>*pq...m...n...r*</sub> = 0
-   We can also write any tensor as the sum of its symmetric and anti-symmetric parts
    -   $a\_{ij} = \\frac{1}{2} (a\_{ij} + a\_{ji}) + \\frac{1}{2} (a\_{ij} - a\_{ji})$

----
## symmetry

-   This textbook uses a special shortcut notation for the symmetric and anti-symmetric portions of a tensor
    -   Symmetric: $a\_{(ij)} = \\frac{1}{2}(a\_{ij}+a\_{ji})$
    -   Anti-symmetric: $a\_{\[ij\]} = \\frac{1}{2}(a\_{ij}-a\_{ji})$

----
## special symbols

-   For convenience we define two symbols in index notation
-   *Kronecker delta* is a general tensor form of the Identity Matrix

$$\\delta\_{ij} = \\left\\{
\\begin{array}{ll}
1& \\text{if $i=j$}\\\\
0& \\text{otherwise}
\\end{array}
\\right. = \\begin{bmatrix}
1 & 0 & 0\\\\
0 & 1 & 0 \\\\
0 & 0 & 1
\\end{bmatrix}$$

-   Is also used for higher order tensors

----
## Kronecker delta

-   *δ*<sub>*ij*</sub> = *δ*<sub>*ji*</sub>
-   *δ*<sub>*ii*</sub>= 3
-   *δ*<sub>*ij*</sub>*a*<sub>*j*</sub>= *a*<sub>*i*</sub>
-   *δ*<sub>*ij*</sub>*a*<sub>*ij*</sub>= *a*<sub>*ii*</sub>

----
## special symbols

-   *alternating symbol* or *permutation symbol*

$$\\epsilon\_{ijk} = \\left\\{
\\begin{array}{rl}
1 & \\text{if $ijk$ is an even permutation of 1,2,3}\\\\
-1 & \\text{if $ijk$ is an odd permutation of 1,2,3}\\\\
0 & \\text{otherwise}
\\end{array}
\\right.$$

----
## permutation symbol

-   This symbol is not used as frequently as the *Kronecker delta*
-   For our uses in this course, it is enough to know that 123, 231, and 312 are even permutations
-   321, 132, 213 are odd permutations
-   all other indexes are zero
-   *ϵ*<sub>*ijk*</sub>*ϵ*<sub>*imn*</sub> = *δ*<sub>*jm*</sub>*δ*<sub>*kn*</sub> − *δ*<sub>*jn*</sub>*δ*<sub>*mk*</sub>

----
## determinant

-   We use the alternating symbol for writing determinants and cross-products

$$\\det\[a\_{ij}\] = |a\_{ij}| = \\begin{vmatrix}
a\_{11} & a\_{12} & a\_{13}\\\\
a\_{21} & a\_{22} & a\_{23}\\\\
a\_{31} & a\_{32} & a\_{33}
\\end{vmatrix}
= \\epsilon\_{ijk}a\_{i1} a\_{j2} a\_{k3}$$

$$\\det\[a\_{ij}\] = \\frac{1}{6}\\epsilon\_{ijk} \\epsilon\_{pqr}a\_{ip}a\_{jq}a\_{kr}$$

----
## cross product

-   The cross-product can be written as a determinant:

$$\\hat{a} \\times \\hat{b} = \\begin{vmatrix}
\\hat{e}\_1 & \\hat{e}\_2 & \\hat{e}\_3\\\\
a\_1 & a\_2 & a\_3 \\\\
b\_1 & b\_2 & b\_3
\\end{vmatrix}$$

-   Or in index notation

$$\\hat{a} \\times \\hat{b} = \\epsilon\_{ijk} \\hat{e}\_i a\_j b\_k $$

----
## partial derivative

-   We indicate (partial) derivatives using a comma
-   In three dimensions, we take the partial derivative with respect to each variable (*x*, *y*, *z* or *x*<sub>1</sub>, *x*<sub>2</sub>, *x*<sub>3</sub>)
-   For example a scalar property, such as density, can have a different value at any point in space
-   *ρ* = *ρ*(*x*<sub>1</sub>, *x*<sub>2</sub>, *x*<sub>3</sub>)

$$\\rho\_{,i} = \\frac{\\partial}{\\partial x\_i} \\rho = \\left\\langle \\frac{\\partial \\rho }{\\partial x\_1}, \\frac{\\partial \\rho }{\\partial x\_2}, \\frac{\\partial \\rho }{\\partial x\_3} \\right\\rangle$$

----
## partial derivative

-   Similarly, if we take the partial derivative of a vector, it produces a matrix

$$u\_{i,j} = \\frac{\\partial}{\\partial x\_j} u\_i = \\begin{bmatrix}
\\frac{\\partial u\_1}{\\partial x\_1} & \\frac{\\partial u\_1}{\\partial x\_2} & \\frac{\\partial u\_1}{\\partial x\_3}\\\\
\\frac{\\partial u\_2}{\\partial x\_1} & \\frac{\\partial u\_2}{\\partial x\_2} & \\frac{\\partial u\_2}{\\partial x\_3}\\\\
\\frac{\\partial u\_3}{\\partial x\_1} & \\frac{\\partial u\_3}{\\partial x\_2} & \\frac{\\partial u\_3}{\\partial x\_3}
\\end{bmatrix}$$

---
# examples

----
## example 1

-   Write the following in conventional notation
    *T*<sub>*ij*, *j*</sub> + *F*<sub>*i*</sub> = 0
-   <!-- .element class="fragment" --> The comma indicates a partial derivative
-   <!-- .element class="fragment" --> The first index, 
_i_, is not repeated in any terms, so it is a “free index”
    -   This means in a 3D coordinate system, we will have at least three equations
-   <!-- .element class="fragment" --> The second index, 
_j_, is repeated in the first term, indicating summation.
    -   We will have exactly three equations

----
## example 1 (solution)

*T*<sub>*ij*, *j*</sub> + *F*<sub>*i*</sub> = 0

$$\\begin{aligned}
\\frac{\\partial T\_{11}}{\\partial x\_1} + \\frac{\\partial T\_{12}}{\\partial x\_2} + \\frac{\\partial T\_{13}}{\\partial x\_3} + F\_1= 0\\\\
\\frac{\\partial T\_{21}}{\\partial x\_1} + \\frac{\\partial T\_{22}}{\\partial x\_2} + \\frac{\\partial T\_{23}}{\\partial x\_3} + F\_2= 0\\\\
\\frac{\\partial T\_{31}}{\\partial x\_1} + \\frac{\\partial T\_{32}}{\\partial x\_2} + \\frac{\\partial T\_{33}}{\\partial x\_3} + F\_3= 0\\\\\\end{aligned}$$

----
## example 2

-   Identify whether the following expressions represent a scalar, vector, or matrix
-   If index notation is used incorrectly, give a reason why
-   *A*<sub>*i*</sub> = *B*<sub>*i*</sub>
-   *A*<sub>*i*</sub> = *B*<sub>*i*</sub> + *C*<sub>*i*</sub>*D*<sub>*i*</sub>
-   *δ*<sub>*ij*</sub>*A*<sub>*i*</sub>*B*<sub>*j*</sub>
-   $\\phi = \\frac{\\partial F\_i}{\\partial x\_i}$

----
## example 2 (solution)

-   Vector equation
-   Incorrect use of index notation, *i* used as both free and dummy index
-   Scalar value (both indexes are dummy indexes)
-   Scalar value (could also be written *F*<sub>*i*, *i*</sub>)


